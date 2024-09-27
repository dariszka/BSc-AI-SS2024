from typing import Optional


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = len(self.heap)

    def get_size(self) -> int:
        """
        @return number of elements in the min heap
        """
        return self.size

    def is_empty(self) -> bool:
        """
        @return True if the min heap is empty, False otherwise
        """
        return True if self.size == 0 else False

    def insert(self, integer_val: int) -> None:
        """
        inserts integer_val into the min heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None or not an int
        """
        if integer_val is None or not isinstance(integer_val, int):
            raise ValueError
        
        self.heap.append(integer_val)
        self.size += 1
        self.up_heap(self.size-1)

    def get_min(self) -> Optional[int]:
        """
        returns the value of the minimum element of the PQ without removing it
        @return the minimum value of the PQ or None if no element exists
        """
        if self.is_empty():
            return None
        else:
            return self.heap[0]

    def remove_min(self) -> Optional[int]:
        """
        removes the minimum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        if self.is_empty():
            return None
        else:
            old_min =  self.heap[0]

            self.heap[0] = self.heap[-1] 
            del self.heap[-1]

            self.size -= 1
            self.down_heap(0)

            return old_min

    ### auxiliary methods ###

    def up_heap(self, index):
        current_i = index
        parent_i = self.parent(current_i)

        while parent_i is not None:
            if self.heap[parent_i] > self.heap[current_i]:
                self.swap(parent_i, current_i)
                
                current_i = parent_i
                parent_i = self.parent(current_i)
            else:
                break

    def down_heap(self, index):
        current_i = index
        left_child_i = self.left_child(current_i)
        right_child_i = self.right_child(current_i)

        while left_child_i is not None or right_child_i is not None:
            smallest_child_i = self.get_smallest_child(left_child_i, right_child_i)

            if self.heap[smallest_child_i] < self.heap[current_i]:
                self.swap(smallest_child_i, current_i)
                
                current_i = smallest_child_i
                left_child_i = self.left_child(current_i)
                right_child_i = self.right_child(current_i)
            else:
                break

    def get_smallest_child(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return left if self.heap[left] < self.heap[right] else right
        
    def parent(self, index):
        # https://cs.stackexchange.com/questions/130167/why-does-the-formula-floori-1-2-find-the-parent-node-in-a-binary-heap
        i = (index - 1)//2
        return i if i>=0 else None

    def left_child(self, index):
        i = 2*index + 1 
        return i if i < self.size else None

    def right_child(self, index):
        i = 2*index + 2
        return i if i < self.size else None

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
