class MinHeap:
 """Array-based implementation of a minimum heap (priority queue)."""
    def __init__(self):
        self.heap_array = []
        self.element_counter = 0

    #helper methods
    def left_child(parent: int) -> int:
        return 2 * parent + 1

    def right_child(parent: int) -> int:
        return 2 * (parent + 1)

    def parent(child: int) -> int:
        return (child - 1) // 2

    def swap(heap_array: list, i: int, j: int) -> None:
        """In place swap of two array elements."""
        if i != j:
            temp = heap_array[i]
            heap_array[i] = heap_array[j]
            heap_array[j] = temp

    #heap property maintence
    def restore_heap_upward(self, index:int) -> None:
        """Restore heap property up after insertion"""
        while index > 0:
            p = self.get_parent_index(index) #find parent index
            if self.heap_array[index] < self.help_array[p]: 
                #if current element is smaller than parent swap them
                self.swap = (index, p)
                #Move index pointer up to parent
                index = p
            else:
                index = 0 #exit array

    def restore_heap_downward(self, index: int) -> None:
        """restore heap downward after removal"""
        size = self.element_counter 
        fin = False
        while not fin:
            #get left and right child indexes
            l = self.get_left_child_index(index)
            r = self.get_right_child_index(index)
            smallest = index # assume current index is smallest
            #compare with left child
            if l < size and self.heap_array[l] < self.heap_array[smallest]:
                smallest = l
            #compare with right child
            if r < size and self.heap_array[r] < self.heap_array[smallest]:
                smallest = r
            # if one of children is smaller, swap and continue down
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                # heap prop restored
                fin = True
    # Public heap operations
    def insert(self, value:str) -> None:
        """Add a new element to the heap array."""
        if self.element_counter < len(self.heap_array):
            #place the element at the next available slot
            self.heap_array[self.element_counter] = value
            #increase count
            self.element_counter += 1
            #restore heap property upward
            self.restore_heap_upward(self.element_counter -1)
    def remove_min(self) -> str | None:
        """Remove and return smallest element"""
        removed = None
        if self.element_counter > 0:
            #smallest elment is always index 0
            removed = self.heap[0]
            #replace root with last element in the heap
            self.heap_array[0] = self.heap_array[self.element_counter - 1]
            #clear last slot
            self.heap_array[self.element_counter -1] = None
            #Decrease the count of elements
            self.element_counter -= 1
            #restore the heap downward
            if self.element_count > 0:
                self.restore_heap_downward(0)
        return removed

    #return smallest element
    def get_min(self) -> str | None:
        """return without removing smallest element"""
        if self.element_counter > 0:
            return self.heap_array[0]
        return None

    #return size of array
    def get_size(self) -> int:
        return self.element_counter

    #print only the portion of the array that has elements
    def __str__(self) -> str:
        return str(self.heap_array[:self.element_counter])

if __name__ == "__main__":
    h = MinHeap()        # Create a heap with capacity 10

h.insert("delta")      # Add element
h.insert("alpha")      # Add element
h.insert("charlie")    # Add element
h.insert("bravo")      # Add element

print("Heap contents:", h)        # ['alpha', 'bravo', 'charlie', 'delta']
print("Smallest element:", h.get_min())  # alpha
print("Heap size:", h.get_size())        # 4

print("Removed:", h.remove_min())        # alpha
print("After removal:", h)  