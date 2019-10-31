from Tree import *
Team8 = Team('Chicago Bears',1921)
Team2 = Team('Hurricanes',1997)
Team10 = Team('Chicago cubs',1870)
Team7 = Team('FC Cincinnati',2019)
Team5 = Team('Cleveland Browns',1946)
Team4 = Team('Columbus Blue Jackets',2000)
Team1 = Team('Dallas',1980)
Team3 = Team('Denver Broncos',1960)
Team9 = Team('Detroit Tigers',1901)
Team6 = Team('Houston Texans',2002)

tree = Node(Team1)
tree.insert(Team2)
tree.insert(Team3)
tree.insert(Team4)
tree.insert(Team5)
tree.insert(Team6)
tree.insert(Team7)
tree.insert(Team8)
tree.insert(Team9)
tree.insert(Team10)

# • An inorder traversal
print('in-order traversal:')
print_in_order(tree)
print('.......\n')

# • A postorder traversal
print('post-order traversal:')
print_Postorder(tree)
print ('......\n')

# • A preorder traversal
print('pre-order traversal:')
print_Preorder(tree)
print('.......\n')

# • A breadth-first traversal
print('breadth-first traversal:')
breadth_first_traversal(tree)


