from n_digit_puzzle import Node_Graph


def DepthFirstSearch(start_state, dim):
    visited = []

    initial_node = Node_Graph(start_state, None, 0, dim, None)
    visited.append(initial_node.state)

    if initial_node.is_success() == True:
        return initial_node.show_path()

    lifo_list = []
    lifo_list.append(initial_node)

    while len(lifo_list) != 0:
        actual_node = lifo_list.pop(-1)
        visited.append(actual_node.state)
        sub_nodes = actual_node.create_sub_node()
        for sub_node in sub_nodes:
            if sub_node.state not in visited:
                if sub_node.is_success() == True:
                    print("Success! Converged to {}".format(sub_node.state))
                    return sub_node.show_path()
                lifo_list.append(sub_node)
    return

