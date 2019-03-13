from src.point import EndPoint


class Road(object):
    def __init__(self, name, length, id, junction, predecessor, successor, plan_view):
        self.name = name
        self.length = length
        self.id = id
        self.junction = junction
        self.predecessor = predecessor
        self.successor = successor
        self.type = list()
        self.plan_view = plan_view
        self.elevation_profile = None
        self.lateral_profile = None
        self.lanes = None

        # Points that represent the road
        # Endpoints between records are duplicated atm
        self.points = list()
        self.generate_points()
        self.segments = list()
        self.generate_segments()

        self.start_point = EndPoint
        self.end_point = EndPoint
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


class RoadLink(object):
    def __init__(self, element_type, element_id, contact_point):
        self.element_type = element_type
        self.element_id = element_id
        self.contact_point = contact_point
