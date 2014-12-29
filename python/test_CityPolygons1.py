import Polygon
import CityPolygons

#tests function normalizePolygons()

pol1 = [[1.0,1.0],[1.0,2.0],[2.0,1.0],[2.0,2.0]]
pol2 = [[3.0,3.0],[3.0,4.0],[4.0,3.0]]
pol3 = [[6.0,1.0],[6.0,3.0],[8.0,1.0],[8.0,3.0]]

p1 = Polygon.Polygon()
p2 = Polygon.Polygon()
p3 = Polygon.Polygon()

p1.addPoints(pol1)
p2.addPoints(pol2)
p3.addPoints(pol3)

city = CityPolygons.CityPolygons('test')
city.addPolygon(p1)
city.addPolygon(p2)
city.addPolygon(p3)

city.normalizePolygons()
print str(city)