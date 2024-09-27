from my_list_node import MyListNode


class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    # The following methods have to be implemented.

    def get_value(self, index: int) -> int:
        """Return the value (elem) at position 'index' without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            (int): Retrieved value.

        Raises:
            ValueError: If the passed index is not an int or out of range.
        """

        # https://stackoverflow.com/questions/47291094/is-it-possible-to-obtain-index-value-from-singly-linked-list

        if not isinstance(index, int) or index not in range(0, self.__len__()):
            raise ValueError('The passed index is not an int or is out of range.')

        cur_i=0
        cur=self._head
        while cur:
            if cur_i==index: 
                return cur.elem
            cur=cur.next_node
            cur_i+=1
        return 0

    def search_value(self, val: int) -> int:
        """Return the index of the first occurrence of 'val' in the list.

        Args:
            val (int): Value to be searched.

        Returns:
            (int): Retrieved index.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError('val is not an int')
        
        cur_i=0
        cur=self._head
        while cur:
            if cur.elem==val: 
                return cur_i
            cur=cur.next_node
            cur_i+=1

        return -1
        return 0 # i didn't know if i could get rid of this, if it counts as the skeleton, in any case, it's not being accessed

    def insert(self, val: int) -> None:
        """Add a new node containing 'val' to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError('val is not an int')
        
        new_node = MyListNode(val)

        if self._head is None: # empty list
            self._head = new_node
            self._tail = new_node

        elif self._tail.elem <= val: # insert at end
            cur = self._tail
            self._tail = new_node

            new_node.prev_node = cur
            cur.next_node = new_node
            
        elif self._head.elem >= val: # insert at beginning
            cur = self._head
            self._head = new_node

            cur.prev_node = new_node
            new_node.next_node = cur

        else: # insert somewhere inside the list
            cur=self._head
            while cur: 
                if cur.elem>val: 
                    # same idea as in UE slides, except temp and cur are switched, 
                    # since i'm inserting before the cur value (val needs to be smaller than that of cur)
                    
                    temp = cur.prev_node

                    cur.prev_node = new_node
                    new_node.next_node = cur

                    new_node.prev_node = temp
                    temp.next_node = new_node
                    break
                cur=cur.next_node

        self._size +=1

    def remove_first(self, val: int) -> bool:
        """Remove the first occurrence of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether an element was successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError('val is not an int')
        
        # i changed the temp from UE slides to temp_prev and temp_next to keep it clearer as to what and where the nodes are

        cur=self._head
        while cur:
            if self._head.elem == val: # remove at beginning, i'm checking inside the loop to not get an attribute error, doesn't add much to complexity
                temp_next = cur.next_node
                
                cur.next_node = None
                cur.elem = None
                temp_next.prev_node = None

                self._head = temp_next

                self._size -= 1
                return True

            elif self._tail.elem == val and self._tail.prev_node.elem != val: # remove at end, second part checks if last value isn't repeating, eg [1,2,3,3]
                cur = self._tail
                temp_prev = cur.prev_node
                
                cur.prev_node = None
                cur.elem = None
                temp_prev.next_node = None
                
                self._tail = temp_prev
                
                self._size -= 1
                return True
            
            else: # remove inside
                if cur.elem==val: 
                    temp_next = cur.next_node
                    temp_prev = cur.prev_node

                    temp_next.prev_node = temp_prev
                    temp_prev.next_node = temp_next

                    cur.prev_node = None
                    cur.next_node = None
                    cur.elem = None

                    self._size -= 1
                    return True
            
            cur=cur.next_node

        return False 

    def remove_all(self, val: int) -> bool:
        """Remove all occurrences of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether elements were successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError('val is not an int')
        
        cur=self._head
        removed = 0
        while cur:
            # https://stackoverflow.com/questions/71859072/how-to-remove-in-a-doubly-linked-list-python
            # used this idea, but with cur clean up like in slides
            nxt = cur.next_node

            if cur.elem == val:
                temp_next = cur.next_node
                temp_prev = cur.prev_node

                if temp_prev:
                    temp_prev.next_node = temp_next
                else:
                    self._head = temp_next

                if temp_next:
                    temp_next.prev_node = temp_prev
                else:
                    self._tail = temp_prev

                cur.prev_node = None
                cur.next_node = None
                cur.elem = None

                removed += 1

            cur = nxt 

        if removed>0:
            self._size -= removed
            return True
        return False

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        
        cur=self._head
        removed = 0
        unique = []


        while cur:
            nxt = cur.next_node

            if cur.elem in unique:
                temp_next = cur.next_node
                temp_prev = cur.prev_node

                if temp_prev:
                    temp_prev.next_node = temp_next
                else:
                    self._head = temp_next

                if temp_next:
                    temp_next.prev_node = temp_prev
                else:
                    self._tail = temp_prev

                cur.prev_node = None
                cur.next_node = None
                cur.elem = None

                removed += 1
            else:
                unique.append(cur.elem)

            cur = nxt 

        self._size -= removed

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the 'n' highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            ValueError: If the passed value n is not an int or out of range.
        """
        if not isinstance(n, int) or n not in range(1, self.__len__()+1):
            raise ValueError('The passed value n is not an int or is out of range.')

        cur_i=0 
        cur=self._head
        removed = 0
        wanted_i = self._size - n

        while cur:
            nxt = cur.next_node
            if cur_i < wanted_i:
                self._head = cur.next_node
                cur.prev_node = None
                cur.next_node = None
                cur.elem = None

                removed +=1
            elif cur_i == wanted_i: 
                cur.prev_node = None
                break

            cur=nxt
            cur_i+=1

        self._size -= removed

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        cur=self._head
        removed = 0
        while cur:
            nxt = cur.next_node

            if cur.elem%2 == 0:
                temp_next = cur.next_node
                temp_prev = cur.prev_node

                if temp_prev:
                    temp_prev.next_node = temp_next
                else:
                    self._head = temp_next

                if temp_next:
                    temp_next.prev_node = temp_prev
                else:
                    self._tail = temp_prev

                cur.prev_node = None
                cur.next_node = None
                cur.elem = None

                removed += 1

            cur = nxt 

        self._size -= removed

    def filter_even(self) -> None:
        """Filter the list to only contain even values."""
        cur=self._head
        removed = 0
        while cur:
            nxt = cur.next_node

            if cur.elem%2 != 0:
                temp_next = cur.next_node
                temp_prev = cur.prev_node

                if temp_prev:
                    temp_prev.next_node = temp_next
                else:
                    self._head = temp_next

                if temp_next:
                    temp_next.prev_node = temp_prev
                else:
                    self._tail = temp_prev

                cur.prev_node = None
                cur.next_node = None
                cur.elem = None

                removed += 1

            cur = nxt 

        self._size -= removed

