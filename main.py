from roadgeometry import RoadLine, RoadArc, RoadSpiral
import matplotlib.pyplot as plt
from xmlparser import XMLParser
from lxml import etree

# road1 = RoadLine(0, 7.0710678120487289e+00, 7.0710678117015151e+00, 3.9269908169686372e+00, 4.8660000002387466e-01)
# road5 = RoadLine(1.6031224248136859e+01, -6.7269902520731444e+00, 6.7269896521996131e+00, 2.3561944901771223e+00, 4.8660000002378739e-01)
#
# road2 = RoadSpiral(4.8660000002387466e-01, 6.7269896523017803e+00,
#                    6.7269896519639518e+00, 3.9269908169720189e+00,
#                    3.1746031746031744e+00, 0, -1.2698412698412698e-01)
#
# road4 = RoadSpiral(1.2856621073533685e+01, -4.3409256447380580e+00,
#                    4.6416930099307159e+00, 2.5577565965011333e+00,
#                    3.1746031746031744e+00, -1.2698412698412698e-01, -0.0000000000000000e+00)
#
# road3 = RoadArc(3.6612031746270493e+00,
#                 4.3409250448908985e+00,
#                 4.6416930097877751e+00,
#                 3.7254287106480075e+00,
#                 9.1954178989066371e+00,
#                 -1.2698412698412698e-01)
#
# # roada = RoadArc(0, 0, 1, math.pi, 28, -1.2698412698412698e-01)
#
#
# road1.graph()
# road5.graph()
# road3.graph()
# road2.graph()
# road4.graph()
# plt.plot(-4.3409256447380580e+00, 4.6416930099307159e+00, 'r+')
#
# plt.xlim(-10, 10)
# plt.ylim(0, 20)
# plt.show()

# Crossing8Course.xodr
parser = XMLParser('Crossing8Course.xodr')
roads = parser.parse_roads()
for road in roads:
    road.draw_road()
plt.show()
