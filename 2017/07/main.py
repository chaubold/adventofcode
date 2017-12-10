import networkx as nx

g = nx.DiGraph()

with open('input.txt', 'r') as f:
    lines = f.readlines()

progs = [] # list of dicts with {'name': str, 'weight': int, 'below':[list of str]}
for l in lines:
    ws = l.strip().split(' ')
    name = ws[0]
    weight = int(ws[1][1:-1])
    below = []
    if len(ws) > 3:
        below = [w.replace(',','') for w in ws[3:]]

    progs.append({'name':name, 'weight':weight, 'below':below})

# print(progs)
for p in progs:
    g.add_node(p['name'], weight=p['weight'])

for p in progs:
    for u in p['below']:
        g.add_edge(p['name'], u)

root = None
for n in g.nodes_iter():
    if g.in_degree(n) == 0:
        print(n)
        root = n
        break

# --- part 2 ---
edgesToProcess = list(reversed(list(nx.bfs_edges(g, root))))
edgesToProcess.append((root, root))

for ed in edgesToProcess:
    n = ed[1]
    weightList = []
    nameList = []
    for e in g.out_edges(n):
        nameList.append(e[1])
        weightList.append(g.node[e[1]]['accumWeight'])

    weightSet = set(weightList)
    if len(weightSet) > 1:
        print(f"at node {n} we have INSTABLE config {weightList} of nodes {nameList}")
    # else:
    #     print(f"at node {n} we have stable config {weightList} of nodes {nameList}")

    accumWeight = sum(weightList) + g.node[n]['weight']
    g.node[n]['accumWeight'] = accumWeight

for e in g.out_edges('cumah'):
    print(g.node[e[1]])