import sys
import tkinter as tk

class GraphGUI:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.vertices = [(10,200), (100, 50), (100, 350),(250,50),(250,350),(340,200)
        ]

        self.connections = [(0,1),(0,2),(1,3),(3,4),(2,4),(3,5),(4,5)]

        self.values = [3, 4, 7, 8, 11,9,12]

        self.draw_graph()

    def draw_graph(self):
        for i, (start, end) in enumerate(self.connections):
            x1, y1 = self.vertices[start]
            x2, y2 = self.vertices[end]
            self.canvas.create_line(x1, y1, x2, y2,fill="blue" ,width=2)
            self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=str(self.values[i]),fill="black")

        for i, (x, y) in enumerate(self.vertices):
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")
            self.canvas.create_text(x, y - 15, text=f"R{i+1}")


import tkinter as tk
from tkinter import messagebox

class DijkstraGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Link State Routing Algorithm")

        # Predefined graph
        self.graph = {
            'R1': {'R2': 3, 'R3': 4},
            'R2': {'R1': 3, 'R4': 7},
            'R3': {'R1': 4, 'R5': 11},
            'R4': {'R2': 7, 'R5': 8, 'R6': 9},
            'R5': {'R4': 8, 'R3': 11,'R6': 12},
            'R6': {'R4': 9, 'R5': 12}
        }
        
        self.output_button = tk.Button(master, text="Find Shortest Path", command=self.run_dijkstra)
        self.output_button.pack(pady=10)

        self.output_label = tk.Label(master, text="Shortest Path:")
        self.output_label.pack()

        self.output_text = tk.Text(master, height=5, width=50)
        self.output_text.pack()

    def run_dijkstra(self):
        shortest_path = self.dijkstra(self.graph, 'R1')  # Start from node A
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, shortest_path)

    def dijkstra(self, graph, start):
        # Initialization
        unvisited = {node: float('inf') for node in graph}
        visited = {}
        current = start
        current_distance = 0
        unvisited[start] = 0

        while True:
            for neighbor, distance in graph[current].items():
                if neighbor not in unvisited:
                    continue
                new_distance = current_distance + distance
                if new_distance < unvisited[neighbor]:
                    unvisited[neighbor] = new_distance
            visited[current] = current_distance
            del unvisited[current]
            if not unvisited:
                break
            candidates = [node for node in unvisited.items() if node[1]]
            current, current_distance = sorted(candidates, key=lambda x: x[1])[0]

        return visited

def main():
    root = tk.Tk()
    app = DijkstraGUI(root)
    root.mainloop()


        
root = tk.Tk()
root.geometry("700x500")
app = GraphGUI(root)
if __name__ == "__main__":
    main()
root.mainloop()
