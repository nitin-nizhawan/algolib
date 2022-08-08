from part6_graph.chap22.dfs import dfs

def topological_sort(g):
    result = dfs.DFS(g)
    finish_times  = result.f
    ls = []
    for t in range(0,len(finish_times)):
        finish_time = finish_times[t]
        ls.append((finish_time,g.getVertex(t)))

    ls.sort(reverse = True, key=lambda x : x[0])
    return list(map(lambda x:x[1],ls))







