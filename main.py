from reader import Reader
execution = True

print('Welcome to BGraph2', end='\n')
print('We will find cycle, sort, count strong connected components'
      '', end='\n')
print('in your digraph and draw it', end='\n')

while execution:
    print('Enter the path to your graph(*.txt)', end='\n')
    path = input()
    while path == '':
        print('Wrong path. Please retry.', end='\n')
        path = input()
    g = Reader.read(path)
    cycle = g.find_cycle()
    sort = g.topological_sort()
    scc = g.strong_connected_comps()
    if cycle:
        print(f"Cycle: {cycle}", end='\n')
    else:
        print(f"Cycle: None", end='\n')
    print(f"Topological sort: {sort}", end='\n')
    print(f"Number of strong connected components: {scc}", end='\n')
    g.draw_graph('your_graph', 'png')
    print("Another graph? Y/N")
    dialog = input()
    if dialog == 'n' or dialog == 'N':
        execution = False