from n_digit_puzzle import Node_Graph


def BreadthFirstSearch(start_state, dim):


    initial_node = Node_Graph(start_state, None, 0, dim, None)

    visited = []
    visited.append(initial_node.state)

    if initial_node.is_success() == True:
        return initial_node.show_path()

    fifo_list = []
    fifo_list.append(initial_node)

    while len(fifo_list) != 0:
        actual_node = fifo_list.pop(0)
        sub_nodes = actual_node.create_sub_node()
        for sub_node in sub_nodes:
            if sub_node.state not in visited:
                visited.append(sub_node.state)
                if sub_node.is_success() == True:
                    print("Success! Converged to {}".format(sub_node.state))
                    return sub_node.show_path()
                fifo_list.append(sub_node)
    return

