
class MaxHeap:
    def __init__(self, input_array):
        """
        @param input_array from which the heap should be created
        @raises ValueError if list is None.
        Creates a bottom-up max heap in place.
        """
        if input_array is None:
            raise ValueError
        self.size = len(input_array)
        self.heap = self.construct(input_array)

    def get_heap(self):
        # helper function for testing, do not change
        return self.heap

    def get_size(self):
        """
        @return size of the max heap
        """
        return self.size

    def contains(self, val):
        """
        @param val to check if it is contained in the max heap
        @return True if val is contained in the heap else False
        @raises ValueError if val is None.
        Tests if an item (val) is contained in the heap. Does not search the entire array sequentially, but uses the
        properties of a heap.
        """
        if val is None:
            raise ValueError
        
        return self.contains_helper(val, self.heap, 0)
        
    def sort(self):
        """
        This method sorts (ascending) the list in-place using HeapSort, e.g. [1,3,5,7,8,9]
        """
        # https://www.programiz.com/dsa/heap-sort
        n = self.size

        for i in range(n - 1, 0, -1):
            self.swap(self.heap, 0, i)
            self.size -= 1 # not removing the elem, since i still need the heap but im cutting it off the sort, since it's at last indices
            self.down_heap(self.heap,0)

        self.size = n

    def remove_max(self):
        """
        Removes and returns the maximum element of the heap
        @return maximum element of the heap or None if heap is empty
        """
        if self.size == 0:
            return None
        else:
            old_max =  self.heap[0]

            if self.size == 1:
                del self.heap[0]
            else:
                self.heap[0] = self.heap[-1] 
                del self.heap[-1]

            self.size -= 1
            self.down_heap(self.heap, 0)

            return old_max

    ### auxiliary methods ###

    def construct(self, arr):
        n = len(arr)

        # https://www.geeksforgeeks.org/building-heap-from-array/
        first_i = n//2-1
        for i in range(first_i,-1,-1):
            self.down_heap(arr, i)

        return arr

    def up_heap(self, index):
        current_i = index
        parent_i = self.parent(current_i)

        while parent_i is not None:
            if self.heap[parent_i] < self.heap[current_i]:
                self.swap(parent_i, current_i)
                
                current_i = parent_i
                parent_i = self.parent(current_i)
            else:
                break

    def down_heap(self, heap, index):
        current_i = index
        left_child_i = self.left_child(current_i)
        right_child_i = self.right_child(current_i)

        while left_child_i is not None or right_child_i is not None:
            largest_child_i = self.get_largest_child(heap, left_child_i, right_child_i)

            if largest_child_i is None:
                break
            # print(largest_child_i, current_i)

            if heap[largest_child_i] > heap[current_i]:
                self.swap(heap, largest_child_i, current_i)
                
                current_i = largest_child_i
                left_child_i = self.left_child(current_i)
                right_child_i = self.right_child(current_i)
            else:
                break

    def get_largest_child(self, heap, left, right):
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return left if heap[left] > heap[right] else right
        
    def parent(self, index):
        i = (index - 1)//2
        return i if i>=0 else None

    def left_child(self, index):
        i = 2*index + 1
        return i if i < self.size else None

    def right_child(self, index):
        i = 2*index + 2
        return i if i < self.size else None

    def swap(self, heap, index1, index2):
        heap[index1], heap[index2] = heap[index2], heap[index1]
        
    def contains_helper(self, val, heap, index):
        if index is None or index >= len(heap): 
            return False
        
        current_i = index
        left_child_i = self.left_child(current_i)
        right_child_i = self.right_child(current_i)

        if heap[index] == val: 
            return True
        elif heap[index] > val: 
            in_branches = (self.contains_helper(val, heap, left_child_i) or self.contains_helper(val, heap, right_child_i))       
            return in_branches
        else:
            return False       
    
