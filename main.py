from Graph import *
import time

from Graph import *
import time

if __name__ == '__main__':
    graph = Graph()
    time1 = time.time()
    graph.make_graph_demo()
    time2 = time.time()

    print("Dijkstra Shortest Path:")
    dijkstra_start = time.time()
    shortest_time, shortest_path = graph.get_shortest_path_dijkstra('A', 'G')
    dijkstra_end = time.time()
    print(f"Shortest time: {shortest_time}")
    print(f"Shortest path: {' -> '.join(shortest_path)}")
    print(f"Dijkstra execution time: {dijkstra_end - dijkstra_start} seconds")

    print("\nContraction Hierarchies Shortest Path:")
    shortest_time, shortest_path = graph.get_shortest_path_CH('A', 'G')
    print(f"Shortest time: {shortest_time}")
    print(f"Shortest path: {' -> '.join(shortest_path)}")

    time3 = time.time()
    print("\nTime making graph: ", time2 - time1)
    print('Total execution time: ', time3 - time1)
