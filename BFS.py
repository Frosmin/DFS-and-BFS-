import time
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return visited

if __name__ == "__main__":
    tree = {
        'A': ['B', 'C', 'D', 'E', 'F'],
        'B': ['G', 'H', 'I'],
        'C': ['J', 'K'],
        'D': ['L', 'M', 'N'],
        'E': ['O', 'P', 'Q'],
        'F': ['R', 'S'],
        'G': ['T', 'U'],
        'H': ['V'],
        'I': ['W', 'X', 'Y'],
        'J': ['Z', 'AA'],
        'K': ['AB'],
        'L': ['AC', 'AD', 'AE'],
        'M': ['AF', 'AG'],
        'N': ['AH'],
        'O': ['AI', 'AJ'],
        'P': ['AK', 'AL'],
        'Q': ['AM'],
        'R': ['AN', 'AO'],
        'S': ['AP'],
        'T': [],
        'U': ['AQ'],
        'V': ['AR'],
        'W': ['AS'],
        'X': ['AT', 'AU'],
        'Y': [],
        'Z': ['AV'],
        'AA': ['AW', 'AX'],
        'AB': [],
        'AC': [],
        'AD': [],
        'AE': ['AY', 'AZ'],
        'AF': [],
        'AG': [],
        'AH': [],
        'AI': [],
        'AJ': ['BA', 'BB'],
        'AK': [],
        'AL': ['BC'],
        'AM': [],
        'AN': [],
        'AO': ['BD', 'BE'],
        'AP': [],
        'AQ': [],
        'AR': [],
        'AS': [],
        'AT': [],
        'AU': ['BF'],
        'AV': [],
        'AW': [],
        'AX': [],
        'AY': [],
        'AZ': [],
        'BA': [],
        'BB': [],
        'BC': [],
        'BD': [],
        'BE': [],
        'BF': []
    }

    inicio = time.time()
    bfs(tree, 'A')
    fin = time.time()

    print("\nTiempo de ejecución: ", fin - inicio)