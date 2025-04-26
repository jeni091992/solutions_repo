## Problem 1

### Equivalent Resistance Using Graph Theory

---

#### 1. Introduction to Graph Theory for Circuits

- **Circuit Representation as a Graph:**  
  A circuit can be represented as a graph, where:
  - **Nodes** represent the junctions (connection points between resistors),
  - **Edges** represent resistors with weights equal to their resistance values.
  
  This graph-based approach allows for the use of graph theory algorithms to simplify and analyze complex electrical circuits.

- **Goal:**  
  The goal is to calculate the equivalent resistance of a circuit by iteratively simplifying series and parallel resistor connections. This approach eliminates the need for manual identification of series and parallel connections and reduces the circuit to a single equivalent resistance.

---

#### 2. Algorithm Description

- **Identifying Series and Parallel Connections:**
  - **Series Connection:**  
    Resistors are in series if they are connected end-to-end with no intermediate junction. The equivalent resistance \( R_{\text{eq}} \) for two resistors \( R_1 \) and \( R_2 \) in series is:
    \[
    R_{\text{eq}} = R_1 + R_2
    \]
  - **Parallel Connection:**  
    Resistors are in parallel if they share both ends at the same junction. The equivalent resistance \( R_{\text{eq}} \) for two resistors \( R_1 \) and \( R_2 \) in parallel is:
    \[
    \frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2}
    \]
    or equivalently:
    \[
    R_{\text{eq}} = \frac{R_1 \cdot R_2}{R_1 + R_2}
    \]

- **Iterative Graph Reduction:**
  - The circuit is iteratively simplified by detecting series and parallel connections.
  - After identifying and simplifying a connection, the new equivalent resistor is added back to the graph.
  - This process repeats until only one equivalent resistance remains.

- **Handling Nested Configurations:**
  - For circuits with nested series and parallel connections, the algorithm applies the reduction rules recursively. If a combination of resistors is simplified into a single equivalent resistor, this newly formed resistor might itself be part of a more complex combination, requiring further simplification.

---

#### 3. Pseudocode

```python
def calculate_equivalent_resistance(circuit_graph):
    # Step 1: Simplify series connections
    while series_connections_exist(circuit_graph):
        simplify_series(circuit_graph)

    # Step 2: Simplify parallel connections
    while parallel_connections_exist(circuit_graph):
        simplify_parallel(circuit_graph)

    # Step 3: Return the final equivalent resistance
    return circuit_graph[0]  # Assuming only one node remains, holding the final equivalent resistance

def series_connections_exist(circuit_graph):
    # Check if there are any series connections
    for node in circuit_graph:
        if is_series_connection(node):
            return True
    return False

def parallel_connections_exist(circuit_graph):
    # Check if there are any parallel connections
    for node in circuit_graph:
        if is_parallel_connection(node):
            return True
    return False

def simplify_series(circuit_graph):
    # Find two resistors in series and combine them
    node = find_series_nodes(circuit_graph)
    combined_resistance = node[0].resistance + node[1].resistance
    remove_resistors(circuit_graph, node)
    add_combined_resistor(circuit_graph, node, combined_resistance)

def simplify_parallel(circuit_graph):
    # Find two resistors in parallel and combine them
    node = find_parallel_nodes(circuit_graph)
    combined_resistance = (node[0].resistance * node[1].resistance) / (node[0].resistance + node[1].resistance)
    remove_resistors(circuit_graph, node)
    add_combined_resistor(circuit_graph, node, combined_resistance)

def is_series_connection(node):
    # Check if two resistors are in series
    return node.has_series_neighbors()

def is_parallel_connection(node):
    # Check if two resistors are in parallel
    return node.has_parallel_neighbors()

def find_series_nodes(circuit_graph):
    # Identify and return two nodes connected in series
    pass

def find_parallel_nodes(circuit_graph):
    # Identify and return two nodes connected in parallel
    pass

def remove_resistors(circuit_graph, nodes):
    # Remove the identified resistors from the graph
    pass

def add_combined_resistor(circuit_graph, nodes, resistance):
    # Add the new combined resistor to the graph
    pass
