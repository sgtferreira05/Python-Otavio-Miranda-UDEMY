# Deque - Working with LIFO and FIFO
# Deque is a double-ended queue that allows adding and removing elements from both ends

# LIFO (Last In First Out) - Stack:
# It means that the last element added to the stack is the first one to be removed.
# This is similar to a stack of plates, where you can only add or remove the top plate.

# FIFO (First In First Out) - Queue:
# It means that the first element added to the queue is the first one to be removed.
# This is similar to a line of people waiting to enter a store, where the first person in line is the first one to enter.

# Deque is a built-in data structure in Python that allows you to implement both LIFO and FIFO behavior.

# To remove itens at final: O(1) - Constant time complexity
# To remove itens at start: O(n) - Linear time complexity

from collections import deque


list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ✅ Good (LIFO with list)
#  0 1 2 3 4 5 6 7 8 9     - INDICES
# [1 2 3 4 5 6 7 8 9 10]   - VALUES


list.append(11) # Add an element to the end of the list
print(list)
list.append(12) 
print(list)
last_removed = list.pop() # Remove the last element from the list
print(list) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(last_removed) # 12

print('---' * 20)


list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ❌ Bad (FIFO with list)
#  0 1 2 3 4 5 6 7 8 9     - INDICES
# [1 2 3 4 5 6 7 8 9 10]   - VALUES

list.insert(0, 0) # Add an element to the start of the list
print(list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list.insert(0, -1)
print(list) # [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_removed = list.pop(0) # Remove the first element from the list
print(list) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('---' * 20)

# ✅ Good (FIFO with deque) Constant time complexity for adding and removing elements from both ends

correct_stack: deque[int] = deque()
correct_stack.append(1) # Add an element to the end of the deque
correct_stack.append(6) 
correct_stack.append(2) 
correct_stack.append(9)
correct_stack.appendleft(0) # Add an element to the start of the deque
print(correct_stack) # [0, 1, 6, 2, 9]
correct_stack.appendleft(-1) # Add an element to the start of the deque
print(correct_stack) # [-1, 0, 1, 6, 2, 9]
correct_stack.pop() # Remove the last element from the deque
print(correct_stack) # [-1, 0, 1, 6, 2]
correct_stack.popleft() # Remove the first element from the deque
print(correct_stack) # [0, 1, 6, 2]

