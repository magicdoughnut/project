import shapefile as shp
import matplotlib.pyplot as plt
from descartes import PolygonPatch
from shapely.geometry import LineString
from shapely.geometry import Polygon
import csv
from matplotlib.colors import LinearSegmentedColormap
import numpy as np


vals = []
names = []
with open('RensResWind.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	print row[1]
        vals.append(float(row[1]))
        names.append(row[0])

cvals = {}
for i in range(0,len(vals)):
	# cvals.append(i/max(vals))
	cvals[names[i]] = vals[i]/max(vals)
	print max(vals)

cvals['United Kingdom'] = cvals['UK']
del cvals['UK']
print cvals


cm = plt.cm.get_cmap('Greens')



fig = plt.figure()
ax = fig.gca()

polys  = shp.Reader("TM_WORLD_BORDERS-0.3/TM_WORLD_BORDERS-0.3.shp")
geomet = polys.shapeRecords() #will store the geometry separately
first = geomet[0] #will extract the first polygon to a new object
# first.shape.points #will show you the points of the polygon
first.record #will show you the attributes
print(first.record[4])

multis = []
COLOUR = '#6699cc' #BLUE
for i in range(0,polys.numRecords):
	poly = polys.shape(i).__geo_interface__
	# poly = polys.iterShapes().next().__geo_interface__
	no = geomet[i]
	GISname = no.record[4]
	# if GISname[1:-1] == 'land Islands':
	# 	GISname = 'Island4000'
	# 	print fuck*100
	if GISname == "Italy":
		print "ITALY"*20
		print poly['type']
	print GISname


	if GISname in cvals.keys():
		print 'YES!'
		ccoulor = cm(cvals[GISname])
		hval = ' '
	else:
		ccoulor = '0.75'
		hval = 'x'

	if poly['type'] != 'MultiPolygon':
		a = ax.add_patch(PolygonPatch(poly, fc=ccoulor, ec='k', alpha=1, zorder=2,hatch = hval))
	else:
		for j in poly['coordinates']:
			for k in j:
				poly = Polygon(k)
				if poly.is_empty:
					print 'hi'
				else:
					b = ax.add_patch(PolygonPatch(poly, fc=ccoulor, ec='k', alpha=1, zorder=2,hatch = hval))

hval = ''
legPoly = {'type': 'Polygon','coordinates':[((90,90),(91,90),(91,91),(90,91),(90,90))]}
c = ax.add_patch(PolygonPatch(legPoly, fc=cm(30000/max(vals)), ec='k', alpha=1, zorder=2,label='USD30b',hatch = hval))

legPoly = {'type': 'Polygon','coordinates':[((90,90),(91,90),(91,91),(90,91),(90,90))]}
d = ax.add_patch(PolygonPatch(legPoly, fc=cm(20000/max(vals)), ec='k', alpha=1, zorder=2,label='USD20b',hatch = hval))

legPoly = {'type': 'Polygon','coordinates':[((90,90),(91,90),(91,91),(90,91),(90,90))]}
e = ax.add_patch(PolygonPatch(legPoly, fc=cm(10000/max(vals)), ec='k', alpha=1, zorder=2,label='USD10b',hatch = hval))

hval  = 'x'
legPoly = {'type': 'Polygon','coordinates':[((90,90),(91,90),(91,91),(90,91),(90,90))]}
f = ax.add_patch(PolygonPatch(legPoly, fc='0.75', ec='k', alpha=1, zorder=2,label='No Data',hatch = hval))


plt.legend(handles=[c,d,e,f])
ax.axis('scaled')
ax.axis([-15, 25, 35, 65])
ax.legend(loc='upper right')
plt.savefig('RenResWind.png')
plt.show()


