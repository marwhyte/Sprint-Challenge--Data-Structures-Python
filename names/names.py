import time


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if self.value == value:
        #     return
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value and self.left:
            return self.left.contains(target)
        elif target > self.value and self.right:
            return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)

        while len(queue) is not 0:
            getLeftRight = queue.pop(0)
            print(getLeftRight.value)
            if getLeftRight.left:
                queue.append(getLeftRight.left)
            if getLeftRight.right:
                queue.append(getLeftRight.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self, node):
        stack = []
        stack.append(node)

        while len(stack) is not 0:
            depthVal = stack.pop()
            print(depthVal.value)
            if depthVal.right:
                stack.append(depthVal.right)
            if depthVal.left:
                stack.append(depthVal.left)

            #    1. stack = [1]                            |-------1 --------|
            #    2. depthVal = 1 stack = []            |---2----|      |-----3-----|
            #    3. stack = [3, 2]                     4        5       6           6
            #    4. depthVal = 2 stack = [3]
            #    5. stack = [3, 5, 4]
            #    6. depthVal = 4 stack = [3, 5]
            #    7. stack = [3, 5]
            #    7. depthVal = 5 stack = [3]
            #    8. depthVal = 3 stack = [7, 6]
            #    9. depthVal = 6 stack = [7]
            #    10. depthVal 7

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# name1BST = BSTNode(names_1[0])
# for name in names_1:
#     name1BST.insert(name)

# for name in names_2:
#     if name1BST.contains(name):
#         duplicates.append(name)

cache = {}
for name in names_1:
    if name not in cache:
        # number is fastest, then comes string, then boolean
        cache[name] = 1
for name in names_2:
    if name in cache:
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
