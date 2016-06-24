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


listings, req_dpoints, req_price = [], [], []

with open("nndata.csv", "rb") as csvfile:
	listings = csv.DictReader(csvfile)

# '''
# 	Plot graphs, vizualize data in 2-D.
# '''
	
	# price, total_floors, floor, prop_age, r_park, area, bed = zip(*[(float(lis["price_per_unit"]), float(lis["total_floors"]), float(lis["floor"]), float(lis["prop_age"]), float(lis["reserved_parking"]), float(lis["area"]), float(lis["bed"])) for lis in listings if lis["price_per_unit"] and lis["total_floors"] and lis["floor"] and lis["prop_age"] and lis["reserved_parking"] and lis["area"] and lis["bed"]])
	# prop_age = map(lambda x: (x+1)*15, prop_age)
	# price = map(lambda x: x/100, price)
	# floor = map(lambda x: (x+1)*7, floor)
	# price, total_floors, floor = np.array(price), np.array(total_floors), np.array(floor)



	# plt.scatter(area, price, c=prop_age, s=50)

	# xlabel("area")
	# ylabel("price")
	
	# plt.show()


# '''
# 		Estimator using random-forest regressor.
# '''
	
	req_dpoints, req_price = zip(*[([lis["area"], lis["bed"], lis["bath"], lis["balcony"], lis["reserved_parking"], lis["floor"], lis["total_floors"], lis["east"], lis["west"], lis["north"], lis["northEast"], lis["prop_age"]], [lis["price_per_unit"]]) for lis in listings if lis["area"] and lis["bed"] and lis["bath"] and lis["balcony"] and lis["reserved_parking"] and lis["floor"] and lis["total_floors"] and lis["east"] and lis["west"] and lis["north"] and lis["northEast"] and lis["prop_age"] and lis["price_per_unit"]])

	datalen = len(req_dpoints)


	clf = RandomForestRegressor(n_estimators=50)
	clf = clf.fit(req_dpoints[0:int(3*datalen/4)], req_price[0:int(3*datalen/4)])
	imp = clf.feature_importances_

	pred = clf.predict(req_dpoints[int(3*datalen/4):datalen])
	req = req_price[int(3*datalen/4):datalen]

	req_p = [float(i[0]) for i in req]

	# err = clf.score(req_dpoints[37:49], req_price[37:49])
	err = []


	for i in range(len(req)):
		err.append(abs((float(req_p[i])-float(pred[i]))/float(req_p[i])))

	err.sort()

	

	print "regressor 	 ", clf 
	print "feature importances  	", imp
	print "actual values 	", req
	print "predicted values 	", pred
	print "individual errors  	", err
	print "average error rate 	 ", sum(err) / len(err)
	

	# print err[int(len(err)/2)]



	# pred1 = clf.predict([2195.0, 4, 4, 4, 11, 15, 0, 0, 1, 0, 2])
	# pred2 = clf.predict([2195.0, 4, 4, 4, 11, 15, 1, 0, 0, 0, 2])
	# pred3 = clf.predict([2195.0, 4, 4, 4, 11, 15, 0, 0, 1, 0, 2])
	# pred4 = clf.predict([2195.0, 4, 4, 4, 11, 15, 1, 0, 0, 0, 2])
	# pred = clf.predict([1630.0, 3, 4, 3, 0, 8, 15, 1, 0, 0, 0, 2])
	# print pred1, pred2, pred3, pred4





# area,price_cr,price_per_unit,bed,bath,balcony,reserved_parking,floor,total_floors,
# east,west,north,south,northEast,southEast,northWest,southWest,
# possession,prop_age,freehold,lease,dealer_name


# def req_points(listings):

# 	req_dpoints, req_price = zip(*[([lis["area"], lis["bed"], lis["bath"], lis["balcony"], lis["reserved_parking"], lis["floor"], lis["total_floors"], lis["east"], lis["west"], lis["north"], lis["northEast"], lis["prop_age"]], [lis["price_per_unit"]]) for lis in listings if lis["area"] and lis["bed"] and lis["bath"] and lis["balcony"] and lis["reserved_parking"] and lis["floor"] and lis["total_floors"] and lis["east"] and lis["west"] and lis["north"] and lis["northEast"] and lis["prop_age"] and lis["price_per_unit"]])

# 	print len(req_dpoints), len(req_price)


# req_points(listings)

# nnacres, mbricks = [], []

# with open("data.csv", "rb") as infile1:
# 	nn = csv.DictReader(infile1)
# 	nnacres = [[i["area"], i["floor"], i["total_floors"], i["price_per_unit"]] for i in nn if i["area"] and i["floor"] and i["total_floors"] and i["price_per_unit"]]

# with open("mbVipulgreen.csv", "rb") as infile2:
# 	mb = csv.DictReader(infile2)
# 	mbricks = [[i["area"], i["floor"], i["total_floors"], i["price_per_unit"]] for i in mb if i["area"] and i["floor"] and i["total_floors"] and i["price_per_unit"]]


# # print type(nnacres[0][0]), type(mbricks[0][0])
# def check_variation(nnacres, mbricks):

# 	same_lis = [abs((float(i[3])-float(j[3]))/float(i[3])) for i in nnacres for j in mbricks if float(i[1])==float(j[1]) and float(i[2])==float(j[2])]

# 	print len(same_lis)
# 	same_lis.sort()
# 	print same_lis

# check_variation(nnacres, mbricks)










