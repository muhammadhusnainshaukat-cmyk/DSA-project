# src/city.py
# Zone-based city graph representation with shortest path algorithm

class City:
    def __init__(self):
        # Custom adjacency list (no STL containers)
        self.adj_list = {}
        self.zones = {}  # zone_name -> list of locations
        self.location_zones = {}  # location -> zone_name
        self.location_coords = {}  # location -> (x, y) coordinates for visualization

    def add_location(self, name, zone=None, x=0, y=0):
        """Add a location (node) to the city graph"""
        if name not in self.adj_list:
            self.adj_list[name] = []
            self.location_coords[name] = (x, y)
            
            if zone:
                self.location_zones[name] = zone
                if zone not in self.zones:
                    self.zones[zone] = []
                self.zones[zone].append(name)

    def add_road(self, from_loc, to_loc, distance):
        """Add a bidirectional road (edge) between two locations"""
        # Ensure both locations exist
        if from_loc not in self.adj_list:
            self.add_location(from_loc)
        if to_loc not in self.adj_list:
            self.add_location(to_loc)

        # Add undirected edge
        self.adj_list[from_loc].append((to_loc, distance))
        self.adj_list[to_loc].append((from_loc, distance))

    def get_neighbors(self, location):
        """Get all neighbors of a location"""
        if location in self.adj_list:
            return self.adj_list[location]
        return []

    def shortest_path(self, start, end):
        """Dijkstra's algorithm for shortest path"""
        if start not in self.adj_list or end not in self.adj_list:
            return float('inf'), []

        dist = {node: float('inf') for node in self.adj_list}
        prev = {node: None for node in self.adj_list}
        visited = {node: False for node in self.adj_list}

        dist[start] = 0

        while True:
            # Find unvisited node with minimum distance
            current = None
            min_dist = float('inf')

            for node in self.adj_list:
                if not visited[node] and dist[node] < min_dist:
                    min_dist = dist[node]
                    current = node

            if current is None or current == end:
                break

            visited[current] = True

            # Update distances to neighbors
            for neighbor, weight in self.adj_list[current]:
                if not visited[neighbor]:
                    new_dist = dist[current] + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        prev[neighbor] = current

        # Reconstruct path
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = prev[node]
        path.reverse()

        if dist[end] == float('inf'):
            return float('inf'), []
        
        return dist[end], path

    def get_zone(self, location):
        """Get the zone of a location"""
        return self.location_zones.get(location, None)

    def is_cross_zone(self, loc1, loc2):
        """Check if two locations are in different zones"""
        zone1 = self.get_zone(loc1)
        zone2 = self.get_zone(loc2)
        if zone1 and zone2:
            return zone1 != zone2
        return False

    def get_cross_zone_multiplier(self, loc1, loc2):
        """Return fare multiplier for cross-zone trips"""
        if self.is_cross_zone(loc1, loc2):
            return 1.5  # 50% extra for cross-zone
        return 1.0

    def get_all_locations(self):
        """Get all locations in the city"""
        return list(self.adj_list.keys())

    def get_all_roads(self):
        """Get all roads as (from, to, distance) tuples"""
        roads = []
        seen = set()
        for from_loc, neighbors in self.adj_list.items():
            for to_loc, distance in neighbors:
                edge = tuple(sorted([from_loc, to_loc]))
                if edge not in seen:
                    roads.append((from_loc, to_loc, distance))
                    seen.add(edge)
        return roads

    def get_location_coords(self, location):
        """Get coordinates of a location"""
        return self.location_coords.get(location, (0, 0))

    def set_location_coords(self, location, x, y):
        """Set coordinates of a location"""
        if location in self.adj_list:
            self.location_coords[location] = (x, y)