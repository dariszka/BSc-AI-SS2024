from typing import Any, Generator, Tuple

from tree_node import TreeNode


class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.
        
        Raises:
            ValueError: root is neither a TreeNode nor None.
        """
        self._root = root
        self._size = 0 if root is None else 1
        self._num_of_comparisons = 0

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """
        if not isinstance(key,int):
            raise ValueError('Key is not an integer')
        
        if self._root is None:
            self._root = TreeNode(key, value)
            self._size += 1
        else:
            self._insert_helper(self._root, key, value)

    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """
        if not isinstance(key,int):
            raise ValueError('Key is not an integer.')

        if self._root:
            found = self._find_helper(self._root, key)

            if not found:
                raise KeyError('Key is not present in the tree.')
            
            return found
        else:
            raise KeyError('Key is not present in the tree (because it\'s empty).')

    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""
        return self._size
        # return len(list(self.inorder())) # would be nicer but slower (i modified the insert functions for the solution above)

    # If users instead call `len(tree)`, this makes it return the same as `tree.size`
    __len__ = size 

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        return self.find(key).value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        if not isinstance(key,int):
            raise ValueError('Key is not an integer.')
    
        if self._root:
            self._root = self._remove_helper(self._root, key)
        else:
            raise KeyError('Key is not present in the tree (because it\'s empty).')
           
    # Hint: The following 3 methods can be implemented recursively, and 
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here: 
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root
        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())
        yield from self._inorder(node)

    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._preorder(node)

    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._postorder(node)

    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]: 
        yield from self._preorder(self._root)

    @property
    def is_valid(self) -> bool:
        """Return if the tree fulfills BST-criteria."""
        if self._root:
            nodes = list(self.inorder())
            i = 0
            while i<len(nodes):
                #each node contains a key
                if not nodes[i].key:
                    return False
                
                #external nodes have no child branches
                if nodes[i].is_external: 
                    if nodes[i].right or nodes[i].left:
                        return False

                if i != len(nodes)-1:
                    #keys in the left sub-tree of a node n are smaller than (or equal to) the key stored in n
                    #keys in the right sub-tree of a node n are greater than the key stored in n
                    # this is the way i figured to check validity of tree that wasn't created by my insert - if it's inorder is malformed, there's something wrong 
                    if nodes[i].key>nodes[i+1].key:
                        return False

                i+=1
            return True     
        else:
            return True      

    def return_max_key(self) -> TreeNode:
        """Return the node with the largest key (None if tree is empty)."""
        if self._root:
            _node = self._root
            while _node.right:
                _node = _node.right
            return _node
        else:
            return None
    
    def return_min_key(self) -> TreeNode:
        """Return the node with the smallest key."""
        if self._root:
            _node = self._root
            while _node.left:
                _node = _node.left
            return _node
        else:
            return None

    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute the number of comparisons needed for
           finding the key both in the list and in the BST.
           Return the numbers of comparisons for both, the list and the BST
        """
        python_list = list(node.key for node in self._preorder(self._root))
        
        node = self.find(key)
        bst_comparisons = node.depth*2+1

        list_comparisons = 0
        for _key in python_list:
            list_comparisons+=1
            if _key == key:
                break

        return list_comparisons, bst_comparisons

    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self._inorder(self._root))})"

    ####################################################
    # Helper Functions
    ####################################################

    def get_root(self):
        return self._root

    def _inorder(self, current_node):
        if current_node:
            yield from self._inorder(current_node.left)
            yield current_node
            yield from self._inorder(current_node.right)

    def _preorder(self, current_node):
        if current_node:
            yield current_node
            yield from self._preorder(current_node.left)
            yield from self._preorder(current_node.right)

    def _postorder(self, current_node):
        if current_node:
            yield from self._postorder(current_node.left)
            yield from self._postorder(current_node.right)
            yield current_node

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)

    # lecture slides p34, adapted
    def _insert_helper(self, current_node, key, value):
            if current_node.key == key:
                raise KeyError('Key is already present in the tree')
            
            if current_node.key < key:
                if current_node.right:
                    self._insert_helper(current_node.right, key, value)
                else:
                    current_node.right = TreeNode(key, value, parent=current_node)
                    self._size += 1
            else:
                if current_node.left:
                    self._insert_helper(current_node.left, key, value)
                else:
                    current_node.left= TreeNode(key, value, parent=current_node)
                    self._size += 1

    # lecture slides p35, adapted
    def _find_helper(self, current_node, key):
        if key > current_node.key:
            if current_node.right:
                return self._find_helper(current_node.right, key)
            else:
                return False
        elif key < current_node.key:
            if current_node.left:
                return self._find_helper(current_node.left, key)
            else:
                return False
        elif key == current_node.key:
            return current_node

    def _remove_helper(self, _node, key):
        """Recursively find and remove the node with the given key."""
        if _node is None:
            raise KeyError('Key is not present in the tree.')

        if key < _node.key:
            _node.left = self._remove_helper(_node.left, key)
        elif key > _node.key:
            _node.right = self._remove_helper(_node.right, key)
        else:
            self._size -=1
            if _node.left and _node.right:
                # case 3
                _new = _node.right
                _new_p = _node

                while _new.left:
                    _new_p = _new
                    _new = _new.left

                if _new_p != _node:
                    _new_p.left = _new.right
                    _new.right = _node.right
                _new.left = _node.left

                if _node.parent:
                    _new.parent = _node.parent
                else:
                    self._root = _new

                return _new
            # case 2
            elif _node.left:
                return _node.left 
            elif _node.right:
                return _node.right
            # case 1
            else:
                return None
        return _node

if __name__ == '__main__':
    tree = BinarySearchTree() 

    def create_bst_from_list(list_):
        bst_solution = BinarySearchTree()
        for k in list_:
            bst_solution.insert(key=k, value=str(k))
        return bst_solution


    arr_list_1 = [5, 18, 1, 8, 14, 16, 13, 3]
    bst = create_bst_from_list(arr_list_1)  

    def print_tree(tree_root):
        if tree_root is not None:
            ret_str = "\n"
            lines, _, _, _ = display_aux(tree_root)
            for line in lines:
                ret_str += line + "\n"
                # print(line)
            return ret_str + "\n"
        else:
            return ""

    def display_aux(cur_node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if cur_node.right is None:
            lines, n, p, x = display_aux(cur_node.left)
            s = '%s' % cur_node.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if cur_node.left is None:
            lines, n, p, x = display_aux(cur_node.right)
            s = '%s' % cur_node.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display_aux(cur_node.left)
        right, m, q, y = display_aux(cur_node.right)
        s = '%s' % cur_node.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    print(bst.__repr__(), '\n')
    print(print_tree(bst._root))
    bst.remove(5)
    print(print_tree(bst._root), 5)
    bst.remove(14)
    print(print_tree(bst._root), 14)
    bst.remove(8)
    print(print_tree(bst._root), 8)
    bst.remove(16)
    print(print_tree(bst._root),16)
    bst.remove(13)
    print(print_tree(bst._root),13)
    bst.remove(1)
    print('bst.remove(1)',print_tree(bst._root))
    bst.remove(18)
    print('bst.remove(18)',print_tree(bst._root))
    bst.remove(3)
    print('bst.remove(3)',print_tree(bst._root))
    print(bst.__repr__(), '\n')

