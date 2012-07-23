import doctest
def dot_graph(nodes, edges, multigraph=False):
    """
    Return the graph as a DOT file format string.

    Think of this as a very thin wrapper around the actual DOT output.
    Each 'node' can be an arbitrary (hashable) Python objects.
    Nodes is a dict that maps each 'node' to attribute dicts.
    Edges is an iterable of pairs of 'nodes' (or other collections of size 2).

    If you want the Python object you use as a node to have a nice name
    in the output file for readability, set the attribute 'name'.
    (Note that this is different from the 'label' used in the image.)

    >>> nodes = {'gday': {'shape': 'box', 'name': 'hello', 'label': 'greeting'}}
    >>> edges = [['gday', 'world']]
    >>> print dot_graph(nodes, edges)
    graph G {
        hello [shape=box,label=greeting];
        "'world'" -- hello;
    }
    """

    if not multigraph:
        # remove duplicate edges
        edges = set(map(frozenset, edges))

    lines = ['']
    for node in sorted(nodes.keys()):
        att = nodes[node]
        name = node_name(node, nodes)
        att_str = ','.join("%s=%s" % item for item in att.iteritems() if item[0] != 'name')
        lines.append("%s [%s];" % (name, att_str))

    for edge in edges:
        e = list(edge)
        s = node_name(e[0], nodes)
        t = node_name(e[-1], nodes) # -1 not 1 so it works for loop edges
        lines.append("%s -- %s;" % (s, t))

    return "graph G {%s\n}" % '\n    '.join(lines)

def node_name(node, nodes):
    try:
        return nodes[node]['name']
    except KeyError:
        return "\"%s\"" % repr(node)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
