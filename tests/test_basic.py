import sys
import os

# allow access to src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.city import City


def test_shortest_path():
    city = City()

    city.add_road("A", "B", 5)
    city.add_road("B", "C", 3)
    city.add_road("A", "C", 10)
    city.add_road("C", "D", 2)

    result = city.shortest_path("A", "C")
    print("Shortest distance from A to C:", result)


if __name__ == "__main__":
    test_shortest_path()
