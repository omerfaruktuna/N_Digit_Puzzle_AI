from n_digit_puzzle import Node_Graph


def UniformCostSearch(start_state, dim):
    visited = []

    initial_node = Node_Graph(start_state, None, 0, dim, None)
    visited.append(initial_node.state)

    if initial_node.is_success() == True:
        return initial_node.show_path()

    fifo_list = []
    fifo_list.append(initial_node)

    while len(fifo_list) != 0:
        dummy_list = [i.cost for i in fifo_list]
        minpos = dummy_list.index(min(dummy_list))

        actual_node = fifo_list.pop(minpos)
        sub_nodes = actual_node.create_sub_node()
        for sub_node in sub_nodes:
            if sub_node.state not in visited:
                visited.append(sub_node.state)
                if sub_node.is_success() == True:
                    print("Success! Converged to {}".format(sub_node.state))
                    return sub_node.show_path()
                fifo_list.append(sub_node)
    return

