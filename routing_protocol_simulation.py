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

    def print_routing_table(self):
        """
        Stampa la tabella di routing del nodo.
        """
        print(f"Routing Table for {self.name}:")
        for dest, dist in self.routing_table.items():
            print(f"Destination: {dest}, Distance: {dist}")
        print()