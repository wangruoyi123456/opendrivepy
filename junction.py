

class Junction(object):
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.connections = list()
        self.priorities = list()
        self.controllers = list()

    def add_connection(self, connection):
        self.connections.append(connection)


class Connection(object):
    def __init__(self, id, incoming_road, connecting_road, contact_point):
        self.id = id
        self.incoming_road = incoming_road
        self.connecting_road = connecting_road
        self.contact_point = contact_point
        self.lane_link = list()

# TODO Add Priorities, JunctionGroups and LaneLinks

