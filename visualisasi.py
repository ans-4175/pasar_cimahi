from os import listdir
from os.path import isfile, join
import json

import matplotlib.pyplot as plt

xaxis = []
barangs = []
harga_atas = []
harga_cimindi = []
harga_melong = []
berapa_tulis = 0
for date in [f for f in listdir('data') if isfile(join('data', f))]:
    berapa_tulis = 0 if berapa_tulis == 5 else berapa_tulis + 1
    xaxis.append(date[5:10] if berapa_tulis == 1 else '')
    with open(join('data', date)) as infile:
        mentah = json.load(infile)
        barangs = [barang for barang in mentah if barang['barang'] == 'Daging Ayam Broiler']
        harga_atas.append(barangs[0]['pasar_atas'])
        harga_cimindi.append(barangs[0]['pasar_cimindi'])
        harga_melong.append(barangs[0]['pasar_melong'])

fig, ax = plt.subplots()
ax.plot(harga_atas, label='Pasar Atas')
ax.plot(harga_cimindi, label='Pasar Cimindi')
ax.plot(harga_melong, label='Pasar Melong')

plt.xticks(range(len(xaxis)), xaxis, rotation=45)

# Now add the legend with some customizations.
legend = ax.legend(loc='upper center', shadow=True)

# The frame is matplotlib.patches.Rectangle instance surrounding the legend.
frame = legend.get_frame()
frame.set_facecolor('0.90')

# Set the fontsize
for label in legend.get_texts():
    label.set_fontsize('large')

for label in legend.get_lines():
    label.set_linewidth(1.5)  # the legend line width

x1,x2,y1,y2 = plt.axis()
plt.axis((x1, x2, 10000, 200000))

plt.grid(True)
plt.show()