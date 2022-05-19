# class Node:
#     # A utility function to create a new node
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None


# root = Node('A')
# root.left = Node('B')
# root.right = Node('C')
# root.left.left = Node('D')
# root.left.right = Node('E')
# root.right.left = Node('F')
# root.right.right = Node('G')


# from collections import defaultdict
# levels = defaultdict(lambda:[])


# def DFSUtil(root, level=0):
#     if root:
#         levels[level].append(root.data)

#         if root.left:
#             DFSUtil(root.left,level+1)
#         if root.right:
#             DFSUtil(root.right,level+1)


class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.left = Node('F')
root.right.right = Node('G')


from collections import defaultdict
levels = defaultdict(lambda:[])


def DFSUtil(root, level=0):
    if root:
        levels[level].append(root.data)

        if root.left:
            DFSUtil(root.left,level+1)
        if root.right:
            DFSUtil(root.right,level+1)

DFSUtil(root)
print(levels)