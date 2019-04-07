from n_digit_puzzle import Node_Graph

global vstd
vstd = []


def DepthLimitedSearch(start_state, level, limit, is_first_time, dimension):
    if is_first_time == 0:
        initial_node = Node_Graph(start_state, None, 0, dimension, None)
        vstd.append(initial_node)
        level = limit
    x = level
    lmt = limit

    if vstd[-1].is_success() == True:
        print(vstd[-1].state)
        print("Found!!!")
        print("Solution found in {}th level".format(x - lmt))
        return vstd[-1].show_path()
    elif lmt == 0:
        s = "cutoff"
        return s
    else:
        cutoff_occured = False
        sub_nodes = vstd[-1].create_sub_node()
        for sub_node in sub_nodes:
            if sub_node.state not in vstd:
                vstd.append(sub_node)
                result = DepthLimitedSearch(sub_node.state, x, (limit - 1), 1, dimension)
                if result == "cutoff":
                    cutoff_occured = True
                elif result != "failure":
                    return result
        if cutoff_occured:
            s = "cutoff"
            return s
        else:
            s = "failure"
            return s
