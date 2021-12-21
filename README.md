# Ex3 - Graphs With Python
### 

<p align="center">
<img align="center" src="https://www.researchgate.net/publication/331679222/figure/fig3/AS:735622553681922@1552397492158/Network-nodes-relationship-diagram-A-network-node-undirected-graph-is-shown-in-figure-3.ppm" />
</p>

### @ Or Yitshak & Haim Goldfisher
---------
## 1. Introduction:

In this task, we would like to convert the graph implementation we did in Java to Python. We will also finally be required to compare the performance of the program we wrote in Java with the performance of the program we will write in Python. This time we got two interfaces that we need to implement:
1. <ins>**GraphInterface**</ins> - Contains the following functions that we must implement:
    * `v_size()` - It returns the amount of nodes in this graph.
    * `e_size()` - It returns the amount of edges in this graph. 
    * `get_all_v()` - It returns a dictionary of all the key_node + nodes in this graph.
    * `all_in_edges_of_node(int)` - It returns a dictionary of all the edges which are directed to the selected vertex.
    * `all_out_edges_of_node(int)` - It returns a dictionary of all the edges coming out of the selected vertex.
    * `get_mc()` - It returns the number of actions which we did on this graph so far.
    * `add_node(int, tuple)` - It adds a new node to this graph.
    * `add_edge(int, int, float)` - It adds a new edge to this graph.
    * `remove_node(int)` - It removes a node from this graph (If it exists).
    * `remove_edge(int, int)` - It removes an edge from this graph (If it exists).
    
2. <ins>**GraphAlgoInterface**</ins> - Contains the following functions that we must implement:
    * `get_graph()` - It returns the graph that the algorithm loaded.
    * `load_from_json(str)` - It loads a new graph from the Json file.
    * `save_to_json(str)` - It saves the graph that works on it into a Json file.
    * `shortest_path(int, int)` - It returns the distance and the path (list) of the shortest path between two vertices.
    *  `TSP(List[int])` - It returns the shortest path that visits all the nodes in the list as a list and the overall distance.
    *  `centerPoint()` - It return the vertex that has the shortest distance to it's farthest node.
    *  `plot_graph()` - It plots the graph. 

---------
## 2. The Thoughts Behind The Classes:


---------
## 3. UML Diagram:

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/diagram.png?raw=true" height=400 weight=800/>
</p>
  
  
---------
## 4. Testing Class:


---------
## 5. Analysis - The Performance of The Algorithms:


| **Graph**  | **# Nodes** | **# Edges** |  **Language**  | `Load & Save`    | `Shortest Path`  | `Center Point`   | `TPS`            |
|------------|-------------|-------------|----------------|------------------|------------------|------------------|------------------|
| A0         | 11          | 22          | Java           |                  |                  |                  |                  |
| A0         | 11          | 22          | Python         |                  |                  |                  |                  |
| A1         | 17          | 36          | Java           |                  |                  |                  |                  |
| A1         | 17          | 36          | Python         |                  |                  |                  |                  |
| A2         | 31          | 80          | Java           |                  |                  |                  |                  |
| A2         | 31          | 80          | Python         |                  |                  |                  |                  |
| A3         | 49          | 136         | Java           |                  |                  |                  |                  |
| A3         | 49          | 136         | Python         |                  |                  |                  |                  |
| A4         | 40          | 102         | Java           |                  |                  |                  |                  |
| A4         | 40          | 102         | Python         |                  |                  |                  |                  |
| A5         | 48          | 166         | Java           |                  |                  |                  |                  |
| A5         | 48          | 166         | Python         |                  |                  |                  |                  |
| T0         | 4           | 5           | Java           |                  |                  |                  |                  |
| T0         | 4           | 5           | Python         |                  |                  |                  |                  |



---------
## 6. How to Download, Run and Use The Graphical Interface:

Download the whole project and export it by the above actions:
```
Click Code (Green Button) -> Click Download ZIP -> Choose Extract to Folder in Zip -> 
```

---------

This project was done by using ...

---------
## 7. Info & Resources:

- Directed Graphs : https://en.wikipedia.org/wiki/Directed_graph
- Connectivity : https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
- DFS Algorithm : https://en.wikipedia.org/wiki/Depth-first_search
- Priority Queue : https://en.wikipedia.org/wiki/Priority_queue
- Dijkstra's Algorithm : https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
- TSP : https://en.wikipedia.org/wiki/Travelling_salesman_problem
- Pygame : https://www.pygame.org/wiki/tutorials
- Matplotlib : https://matplotlib.org/

---------
## 8. Languages & Tools: 

<p align="left">
<a href="https://www.python.org/" title="Python"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/2048px-Python.svg.png" alt="Python" width="40" height="40"/></a>
<a href="https://www.jetbrains.com/pycharm/" title="Pycharm"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png" alt="Pycharm" width="40" height="40"/></a>  
<a href="https://www.json.org/json-en.html" title="JSON"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/JSON_vector_logo.svg/2048px-JSON_vector_logo.svg.png" alt="JSON" width="40" height="40"/></a>
<a href="https://www.pygame.org/news" title="PyGame"> <img src="https://www.pygame.org/ftp/pygame-head-party.png" alt="PyGame" width="40" height="40"/></a>  
  <a href="https://matplotlib.org/" title="Matplotlib"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" alt="Matplotlib" width="40" height="40"/></a>  
<a href="https://pandas.pydata.org/" title="Pandas"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png" alt="Pandas" width="40" height="40"/></a>   

