from scipy.spatial import ConvexHull


class DrawPolygons:
	#clusters:  <(lat, lon), [(lat, lon),(lat, lon)]>
	def __init__(self, clusters):
		self.clusters = clusters
		self.cluster_centers = clusters.keys()

	#points: [(lat, lon),(lat, lon)]
	def getConvexHull(self, points):
		return ConvexHull(points)

	
	def 





f = open('clusters.csv', 'r')
