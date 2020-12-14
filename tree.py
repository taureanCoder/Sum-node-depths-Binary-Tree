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

    def get_node_from_id(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node

    def build(self, data):
        nodes = data["tree"]["nodes"]
        self.root_id = data["tree"]["root"]
        for node in nodes:
            self.nodes.append(Node(**node))
        for node in self.nodes:
            node.leftNode = self.get_node_from_id(node.left)
            node.rightNode = self.get_node_from_id(node.right)
        self.rootNode = self.get_node_from_id(self.root_id)


def binary_tree_node_depth_sum(node, depth=0):
    global Sum
    if not node:
        return 0
    Sum += depth
    binary_tree_node_depth_sum(node.leftNode, depth + 1)
    binary_tree_node_depth_sum(node.rightNode, depth + 1)
    return Sum


if __name__ == "__main__":
    json_string = input("Json:")
    data_dict = json.loads(json_string)
    tree = BinaryTree(data_dict)
    Sum = 0
    sum_of_all_node_depths = binary_tree_node_depth_sum(tree.rootNode)
    print("Result - {0}".format(sum_of_all_node_depths))
