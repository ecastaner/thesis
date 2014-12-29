from scipy.spatial import ConvexHull
import random as ran


class Polygon:

	def __init__(self):
		self.vertices = []
		self.inside = []
		self.current_amenities = None
		self.missing_amenities = None

		self.normalized_vertices = []

	def addVertices(self, vertices):
		self.vertices = vertices

	def addInside(self, points):
		self.inside = points

	def addPoints(self, points):
		convex_hull = ConvexHull(points)
		v_indices = convex_hull.vertices.tolist()
		vertices = [convex_hull.points[vertex].tolist() for vertex in v_indices]
		self.vertices = vertices
		v_set = set()
		for vertex in self.vertices:
			v_set = v_set and set(vertex)
		for vertex in points:
			v_set = v_set and set(vertex)
		self.inside = list(v_set)

	def addNormalizedVertices(self, vertices):
		self.normalized_vertices = vertices

	def addCurrentAmenities(self, cur_amenities):
		self.current_amenities = cur_amenities

	def addMissingAmenities(self, miss_amenities):
		self.missing_amenities = miss_amenities

	def getVertices(self):
		return self.vertices

	def getInside(self):
		return self.inside

	def getPoints(self):
		return self.vertices + self.inside


	#just for the purpose of creating fake data set
	def generateRandomAmenitiesPerc(self, n):
		r = [ran.random() for i in range(n)]
		s = sum(r)
		r = [ str(i/s) for i in r ]
		return r

	#prints NORMALIZED polygon in the form:
	#list of vertices,|, % of cur_amenties,|, % of missing_amenities
	def __str__(self):
		out = ''
		for vertex in self.normalized_vertices:
			out += str(vertex[0]) + "," + str(vertex[1]) + ","
		out += "|,"
		perc_current_amenities = self.generateRandomAmenitiesPerc(10)
		perc_missing_amenities = self.generateRandomAmenitiesPerc(10)
		out += ",".join(perc_current_amenities)
		out += ",|,"
		out += ",".join(perc_missing_amenities)
		return out



