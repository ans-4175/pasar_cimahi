var request = require('request');
var cheerio = require('cheerio');
var Promise = require("bluebird")
var sugar = require("sugar")
var _ = require('lodash')
var fse = require("fs-extra")

function hitURL(date){
	var url = "http://uptpasar.cimahikota.go.id/viewdata/surveypasar/surveypasarlist?cari=Cari&tanggalsurvey="
	return new Promise(function(resolve,reject){
		request({
			url:url+date,
			method:'get'
		},function(err,response,body){
			if (!err)
				resolve(body)
			else
				reject(err)
		})
	})
}

function crawlData(dt){
	var realDate = dt.format('{dd}-{MM}-{yyyy}');
	var dtName = dt.format('{yyyy}-{MM}-{dd}');
	return new Promise(function(resolve){
		hitURL(realDate)
			.then(function(html){
				var $ = cheerio.load(html);
				var prices = []
				$('tr.event').each(function(i, element){
					try{
						var data = {
							timestamp: dt.getTime(),
							barang: $(this).find('td')[1].children[0].data,
							satuan: $(this).find('td')[2].children[0].data,
							pasar_atas: parseInt($(this).find('td')[3].children[0].data.replace(".", "")),
							pasar_cimindi: parseInt($(this).find('td')[4].children[0].data.replace(".", "")),
							pasar_melong: parseInt($(this).find('td')[5].children[0].data.replace(".", "")),
							rerata: parseInt($(this).find('td')[6].children[0].data.replace(".", ""))
						}
						prices.push(data)
					}catch(e){
						console.error(e)		
					}
				})
				if (!fse.existsSync("./data/")){
				    fse.mkdirSync("./data/");
				}
				fse.writeFile("./data/"+dtName+".json",JSON.stringify(prices),function(err){
					console.log("Is error on writing?",realDate, err)
					resolve(true)
				})
			})
			.catch(function(e){
				console.error(realDate, e)
				resolve(false)
			})
	})
}

var Engine = {}
Engine.crawl = crawlData
module.exports = Engine