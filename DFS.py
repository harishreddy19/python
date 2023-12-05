def DFS(node,visited,graph):
    if node not in graph :
        print("Given node not present in the graph")
        return                       
    if node not in visited :
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
graph = {
    '0' : ['1','2'],
    '1' : ['0','3','4'],
    '2' : ['0'],
    '3' : ['1'],
    '4' : ['2','3']
}
visited = set()
DFS('3',visited,graph)