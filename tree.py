import json


class Node:
    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.value = kwargs["value"]
        self.left = kwargs["left"]
        self.right = kwargs["right"]
        self.leftNode = None
        self.rightNode = None


class BinaryTree:
    def __init__(self, data):
        self.nodes = list()
        self.build(data)

    def getNodeFromId(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node

    def build(self, data):
        nodes = data["tree"]["nodes"]
        self.rootId = data["tree"]["root"]
        for node in nodes:
            self.nodes.append(Node(**node))
        for node in self.nodes:
            node.leftNode = self.getNodeFromId(node.left)
            node.rightNode = self.getNodeFromId(node.right)
        self.rootNode = self.getNodeFromId(self.rootId)





def BinaryTreeNodeDepthSum(node, depth=0):
    global Sum
    if not node:
        return 0
    Sum += depth
    BinaryTreeNodeDepthSum(node.leftNode, depth + 1)
    BinaryTreeNodeDepthSum(node.rightNode, depth + 1)
    return Sum


if __name__ == "__main__":
    json_string = row = input("Json:")
    data_dict = json.loads(json_string)

    tree = BinaryTree(data_dict)
    Sum = 0

    sum_of_all_node_depths = BinaryTreeNodeDepthSum(tree.rootNode)
    print("Result - {0}".format(sum_of_all_node_depths))
