var Promise = require("bluebird")
var sugar = require("sugar")
var _ = require('lodash')
var crawler = require('./crawler.js');

var startDate = process.argv[2]
var endDate = process.argv[3]

var startObject = Date.create(startDate).beginningOfDay()
var endObject = Date.create(endDate).beginningOfDay()
var dateList = []
var advancer = {
	day:1
}

while(endObject.getTime() >= startObject.getTime()){
	dateList.push(startObject.clone())
	startObject.advance(advancer)
}

_.reduce(dateList,function(memo,dt){
		return memo.then(function(){
			return crawler.crawl(dt)
		})
	},Promise.resolve())