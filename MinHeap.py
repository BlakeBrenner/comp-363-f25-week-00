class MinHeap:
    """Array-based implementation of a minimum heap (priority queue)."""

    def __init__(self):
        # Dynamic list (no fixed capacity); we still track count explicitly
        self.heap_array = []
        self.element_counter = 0

    # Helper methods
    def left_child(self, parent: int) -> int:
        return 2 * parent + 1

    def right_child(self, parent: int) -> int:
        return 2 * (parent + 1)

    def parent(self, child: int) -> int:
        return (child - 1) // 2

    def swap(self, i: int, j: int) -> None:
        """In-place swap of two array elements."""
        if i != j:
            temp = self.heap_array[i]
            self.heap_array[i] = self.heap_array[j]
            self.heap_array[j] = temp

    # Heap property maintenance ops
    def restore_heap_upward(self, index: int) -> None:
        """Restore heap property after insertion (bubble up)."""
        while index > 0:
            p = self.parent(index)
            if self.heap_array[index] < self.heap_array[p]:
                self.swap(index, p)
                index = p
            else:
                # end loop without break/continue
                index = 0

    def restore_heap_downward(self, index: int) -> None:
        """Restore heap property after removal (bubble down)."""
        size = self.element_counter
        finished = False
        while not finished:
            l = self.left_child(index)
            r = self.right_child(index)
            smallest = index

            if l < size and self.heap_array[l] < self.heap_array[smallest]:
                smallest = l
            if r < size and self.heap_array[r] < self.heap_array[smallest]:
                smallest = r

            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                finished = True

    # Public operations
    def insert(self, value: str) -> None:
        """Add a new element to the heap array."""
        self.heap_array.append(value)
        self.element_counter += 1
        self.restore_heap_upward(self.element_counter - 1)

    def remove_min(self) -> str | None:
        """Remove and return the smallest element."""
        removed = None
        if self.element_counter > 0:
            removed = self.heap_array[0]
            # Move last element to root and shrink array
            self.heap_array[0] = self.heap_array[self.element_counter - 1]
            self.heap_array.pop()
            self.element_counter -= 1
            if self.element_counter > 0:
                self.restore_heap_downward(0)
        return removed

    def get_min(self) -> str | None:
        """Return (without removing) the smallest element."""
        result = None
        if self.element_counter > 0:
            result = self.heap_array[0]
        return result

    def get_size(self) -> int:
        """Return the number of elements currently stored in the heap."""
        return self.element_counter

    def __str__(self) -> str:
        """Readable view of the heap’s current array."""
        return str(self.heap_array)


if __name__ == "__main__":
    h = MinHeap()

    h.insert("delta")
    h.insert("alpha")
    h.insert("charlie")
    h.insert("bravo")

    print("Heap contents:", h)                 # ['alpha', 'bravo', 'charlie', 'delta']
    print("Smallest element:", h.get_min())    # alpha
    print("Heap size:", h.get_size())          # 4

    print("Removed:", h.remove_min())          # alpha
    print("After removal:", h)                 # ['bravo', 'delta', 'charlie']
