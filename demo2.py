from jagwa import dot_graph
# cycle graph demo
nodes = {}
edges = set()

k = 8

for i in xrange(k):
    nodes[i] = {'shape': 'point'}
    edges.add((i, (i+1)%k))

print dot_graph(nodes, edges)
