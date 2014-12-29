from scipy.spatial import ConvexHull
import Polygon

#Script:
#Given clusters of poitns draws polygons delimiting clusters
#Writes a file where each line represents each polygon boundaries

#Requirement: file - clusters_cityname.csv

def drawPolygons(cityname):
	#each line in file represents a cluster, and should have format:
	#	center lat, center lon, lat1, lon1, lat2, lon2, etc
	f = open('clusters_'+cityname+'.csv', 'r')
	city = CityPolygons(cityname)
	for line in f:
		points = f.split()
		cluster_points = []
		for i in range(0, len(points), 2):
			cluster_points.append([float(points[i]), float(points[i+1])])
		poly = Polygon
		poly.addPoints(cluster_points)
		city.addPolygon(poly)
	
