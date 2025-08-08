from typing import Optional, List
from generated_function import balance_bst_dsw

class BSTNode:
    def __init__(self, key: int):
        self.key = key
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None

class BinarySearchTree:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def insert(self, key: int) -> None:
        def _insert(node: Optional[BSTNode], key: int) -> BSTNode:
            if node is None:
                return BSTNode(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            else:
                node.right = _insert(node.right, key)
            return node
        self.root = _insert(self.root, key)

    def inorder_traversal(self) -> List[int]:
        result: List[int] = []
        def traverse(node: Optional[BSTNode]) -> None:
            if not node:
                return
            traverse(node.left)
            result.append(node.key)
            traverse(node.right)
        traverse(self.root)
        return result

def compute_height(node):
    if node is None:
        return 0
    return 1 + max(compute_height(node.left), compute_height(node.right))

def is_balanced(node):
    if node is None:
        return True
    left_height = compute_height(node.left)
    right_height = compute_height(node.right)
    if abs(left_height - right_height) > 1:
        return False
    return is_balanced(node.left) and is_balanced(node.right)

def test_empty_tree():
    bst = BinarySearchTree()
    balanced_bst = balance_bst_dsw(bst)
    assert balanced_bst.inorder_traversal() == []

def test_single_node():
    bst = BinarySearchTree()
    bst.insert(10)
    balanced_bst = balance_bst_dsw(bst)
    assert balanced_bst.inorder_traversal() == [10]

def test_sorted_insertion():
    bst = BinarySearchTree()
    values = list(range(1, 11))
    for val in values:
        bst.insert(val)
    balanced_bst = balance_bst_dsw(bst)
    assert balanced_bst.inorder_traversal() == values
    assert is_balanced(balanced_bst.root)

def test_random_insertion():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    balanced_bst = balance_bst_dsw(bst)
    assert balanced_bst.inorder_traversal() == sorted(values)
    assert is_balanced(balanced_bst.root)

def test_already_balanced_tree():
    bst = BinarySearchTree()
    values = [40, 20, 60, 10, 30, 50, 70]
    for val in values:
        bst.insert(val)
    balanced_bst = balance_bst_dsw(bst)
    assert balanced_bst.inorder_traversal() == sorted(values)
    assert is_balanced(balanced_bst.root)

def test_large_tree():
    bst = BinarySearchTree()
    values = [50, 20, 70, 10, 30, 60, 80, 5, 15, 25, 35, 55, 65, 75, 85]
    for val in values:
        bst.insert(val)
    balanced_bst = balance_bst_dsw(bst)
    assert balanced_bst.inorder_traversal() == sorted(values)
    assert is_balanced(balanced_bst.root)
