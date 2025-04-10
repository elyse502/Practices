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
    