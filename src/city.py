class City:
    def __init__(self):
        # adjacency list
        self.adj_list = {}

    def add_location(self, name):
        if name not in self.adj_list:
            self.adj_list[name] = []

    def add_road(self, from_loc, to_loc, distance):
        self.add_location(from_loc)
        self.add_location(to_loc)

        # undirected graph
        self.adj_list[from_loc].append((to_loc, distance))
        self.adj_list[to_loc].append((from_loc, distance))

    def shortest_path(self, start, end):
        dist = {node: float('inf') for node in self.adj_list}
        visited = {node: False for node in self.adj_list}

        dist[start] = 0

        while True:
            current = None
            min_dist = float('inf')

            for node in self.adj_list:
                if not visited[node] and dist[node] < min_dist:
                    min_dist = dist[node]
                    current = node

            if current is None or current == end:
                break

            visited[current] = True

            for neighbor, weight in self.adj_list[current]:
                if not visited[neighbor]:
                    new_dist = dist[current] + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist

        return dist[end]
