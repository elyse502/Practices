class MaxHeap:
    def __init__(self):
        self.heap = []

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    @staticmethod
    def _get_left_child_index(index):
        return (index * 2) + 1
    
    @staticmethod
    def _get_right_child_index(index):
        return (index * 2) + 2
    
    @staticmethod
    def _get_parent_index(index):
        return (index - 1) // 2
    
    def _heapify_up(self):
        current_index = len(self.heap) - 1
        while current_index > 0:
            parent_index = self._get_parent_index(current_index)
            if self.heap[current_index] > self.heap[parent_index]:
                self._swap(current_index, parent_index)
                current_index = parent_index
            else:
                break
    
    def _heapify_down(self):
        pass  

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()

    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        return max_value
