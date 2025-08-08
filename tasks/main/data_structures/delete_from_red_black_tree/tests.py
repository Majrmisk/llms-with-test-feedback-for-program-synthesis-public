from typing import Optional, List
from generated_function import delete_from_red_black_tree

class RedBlackTreeNode:
    def __init__(self, key: int, color: str):
        self.key = key
        self.color = color
        self.left: Optional['RedBlackTreeNode'] = None
        self.right: Optional['RedBlackTreeNode'] = None
        self.parent: Optional['RedBlackTreeNode'] = None

class RedBlackTree:
    def __init__(self):
        self.root: Optional[RedBlackTreeNode] = None

def inorder_traversal_rbt(node: Optional[RedBlackTreeNode]) -> List[int]:
    result = []
    def traverse(n: Optional[RedBlackTreeNode]):
        if n is None:
            return
        traverse(n.left)
        result.append(n.key)
        traverse(n.right)
    traverse(node)
    return result

def validate_red_black_properties(root: Optional[RedBlackTreeNode]) -> bool:
    if root is None:
        return True
    if root.color != "black":
        return False
    def check_properties(node: Optional[RedBlackTreeNode]) -> int:
        if node is None:
            return 1
        if node.color not in ("red", "black"):
            raise ValueError("Invalid color")
        if node.color == "red":
            if node.left and node.left.color != "black":
                raise ValueError("Red node has red left child")
            if node.right and node.right.color != "black":
                raise ValueError("Red node has red right child")
        left_black = check_properties(node.left)
        right_black = check_properties(node.right)
        if left_black != right_black:
            raise ValueError("Black height mismatch")
        return left_black + (1 if node.color == "black" else 0)
    try:
        check_properties(root)
        return True
    except Exception:
        return False

def test_delete_empty_tree():
    tree = RedBlackTree()
    delete_from_red_black_tree(tree, 10)
    assert tree.root is None

def test_delete_nonexistent_key():
    n10 = RedBlackTreeNode(10, "black")
    n5 = RedBlackTreeNode(5, "red")
    n15 = RedBlackTreeNode(15, "red")
    n10.left = n5
    n10.right = n15
    n5.parent = n10
    n15.parent = n10
    tree = RedBlackTree()
    tree.root = n10
    original_inorder = inorder_traversal_rbt(tree.root)
    delete_from_red_black_tree(tree, 100)
    assert inorder_traversal_rbt(tree.root) == original_inorder
    assert validate_red_black_properties(tree.root)

def test_delete_leaf():
    n10 = RedBlackTreeNode(10, "black")
    n5 = RedBlackTreeNode(5, "red")
    n15 = RedBlackTreeNode(15, "red")
    n10.left = n5
    n10.right = n15
    n5.parent = n10
    n15.parent = n10
    tree = RedBlackTree()
    tree.root = n10
    delete_from_red_black_tree(tree, 5)
    assert inorder_traversal_rbt(tree.root) == [10, 15]
    assert validate_red_black_properties(tree.root)

def test_delete_node_with_one_child():
    n10 = RedBlackTreeNode(10, "black")
    n5 = RedBlackTreeNode(5, "black")
    n15 = RedBlackTreeNode(15, "black")
    n12 = RedBlackTreeNode(12, "red")
    n10.left = n5
    n10.right = n15
    n5.parent = n10
    n15.parent = n10
    n15.left = n12
    n12.parent = n15
    tree = RedBlackTree()
    tree.root = n10
    delete_from_red_black_tree(tree, 15)
    assert inorder_traversal_rbt(tree.root) == [5, 10, 12]
    assert validate_red_black_properties(tree.root)

def test_delete_node_with_two_children():
    n10 = RedBlackTreeNode(10, "black")
    n5 = RedBlackTreeNode(5, "black")
    n15 = RedBlackTreeNode(15, "black")
    n12 = RedBlackTreeNode(12, "red")
    n20 = RedBlackTreeNode(20, "red")
    n10.left = n5
    n10.right = n15
    n5.parent = n10
    n15.parent = n10
    n15.left = n12
    n15.right = n20
    n12.parent = n15
    n20.parent = n15
    tree = RedBlackTree()
    tree.root = n10
    delete_from_red_black_tree(tree, 15)
    assert inorder_traversal_rbt(tree.root) == [5, 10, 12, 20]
    assert validate_red_black_properties(tree.root)
