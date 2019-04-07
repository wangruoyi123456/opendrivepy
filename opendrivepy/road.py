from __future__ import division, print_function, absolute_import

from opendrivepy.point import EndPoint

class Road(object):
    def __init__(self, name, length, id, junction):
        self.name = name
        self.length = length
        self.id = id
        self.junction = junction
        self.predecessor = RoadLink
        self.successor = RoadLink
        self.types = list()
        self.plan_view = list()
        self.elevation_profile = None
        self.lateral_profile = None  # Not implemented
        self.lanes = None
        self.signals = None

        # Points that represent the road
        # Endpoints between records are duplicated atm
        self.points = list()
        self.segments = list()

        self.start_point = EndPoint
        self.end_point = EndPoint

    def update(self):
        self.generate_points()
        self.generate_segments()
        self.update_endpoints()

    def generate_points(self):
        for record in self.plan_view:
            self.points.extend(record.points)

    def generate_segments(self):
        for record in self.plan_view:
            self.segments.extend(record.segments)

    def draw_road(self):
        for record in self.plan_view:
            record.graph()

    # Updates the values of self.startPoint and self.endPoint based on the road array
    def update_endpoints(self):
        if self.plan_view is not None:
            x = self.points[0].x
            y = self.points[0].y
            self.start_point = EndPoint(x, y, self.id, 'start')

            x = self.points[-1].x
            y = self.points[-1].y
            self.end_point = EndPoint(x, y, self.id, 'end')

    # Determines if b
    def in_range(self, other):
        sp = self.start_point.distance(other)
        if self.start_point.distance(other) <= self.length:
            return True

        return False

    # WARNING: This only works so far with a fix width. Simplified for testing purposes
    def get_left_width(self, n):
        width = 0
        for lane in self.lanes.lane_section.left:
            width += lane.width.a

        return width

    def get_right_width(self, n):
        width = 0
        for lane in self.lanes.lane_section.right:
            width += lane.width.a

        return width


class RoadLink(object):
    def __init__(self, element_type, element_id, contact_point):
        self.element_type = element_type
        self.element_id = element_id
        self.contact_point = contact_point


class RoadType(object):
    def __init__(self, s, type, speeds):

        # Attributes
        self.s = s
        self.type = type

        # Elements
        self.speeds = speeds


class RoadSpeed(object):
    def __init__(self, max, unit):
        self.max = max
        self.unit = unit


