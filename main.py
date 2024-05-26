from maze import *


if __name__ == "__main__":

    type = int(input('Provide the traversal type: 0 for Djkistra | 1 for Stack approach | 2 for Astar version 1 | 3 for Astar version 2:'))
    if type not in [0,1,2,3]:
        print('Invalid option.')
    else:
        while(1):
            maze_type = type//3
            alg_type = type if type < 2 else 2 # 0, 1, 2
            m = MazeBuilder(maze_type=maze_type, width = 1000, height = 500, ncellsx = 50, ncellsy = 25)
            rb = SearchAlgs()
            m.init_maze_environment()

            if not USE_SAVED_MAZE: # we build a new maze
                m.build_maze()
                m.save_graph("amaze.pickle") ### save the graph/maze
            else:
                m.load_graph("amaze.pickle") ### load the last saved graph       
            
            if alg_type == 0:
                m.fill_height_map()
                m.draw_grid_from_graph(width = 3)
                visited, optimal_path = rb.Dijkstra(graph = m.graph, pos_start = m.pos_start, pos_end = m.pos_end)
                m.fill_maze_path(visited, optimal_path)
            elif alg_type == 1:
                graph_traversed = {}
                stack = []
                vis = set()
                for k_i in range(5):                
                    m.draw_grid_from_graph(width = 3)
                    visited, optimal_path, graph_traversed, stack, vis = rb.StackBasedApproach(graph = m.graph, pos_start = m.pos_start, pos_end = m.pos_end, graph_traversed=graph_traversed, pos_stack=stack, first = k_i == 0, visited = vis)
                    m.fill_maze_path(visited, optimal_path)
                    print(f'traversal {k_i+1}')
                    time.sleep(2)
            else:
                m.draw_grid_from_graph(width = 3)
                visited, optimal_path = rb.Astar(graph = m.graph, pos_start = m.pos_start, pos_end = m.pos_end)
                m.fill_maze_path(visited, optimal_path)
            m.run()
