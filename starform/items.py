#! usr/bin/env python
# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class linksItem(Item):
	racelink   = Field()
	# raceid     = Field()
	# racedate   = Field()
	# racetime   = Field()
	# racecourse = Field()
	# distance   = Field()
	# furlongs   = Field()	
	# racetype   = Field()
	# going      = Field()	
	# runners	   = Field()
	pass

class cardsItem(Item):
	cardid = Field()	
	cardlink = Field()
	racedate = Field()
	racetime = Field()
	racecourse = Field()
	racecode = Field()
	raceclass = Field()
	racetype = Field()
	agerange = Field()
	prize = Field()
	going = Field()
	distance = Field()
	furlongs = Field()
	draw = Field()
	runners = Field()
	racecardno = Field()
	racehorse = Field()
	rhid = Field()
	formline = Field()
	dslr = Field()	
	crswins = Field()
	tfprediction  = Field()
	tfpredcomment = Field()
	fcprice = Field()
	age = Field()
	weight = Field()
	o_r = Field()
	eq = Field()
	jockey = Field()
	allwnce = Field()
	trainer = Field()	
	backprice = Field()
	backsize = Field()
	layprice = Field()
	laysize	= Field()
	rhcomment = Field()
	mktlink = Field()
	rhlink = Field()
	jklink = Field()
	trlink = Field()
	pass

class resultsItem(Item):
	# raceid = Field()	
	racelink = Field()
	racedate = Field()
	racetime = Field()
	racecourse = Field()
	rcid = Field()
	racenumber = Field()
	racecode = Field()
	raceclass = Field()
	racetype = Field()
	racetitle = Field()
	agerange = Field()
	prize = Field()
	going = Field()
	distance = Field()
	furlongs = Field()
	draw = Field()
	racehorse = Field()
	# rhlink = Field()
	age = Field()
	weight = Field()
	o_r = Field()
	eq = Field()
	jockey = Field()
	allowance = Field()
	trainer = Field()
	rhid = Field()
	jkid = Field()
	trid = Field()		
	position = Field()
	distbtn = Field()
	totdistbtn = Field()
	isp = Field()
	bsp = Field()
	place = Field()
	hi_ir = Field()
	lo_ir = Field()
	wintime = Field()	
	# ran = Field()
	pass

class rhsummItem(Item):
	rhid = Field()
	racehorse = Field()
	age = Field()
	colour = Field()
	horsetype = Field()
	sire = Field()
	dam = Field
	trainer = Field()
	owner = Field()
	category = Field()
	runs = Field()
	first = Field()
	second = Field()
	third = Field()
	fourth = Field()
	prize = Field()
	wins = Field()
	profit = Field()
	lsp = Field()
	pass

class rhformItem(Item):
	rhid = Field()
	racehorse = Field()
	racedate = Field()
	raceid = Field()
	racelink = Field()
	racecourse = Field()
	position = Field()
	ran = Field()
	distance = Field()
	furlongs = Field()
	going = Field()
	o_r = Field()
	eq = Field()
	racetype = Field()
	jockey = Field()
	jkid = Field()
	hi_ir = Field()
	lo_ir = Field()
	isp = Field()
	bsp = Field()
	place = Field()	
	pass	

class jkformItem(Item):
	jkid = Field()
	jockey = Field()
	racedate = Field()
	raceid = Field()
	racelink = Field()
	racecourse = Field()
	position = Field()
	ran = Field()
	distance = Field()
	furlongs = Field()
	going = Field()
	o_r = Field()
	eq = Field()
	racetype = Field()
	trainer = Field()
	trid = Field()
	racehorse = Field()
	rhid = Field()	
	hi_ir = Field()
	lo_ir = Field()
	isp = Field()
	bsp = Field()
	place = Field()	
	pass

class trformItem(Item):
	trid = Field()
	trainer = Field()
	racedate = Field()
	raceid = Field()
	racelink = Field()
	racecourse = Field()
	position = Field()
	ran = Field()
	distance = Field()
	furlongs = Field()
	going = Field()
	o_r = Field()
	eq = Field()
	racetype = Field()
	jockey = Field()
	jkid = Field()
	racehorse = Field()
	rhid = Field()	
	hi_ir = Field()
	lo_ir = Field()
	isp = Field()
	bsp = Field()
	place = Field()	
	pass	