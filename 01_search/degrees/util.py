# class Node
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


# class StackFrontier
class StackFrontier():
    def __init__(self):
        self.frontier = []

    # add
    def add(self, node):
        self.frontier.append(node)

    # contains_state
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    # emoty
    def empty(self):
        return len(self.frontier) == 0

    # remove
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


# class QueueFrontier
class QueueFrontier(StackFrontier):

    # remove
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node