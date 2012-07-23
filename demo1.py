from jagwa import dot_graph
# cube graph demo
nodes = {}
edges = set()

k = 4
for i in xrange(2 ** k):
    bin_str = ('{:0' + str(k) + 'b}').format(i)
    nodes[i] = {
        'name': bin_str,
        'shape': 'circle',
        'height': '0.4',
        'fixedsize': 'true',
        'fontsize': '8'
    }

for u in nodes:
    for v in nodes:
        # check if they differ at precisely one bit position
        # (warning: crazy bit hacks)
        delta = u ^ v
        if delta and not delta & (delta - 1):
            edges.add((u, v))

print dot_graph(nodes, edges)
