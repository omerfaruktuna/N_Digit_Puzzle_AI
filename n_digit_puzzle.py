class Node_Graph():

    def __init__(self, node_state, parent, cost, dimension, move):
        self.dim = dimension
        self.parent = parent
        self.move = move
        self.state = node_state

        if parent is not None:
            self.cost = parent.cost + cost
        else:
            self.cost = cost

        self.target_result = [(i + 1) for i in range((self.dim * self.dim) - 1)]
        self.target_result.append(0)

    def is_success(self):
        if self.state == self.target_result:
            return True
        else:
            return False

    def show_path(self):

        temp = []

        while self.parent is not None:
            temp.append(self.move)
            self = self.parent

        final_path = temp[::-1]
        return final_path

    def decide_moves(self, i, j):

        if i == 0 and j == 0:
            possible_move = ['Down', 'Right']
        elif i == 0 and j == (self.dim - 1):
            possible_move = ['Down', 'Left']
        if i == (self.dim - 1) and j == 0:
            possible_move = ['Up', 'Right']
        elif i == (self.dim - 1) and j == (self.dim - 1):
            possible_move = ['Up', 'Left']
        elif i == 0:
            possible_move = ['Left', 'Down', 'Right']
        elif i == (self.dim - 1):
            possible_move = ['Up', 'Right', 'Left']
        elif j == 0:
            possible_move = ['Up', 'Down', 'Right']
        elif j == (self.dim - 1):
            possible_move = ['Up', 'Down', 'Left']
        else:
            possible_move = ['Up', 'Down', 'Left', 'Right']

        return possible_move

    def create_sub_node(self):
        sub_nodes = []
        pos = self.state.index(0)
        row = pos // self.dim
        col = pos - ((pos // self.dim) * self.dim)

        possible_moves = self.decide_moves(row, col)

        for movee in possible_moves:
            sub_node_state = self.state[:]
            if movee is 'Up':
                temp = sub_node_state[pos]
                sub_node_state[pos] = sub_node_state[pos - self.dim]
                sub_node_state[pos - self.dim] = temp
            elif movee is 'Down':
                temp = sub_node_state[pos]
                sub_node_state[pos] = sub_node_state[pos + self.dim]
                sub_node_state[pos + self.dim] = temp
            elif movee is 'Left':
                temp = sub_node_state[pos]
                sub_node_state[pos] = sub_node_state[pos - 1]
                sub_node_state[pos - 1] = temp
            elif movee is 'Right':
                temp = sub_node_state[pos]
                sub_node_state[pos] = sub_node_state[pos + 1]
                sub_node_state[pos + 1] = temp

            sub_nodes.append(Node_Graph(sub_node_state, self, 1, self.dim, movee))
        return sub_nodes

