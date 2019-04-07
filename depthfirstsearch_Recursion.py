from n_digit_puzzle import Node_Graph

global vstd
vstd = []


def DepthFirstSearch_Recursion(start_state, is_first_time, dim):
    if is_first_time == 0:
        initial_node = Node_Graph(start_state, None, 0, 3, None)
        vstd.append(initial_node)

    if vstd[-1].is_success() == True:
        print(vstd[-1].state)
        print("Found!!!")
        return vstd[-1].show_path()

    else:
        sub_nodes = vstd[-1].create_sub_node()

        for sub_node in sub_nodes:
            if sub_node.state not in vstd:
                vstd.append(sub_node)
                result = DepthFirstSearch_Recursion(sub_node.state, 1, dim)
                if result != "failure":
                    return result
        s = "failure"
        return s
