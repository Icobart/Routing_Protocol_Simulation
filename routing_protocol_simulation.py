import logging

logging.basicConfig(level=logging.INFO)

class Node:
    def __init__(self, name):
        """
        Inizializza un nodo con un nome, una tabella di routing e una lista di vicini.
        :param name: Nome del nodo
        """
        self.name = name
        self.routing_table = {name: 0}  # Distanza da sé stesso è 0
        self.neighbors = {} # Inizializza la lista dei vicini come un dizionario vuoto

    def add_neighbor(self, neighbor, distance):
        """
        Aggiunge un vicino alla lista dei vicini del nodo e aggiorna la tabella di routing.
        :param neighbor: Nodo vicino
        :param distance: Distanza dal nodo vicino
        """
        if distance < 0:
            raise ValueError("La distanza non può essere negativa")
        self.neighbors[neighbor] = distance # Aggiunge il vicino alla lista dei vicini
        self.routing_table[neighbor.name] = distance # Aggiorna la tabella di routing con la distanza dal vicino

    def update_routing_table(self):
        """
        Aggiorna la tabella di routing del nodo in base alle informazioni ricevute dai vicini.
        """
        updated = False # Inizializza una variabile per tracciare se la tabella di routing è stata aggiornata
        for neighbor, distance in self.neighbors.items():  # Itera sui vicini e le loro distanze
            for dest, dist in neighbor.routing_table.items(): # Itera sulle destinazioni e le distanze nella tabella di routing del vicino
                if dest != self.name: # Split horizon: non aggiornare la tabella di routing con rotte apprese dallo stesso vicino
                    new_distance = distance + dist # Calcola la nuova distanza
                    if dest not in self.routing_table or self.routing_table[dest] > new_distance: 
                        self.routing_table[dest] = new_distance # Aggiorna la tabella di routing se la nuova distanza è minore di quella attuale
                        updated = True # Imposta la variabile di aggiornamento su True in questo caso
        return updated # Restituisce True se la tabella di routing è stata aggiornata, altrimenti False

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
node_D = Node('D')
node_E = Node('E')
node_F = Node('F')

# Aggiungere i vicini
node_A.add_neighbor(node_B, 1)
node_B.add_neighbor(node_A, 1)
node_B.add_neighbor(node_C, 2)
node_C.add_neighbor(node_B, 2)
node_C.add_neighbor(node_D, 1)
node_D.add_neighbor(node_C, 1)
node_D.add_neighbor(node_E, 3)
node_E.add_neighbor(node_D, 3)
node_E.add_neighbor(node_F, 2)
node_F.add_neighbor(node_E, 2)

nodes = [node_A, node_B, node_C, node_D, node_E, node_F]
converged = False # Inizializza una variabile per tracciare la convergenza
iteration = 0 # Inizializza il contatore delle iterazioni
max_iterations = 100  # Limite massimo di iterazioni per evitare loop infiniti

# Aggiornare le tabelle di routing
while not converged and iteration < max_iterations:
    logging.info(f"Iteration {iteration}: Checking for convergence")
    converged = True
    for node in nodes:
        if node.update_routing_table():
            converged = False
    iteration += 1

if iteration == max_iterations:
    logging.warning("Reached the maximum iteration limit. There might be a loop in the network.")

# Stampare le tabelle di routing
for node in nodes:
    node.print_routing_table()