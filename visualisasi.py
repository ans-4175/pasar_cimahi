import os
import os.path as path
import json

import matplotlib.pyplot as plt
import matplotlib
# matplotlib.style.use('ggplot')
import numpy as np
import pandas as pd

search = 'Bawang Merah'
pasars = ['atas', 'cimindi', 'melong']
datatest = 'data/test'

# parsing
index, data = [], []
for date in [f for f in os.listdir(datatest) if path.isfile(path.join(datatest, f))]:
    with open(path.join(datatest, date)) as file:
        barangs = json.load(file)
    index.append(pd.to_datetime(date[0:10]))
    barang = next((x for x in barangs if x['barang'] == search), None)
    hargas = []
    for pasar in pasars:
    	if barang is not None:
        	harga = barang['pasar_'+pasar]
        	hargas.append(np.nan if barang is None else np.nan if harga < 1000 else harga)
    data.append(hargas)

# preparing
df = pd.DataFrame(data, index=index, columns=pasars)
df.plot()

# show
y1, y2 = plt.ylim()
plt.ylim((y1-1000, y2+1000))
plt.show()