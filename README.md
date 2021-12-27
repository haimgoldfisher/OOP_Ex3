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

It is important to remember that we have already done most of the planning and implementation in the previous project. Therefore, most of the work will be to intelligently convert the project to Python language. Note that Python has data structures that are similar to the data structures in Java. For example: dictionary instead of hashmap.
A class will be built to represent for us the location(tuple of X,Y,Z) node and edge. Since this task does not require the construction of an Edge class, we can give it up. That is, using a dictionary variable that will hold for each node the dest node to which its edge reaches, as well as the weight of the side, we can represent all the edges in the graph. Because these two classes (location, node + edge) are quite small, we will keep them in the same file that will contain two classes. From there it remains to exercise both the DiGraph and GraphAlgo classes. We will do this by realizing the interfaces GraphInterface, GraphAlgoInterface respectively. Alongside building the classes, we would like to implement two testing classes, one for each class. For the purpose of constructing the comparison document for the previous assignment, an additional class will be constructed. It will produce for us graphs to show the differences between the Java project we did and this Python project.

---------
## 3. UML Diagram:

* We chose to present only the significant functions and methods in the main classes in the project:

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/diagram.png?raw=true" height=500 weight=1000/>
</p>
  
  
---------
## 4. Testing Class:

As required, we will write two test units. The TestDiGraph unit will test the graph methods including location, nodes, edges and MC. Graphs will be built, we will add and remove edges and vertices and then we will ensure that the class works properly. Of course we would like to see that after each operation, the MC value increases as expected. The TestGraphAlgo unit will be performed, but most of the work in it is outside the computer. That is, since we want to verify that the output is correct, we will need to verify this using the algorithmic tools at our disposal. We will check that the desired output is obtained for each of the algorithms. In addition, we would like to see that the auxiliary functions (reverse, isConnected...) are correct as required.

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
| T0         | 4           | 5           | Python         | 2 ms             | 8 ms (0, 3)      |  16 ms           | 3 ms (0, 1, 3)   |

## Random Graphs

| **Graph**  | **# Nodes** | **# Edges**  |  **Language**  | `Load & Save`    | `Shortest Path`   | `Center Point`   | `TPS`                     |
|------------|-------------|--------------|----------------|------------------|-------------------|------------------|---------------------------|
| 100        | 100         | 1,000        | Java           | 253 ms           | 233 ms (0,99)     | 395 ms           | 396 ms  (0,50,99)         |
| 100        | 100         | 1,000        | Python         | 19 ms            | 10 ms (0,99)      | 244 ms           | 30  ms  (0,50,99)         |
| 1,000      | 1,000       | 10,000       | Java           | 312 ms           | 38 ms (0,999)     | 1.970 s          | 2.36 s  (0,500,999)       |
| 1,000      | 1,000       | 10,000       | Python         | 181 ms           | 131 ms (0,999)    | 29.553 s         | 166 ms  (0,500,999)       |
| 10,000     | 10,000      | 100,000      | Java           | 756 ms           | 789 ms (0,9999)   | 9 m 11 s         | OutOfMemoryError          |
| 10,000     | 10,000      | 100,000      | Python         | 477 ms           | 968 ms (0,9999)   | TimeoutException | 1.729 s  (0,5000,9999)    |
| 100,000    | 100,000     | 1,000,000    | Java           | 4.648 s          | 1.821s (0,99999)  | TimeoutException | OutOfMemoryError          |
| 100,000    | 100,000     | 1,000,000    | Python         | 15.102 s         | 13.194s (0,99999) | TimeoutException | 27.053 s  (0,50000,99999) |
| 1,000,000  | 1,000,000   | 10,000,000   | Java           | OutOfMemoryError | 22.542s (0,999999)| TimeoutException | OutOfMemoryError          |
| 1,000,000  | 1,000,000   | 10,000,000   | Python         | 3 m 3.487 s      | 3m 4.5s (0,999999)| TimeoutException | 6m 37s  (0,500000,999999) |

## A very detailed comparative report, including graphs between the two projects can be found on the project's wiki page: https://github.com/haimgoldfisher/OOP_Ex3/wiki/Comparison-report

---------
## 6. How to Download, Run and Use The Project:

Before Running this project, install the above packages:
```
matplotlib Version 3.4.3 (or higher), pandas Version 1.3.4 (or higher).
```

Download the whole project and export it by the above actions:
```
Click Code (Green Button) -> Click Download ZIP -> Choose Extract to Folder in Zip -> Run: Main.py
```

You can add as many nodes and edges as you like and run the algorithms on them.

---------

## 7. Graph Presentations:

## A) A0:

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/A0.png?raw=true" height=300 weight=600/>
</p>

## B) A1:

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/A1.png?raw=true" height=300 weight=600/>
</p>

## C) A2:

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/A2.png?raw=true" height=300 weight=600/>
</p>

## D) A3:

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/A3.png?raw=true" height=300 weight=600/>
</p>

## E) A4:

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/A4.png?raw=true" height=300 weight=600/>
</p>

## F) A5:

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/A5.png?raw=true" height=300 weight=600/>
</p>

## G) T0 (random):

 <p align="center">
<img align="center" src="https://github.com/haimgoldfisher/OOP_Ex3/blob/master/pics/T0.png?raw=true" height=300 weight=600/>
</p>

---------

This project was done by using Python Interpreter: Python 3.8

---------
## 8. Info & Resources:

- Directed Graphs : https://en.wikipedia.org/wiki/Directed_graph
- Connectivity : https://en.wikipedia.org/wiki/Connectivity_(graph_theory)
- DFS Algorithm : https://en.wikipedia.org/wiki/Depth-first_search
- Priority Queue : https://en.wikipedia.org/wiki/Priority_queue
- Dijkstra's Algorithm : https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
- TSP : https://en.wikipedia.org/wiki/Travelling_salesman_problem
- Matplotlib : https://matplotlib.org/
- Pandas: https://pandas.pydata.org/

---------
## 9. Languages & Tools: 

<p align="left">
<a href="https://www.python.org/" title="Python"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/2048px-Python.svg.png" alt="Python" width="40" height="40"/></a>
<a href="https://www.jetbrains.com/pycharm/" title="Pycharm"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png" alt="Pycharm" width="40" height="40"/></a>  
<a href="https://www.json.org/json-en.html" title="JSON"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/JSON_vector_logo.svg/2048px-JSON_vector_logo.svg.png" alt="JSON" width="40" height="40"/></a>
  <a href="https://matplotlib.org/" title="Matplotlib"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Created_with_Matplotlib-logo.svg/2048px-Created_with_Matplotlib-logo.svg.png" alt="Matplotlib" width="40" height="40"/></a>  
<a href="https://pandas.pydata.org/" title="Pandas"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png" alt="Pandas" width="40" height="40"/></a>   

