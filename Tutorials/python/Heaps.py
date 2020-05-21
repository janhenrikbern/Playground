class SimpleBinaryHeapTree:
    def __init__(self, heap_condition = None):
        """
        kwargs:
            heap_condition: Sorting condition wrapped into a function
                            Example: 
                                    heap_condition = lambda check_val, base_val: check_val > base_val

                                Explanation: Return true when  `check_val` is a better val than `base_val`
        """
        self.heap = []
        self._heapCondition = heap_condition

      
    def _getParent(self, index):
        return (index - 1) // 2
    
    def _getLeftChild(self, index):
        return 2 * index + 1

    def _getRightChild(self, index):
        return 2 * index + 2


    def _hasParent(self, index):
        return 0 <= self._getParent(index)

    def _hasLeftChild(self, index):
        return len(self.heap) > self._getLeftChild(index)

    def _hasRightChild(self, index):
        return len(self.heap) > self._getRightChild(index)


    def _swap(self, index_1, index_2):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]

    def _heapifyUp(self, start_index = -1):
        """
        Worst case performance at the order of O(log n)
        """
        if not self._heapCondition: return
        index = start_index if start_index > 0 else len(self.heap) + start_index
        while self._hasParent(index) and self._heapCondition(self.heap[index], self.heap[self._getParent(index)]):
            parent_idx = self._getParent(index)
            self._swap(index, parent_idx)
            index = parent_idx

    def _heapifyDown(self, start_index = 0):
        if not self._heapCondition: return
        index = start_index
        while self._hasLeftChild(index):
            child_idx = self._getBestChild(index)
            if not child_idx: break
            if self._heapCondition(self.heap[child_idx], self.heap[index]):
                self._swap(index, child_idx)
                index = child_idx
            else:
                break

    def _getBestChild(self, index):
        if not self._hasLeftChild(index): return None # explicit - import to trigger break condition
        child_idx = self._getLeftChild(index)
        if self._hasRightChild(index) and self._heapCondition(self.heap[self._getRightChild(index)], self.heap[child_idx]):
            child_idx = self._getRightChild(index)
        return child_idx


    def printHeap(self):
        print(self.heap)

    def add(self, value):
        """
        add a value to the heap tree

        value: object to add to the heap tree.
        """
        self.heap.append(value)
        self._heapifyUp()

    def pop_root(self):
        self._swap(0, -1)
        root = self.heap.pop()
        self._heapifyDown()
        return root
    
    def length(self):
        return len(self.heap)


class MinHeap(SimpleBinaryHeapTree):

    def __init__(self):
        fn = lambda x, y: x <= y
        super().__init__(heap_condition=fn)



class MaxHeap(SimpleBinaryHeapTree):
    
    def __init__(self):
        fn = lambda x,y: x >= y
        super().__init__(heap_condition=fn)


if __name__ == "__main__":

    print(">>> TEST START")
    vals = [4, 1, 2, 4, 5, 3, 6, 7, 2, 5]
    minHeap = MinHeap()
    maxHeap = MaxHeap()
    print("\n>>> CASE 1: \n  Growing Heap \n")
    for v in vals:
        minHeap.add(v)
        maxHeap.add(v)
        minHeap.printHeap()
        maxHeap.printHeap()

    print("\n>>> CASE 2:\n  Shrinking Heap \n")
    min_sorted = []
    max_sorted = []
    minHeap.printHeap()
    maxHeap.printHeap()
    for v in vals:
        min_sorted.append(minHeap.pop_root())
        max_sorted.append(maxHeap.pop_root())
        minHeap.printHeap()
        maxHeap.printHeap()

    print(min_sorted)
    print(max_sorted)

    print("\n>>> TEST END")

