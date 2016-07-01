from __future__ import division
import csv, operator, requests, time, datetime
from collections import defaultdict, Counter
import pylab as pl
from numpy import array
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from math import *
from sklearn.ensemble import RandomForestRegressor


features, price, all_prices, min_price, max_price = [], [], [], 0, 0


def get_min_max_price(all_prices):

	min_price = all_prices[int(len(all_prices)/4)]
	max_price = all_prices[int(0.95*len(all_prices))]
	
	# return min_price, max_price


def tofloat(value):
  try:
    float(value)
    return float(value)
  except ValueError:
    return value



with open("nndata.csv", "rb") as nn1:
	nn = csv.DictReader(nn1)

	nnprice = [tofloat(lis["price_per_unit"]) for lis in nn if lis["price_per_unit"]]
	all_prices.extend(nnprice)


with open("mbdata.csv", "rb") as mb1:
	mb = csv.DictReader(mb1)

	mbprice = [tofloat(lis["price_per_unit"]) for lis in mb if lis["price_per_unit"]]

	# mbprice = [log(i) for i in mbprice]

	# print mbprice
	all_prices.extend(mbprice)
	all_prices.sort()
	min_price, max_price = all_prices[0], all_prices[len(all_prices)-1]




with open("nndata.csv", "rb") as infile1:
	nn = csv.DictReader(infile1)
	# nnacres = [[i["area"], i["floor"], i["total_floors"], i["price_per_unit"], i[""]] for i in nn if i["area"] and i["floor"] and i["total_floors"] and i["price_per_unit"]]
	nn_features, nn_price = zip(*[[[tofloat(lis["area"]), tofloat(lis["reserved_parking"]), tofloat(lis["floor"]), tofloat(lis["total_floors"]), tofloat(lis["prop_age"])], [sqrt(tofloat(lis["price_per_unit"]))]] for lis in nn if lis["area"] and lis["reserved_parking"] and lis["floor"] and lis["total_floors"] and lis["prop_age"] and lis["price_per_unit"] and tofloat(lis["price_per_unit"]) > min_price and tofloat(lis["price_per_unit"]) < max_price])

	features.extend(nn_features)
	price.extend(nn_price)


with open("mbdata.csv", "rb") as infile2:
	mb = csv.DictReader(infile2)
	# mbricks = [[i["area"], i["floor"], i["total_floors"], i["price_per_unit"]] for i in mb if i["area"] and i["floor"] and i["total_floors"] and i["price_per_unit"]]
	mb_features, mb_price = zip(*[[[tofloat(lis["area"]), tofloat(lis["reserved_parking"]), tofloat(lis["floor"]), tofloat(lis["total_floors"]), tofloat(lis["prop_age"])], [sqrt(tofloat(lis["price_per_unit"]))]] for lis in mb if lis["area"] and lis["reserved_parking"] and lis["floor"] and lis["total_floors"] and lis["prop_age"] and lis["price_per_unit"] and tofloat(lis["price_per_unit"]) > min_price and tofloat(lis["price_per_unit"]) < max_price])

	# for lis in mb: 
	# 	print tofloat(lis["price_per_unit"])
	features.extend(mb_features)
	price.extend(mb_price)


def regressor_test(features, price):

	datalen = len(price)

	clf = RandomForestRegressor(n_estimators=30)
	clf = clf.fit(features[0:int(3*datalen/4)], price[0:int(3*datalen/4)])

	print "feature importance ", clf.feature_importances_

	pred = clf.predict(features[int(3*datalen/4):datalen])
	pred = [i**2 for i in pred]
	req = price[int(3*datalen/4):datalen]

	req_p = [(float(i[0]))**2 for i in req]

	err = []

	for i in range(len(req)):
		err.append(abs((float(req_p[i])-float(pred[i]))/float(req_p[i])))

	err.sort()

	print "actual values 	", req
	print "predicted values 	", pred
	print "individual errors  	", err
	print "average error rate 	 ", sum(err) / len(err)
	print "max error 	  ", max(err)



get_min_max_price(all_prices)
regressor_test(features, price)


