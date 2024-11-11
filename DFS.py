import time 
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
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
    dfs(tree, 'A')
    fin = time.time()
 
    print("\nTiempo de ejecución: ", fin - inicio)