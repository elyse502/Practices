#!/usr/bin/python3
import heapq

# help(heapq)

# Create a min-heap
heap = [8, 4, 1, 7]
heapq.heapify(heap)

print(">> Min-Heap:", heap)
print(">> Min element in the heap:", heap[0])

min_element = heapq.heappop(heap)
print("\n>> Popped min element:", min_element)
print(">> Min-Heap after popping:", heap)

heapq.heappush(heap, 3)
print("\n>> Min-Heap after pushing 3:", heap)
print(">> Min element in the heap:", heap[0])
