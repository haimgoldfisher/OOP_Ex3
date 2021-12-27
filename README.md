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

* In every algo running, we firstly load it and then run the algo. That is, included within each algorithm is also a runtime load function. 
* In TPS, we took 3 cities: first the first node, second is the middle node and third is the last node. In addition, the time of bulding the list of the cities is also included in the running time.
* In Shortest Path, the source is the first node and the destination is the last node. In Java we only return the list of the path, because the distance has a whole other function and it won't be fair the use both functions (path + dist).
* Computer Info: Processor - Intel(R) Core(TM) i5 -1035G1 CPU @ 1.00GHz 1.19 GHz, RAM - 20.0 GB (19.8 GB usable) 


| **Graph**  | **# Nodes** | **# Edges** |  **Language**  | `Load & Save`    | `Shortest Path`  | `Center Point`   | `TPS`            |
|------------|-------------|-------------|----------------|------------------|------------------|------------------|------------------|
| A0         | 11          | 22          | Java           | 190 ms           | 154 ms (0,10)    |  192 ms          | 164 ms  (0,5,10) |
| A0         | 11          | 22          | Python         | 5 ms             | 10 ms  (0,10)    |  6 ms            | 3 ms    (0,5,10) |
| A1         | 17          | 36          | Java           | 171 ms           | 163 ms (0,16)    |  172 ms          | 186 ms  (0,8,16) |
| A1         | 17          | 36          | Python         | 10 ms            | 8 ms   (0,16)    |  9 ms            | 4 ms    (0,8,16) |
| A2         | 31          | 80          | Java           | 213 ms           | 192 ms (0,30)    |  173 ms          | 180 ms (0,15,30) |
| A2         | 31          | 80          | Python         | 6 ms             | 10 ms  (0,30)    |  12 ms           | 10 ms  (0,15,30) |
| A3         | 49          | 136         | Java           | 265 ms           | 193 ms (0,48)    |  285 ms          | 236 ms (0,24,48) |
| A3         | 49          | 136         | Python         | 10 ms            | 4 ms   (0,48)    |  30 ms           | 5 ms   (0,24,48) |
| A4         | 40          | 102         | Java           | 223 ms           | 172 ms (0,39)    |  251 ms          | 266 ms (0,20,39) |
| A4         | 40          | 102         | Python         | 6 ms             | 4 ms   (0,39)    |  18 ms           | 6 ms   (0,20,39  |
| A5         | 48          | 166         | Java           | 254 ms           | 179 ms (0,47)    |  225 ms          | 202 ms (0,24,47) |
| A5         | 48          | 166         | Python         | 9 ms             | 2 ms   (0,47)    |  25 ms           | 10 ms  (0,24,47) |
| T0         | 4           | 5           | Java           | FAILED           | FAILED           | FAILED           | FAILED           |
| T0         | 4           | 5           | Python         |                  |                  |                  |                  |

## Random Graphs

| **Graph**  | **# Nodes** | **# Edges**  |  **Language**  | `Load & Save`    | `Shortest Path`   | `Center Point`   | `TPS`                     |
|------------|-------------|--------------|----------------|------------------|-------------------|------------------|---------------------------|
| 100        | 100         | 1,000        | Java           |                  | ___ ms (0,99)     |                  | ___ ms  (0,50,99)         |
| 100        | 100         | 1,000        | Python         | 19 ms            | ___ ms (0,99)     |                  | ___ ms  (0,50,99)         |
| 1,000      | 1,000       | 10,000       | Java           |                  | ___ ms (0,999)    |                  | ___ ms  (0,500,999)       |
| 1,000      | 1,000       | 10,000       | Python         | 181 ms           | ___ ms (0,999)    |                  | ___ ms  (0,500,999)       |
| 10,000     | 10,000      | 100,000      | Java           |                  | ___ ms (0,9999)   |                  | ___ ms  (0,5000,9999)     |
| 10,000     | 10,000      | 100,000      | Python         | 477 ms           | ___ ms (0,9999)   |                  | ___ ms  (0,5000,9999)     |
| 100,000    | 100,000     | 1,000,000    | Java           |                  | ___ ms (0,99999)  |                  | ___ ms  (0,50000,99999)   |
| 100,000    | 100,000     | 1,000,000    | Python         | 15.102 s         | ___ ms (0,99999)  |                  | ___ ms  (0,50000,99999)   |
| 1,000,000  | 1,000,000   | 10,000,000   | Java           |                  | ___ ms (0,999999) |                  | ___ ms  (0,500000,999999) |
| 1,000,000  | 1,000,000   | 10,000,000   | Python         | 3 m 3.487 s      | ___ ms (0,999999) |                  | ___ ms  (0,500000,999999) |


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

