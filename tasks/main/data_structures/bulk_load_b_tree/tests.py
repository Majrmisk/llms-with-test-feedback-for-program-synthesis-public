from typing import Optional, List
from generated_function import bulk_load_b_tree

class BTreeNode:
    def __init__(self, t: int, leaf: bool):
        self.t = t
        self.leaf = leaf
        self.keys: List[int] = []
        self.children: List['BTreeNode'] = []

class BTree:
    def __init__(self, t: int):
        self.t = t
        self.root: Optional[BTreeNode] = None

def inorder_btree(node: Optional[BTreeNode]) -> List[int]:
    if node is None:
        return []
    if node.leaf:
        return node.keys[:]
    result = []
    for child in node.children:
        result.extend(inorder_btree(child))
    return result

def check_key_count(node: BTreeNode, t: int, is_root=False):
    if not is_root:
        assert t - 1 <= len(node.keys) <= 2 * t - 1
    if not node.leaf:
        for child in node.children:
            check_key_count(child, t, False)

def collect_leaf_levels(node: Optional[BTreeNode], level: int, levels: List[int]):
    if node is None:
        return
    if node.leaf:
        levels.append(level)
    else:
        for child in node.children:
            collect_leaf_levels(child, level + 1, levels)

def test_empty_tree():
    tree = bulk_load_b_tree([], 2)
    assert tree.root is None

def test_single_node():
    tree = bulk_load_b_tree([15], 2)
    assert tree.root is not None
    assert tree.root.leaf
    assert tree.root.keys == [15]

def test_bulk_load_one_node():
    elements = [10, 20, 30]
    tree = bulk_load_b_tree(elements, 2)
    assert tree.root is not None
    assert tree.root.leaf
    assert tree.root.keys == elements
    assert tree.root.children == []

def test_bulk_load_multiple_levels():
    elements = list(range(1, 21))
    t = 2
    tree = bulk_load_b_tree(elements, t)
    assert inorder_btree(tree.root) == elements
    if tree.root is not None and not tree.root.leaf:
        for child in tree.root.children:
            check_key_count(child, t, False)
    levels = []
    collect_leaf_levels(tree.root, 0, levels)
    assert len(set(levels)) == 1

def test_bulk_load_different_t():
    elements = list(range(1, 16))
    t = 3
    tree = bulk_load_b_tree(elements, t)
    assert inorder_btree(tree.root) == elements
    if tree.root is not None and not tree.root.leaf:
        for child in tree.root.children:
            check_key_count(child, t, False)
    levels = []
    collect_leaf_levels(tree.root, 0, levels)
    assert len(set(levels)) == 1

def test_bulk_load_large_tree():
    elements = list(range(1, 101))
    t = 3
    tree = bulk_load_b_tree(elements, t)
    assert inorder_btree(tree.root) == elements
    if tree.root is not None and not tree.root.leaf:
        for child in tree.root.children:
            check_key_count(child, t, False)
    levels = []
    collect_leaf_levels(tree.root, 0, levels)
    assert len(set(levels)) == 1

def test_bulk_load_different_t_larger():
    elements = list(range(1, 31))
    t = 4
    tree = bulk_load_b_tree(elements, t)
    assert inorder_btree(tree.root) == elements
    if tree.root is not None and not tree.root.leaf:
        for child in tree.root.children:
            check_key_count(child, t, False)
    levels = []
    collect_leaf_levels(tree.root, 0, levels)
    assert len(set(levels)) == 1
