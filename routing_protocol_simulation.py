class Node:
    def __init__(self, name):
        """
        Inizializza un nodo con un nome, una tabella di routing e una lista di vicini.
        :param name: Nome del nodo
        """
        self.name = name
        self.routing_table = {name: 0}  # Distanza a sé stesso è 0
        self.neighbors = {}

    def add_neighbor(self, neighbor, distance):
        """
        Aggiunge un vicino alla lista dei vicini del nodo e aggiorna la tabella di routing.
        :param neighbor: Nodo vicino
        :param distance: Distanza al nodo vicino
        """
        self.neighbors[neighbor] = distance
        self.routing_table[neighbor.name] = distance

    def update_routing_table(self):
        """
        Aggiorna la tabella di routing del nodo in base alle informazioni ricevute dai vicini.
        """
        for neighbor, distance in self.neighbors.items():
            for dest, dist in neighbor.routing_table.items():
                if dest not in self.routing_table or self.routing_table[dest] > distance + dist:
                    self.routing_table[dest] = distance + dist

    def print_routing_table(self):
        """
        Stampa la tabella di routing del nodo.
        """
        print(f"Routing Table for {self.name}:")
        for dest, dist in self.routing_table.items():
            print(f"Destination: {dest}, Distance: {dist}")
        print()

# Creare i nodi
node_A = Node('A')
node_B = Node('B')
node_C = Node('C')

# Aggiungere i vicini
node_A.add_neighbor(node_B, 1)
node_B.add_neighbor(node_A, 1)
node_B.add_neighbor(node_C, 2)
node_C.add_neighbor(node_B, 2)

# Aggiornare le tabelle di routing
for _ in range(3):  # Eseguire più iterazioni per garantire la convergenza
    node_A.update_routing_table()
    node_B.update_routing_table()
    node_C.update_routing_table()

# Stampare le tabelle di routing
node_A.print_routing_table()
node_B.print_routing_table()
node_C.print_routing_table()