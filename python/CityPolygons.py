
import Polygon
import numpy as np
from scipy.spatial import Voronoi, voronoi_plot_2d
from scipy.spatial import ConvexHull

#Representation of a city as a set of polygons.
class CityPolygons:

	def __init__(self, name):
		self.polygons = []
		self.name = name

	def addPolygon(self, polygon):
		self.polygons.append(polygon)

	def addPolygons(self, polygons):
		self.polygons += polygons

	def getPolygons(self):
		return polygons

	def normalizePolygons(self):
		i = 0
		start = 0
		poly_dict = {}
		all_points = []
		for poly in self.polygons:
			poly_points = poly.getPoints()
			all_points += poly_points
			poly_dict[i] = (poly, start, start + len(poly_points))
			i += 1
			start += len(poly_points)
		vor = Voronoi(all_points)

		regions = vor.regions[1:]
		for poly, start, end in poly_dict.values():
			
			poly_region_list = []
			for i in range(start, end):
				poly_region_list.extend(vor.regions[vor.point_region[i]])

			poly_region_set = set(poly_region_list)
			poly_vertex_list = []
			for v in poly_region_set:
				if v != -1:
					poly_vertex_list.append(vor.vertices[v].tolist())

			all_vertices = poly_vertex_list + poly.getVertices()
			all_edges = ConvexHull(all_vertices)

			normalized_vertices = []
			for vtx in all_edges.vertices:
				normalized_vertices.append(all_edges.points[vtx].tolist())

			poly.addNormalizedVertices(normalized_vertices)


	#prints string where every line represents a polyogon (see polygon.str)
	def __str__(self):
		out = ''
		for poly in self.polygons:
			out += str(poly) + '\n'
		return out






