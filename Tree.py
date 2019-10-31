class Team:
    def __init__(self, team_name, team_year):
        self.team_name = team_name
        self.team_year = team_year


def in_Order(root):
    if root:
        inOrder(root.left)
        print(root.data)
        inOrder(root.right)


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is not None:
            if data.team_year < self.data.team_year:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data.team_year > self.data.team_year:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


def print_info(root):
    print("%s:%d" % (root.data.team_name, root.data.team_year))


def print_in_order(root):
    if root:
        # First recur on left child
        print_in_order(root.left)

        # then print the data of node
        print_info(root)

        # now recur on right child
        print_in_order(root.right)


def print_Postorder(root):
    if root:
        # First recur on left child
        print_Postorder(root.left)

        # the recur on right child
        print_Postorder(root.right)

        # now print the data of node
        print_info(root)


def print_Preorder(root):
    if root:
        # First print the data of node
        print_info(root)

        # Then recur on left child
        print_Preorder(root.left)

        # Finally recur on right child
        print_Preorder(root.right)


def get_height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        l_height = get_height(node.left)
        r_height = get_height(node.right)

        # Use the larger one
        if l_height > r_height:
            return l_height + 1
        else:
            return r_height + 1


def print_current_level(root,level):
    if root is None:
        return
    if level == 1:
        print_info(root)
    elif level > 1:
        print_current_level(root.left,level-1)
        print_current_level(root.right,level-1)


def breadth_first_traversal(root):
    h = get_height(root)
    for i in range(1,h+1):
        print_current_level(root,i)



