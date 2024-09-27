class Node:
   def __init__(self, key):
       self.key = key
       self.left = None
       self.right = None


class BinarySearchTree:
   def __init__(self):
       self.root = None

   def insert(self, key):
       self.root = self._insert(self.root, key)

   def _insert(self, node, key):
       if not node:
           return Node(key)

       if key < node.key:
           node.left = self._insert(node.left, key)
       elif key > node.key:
           node.right = self._insert(node.right, key)

       return node

   def delete(self, key):
       self.root = self._delete(self.root, key)

   def _delete(self, node, key):
       if not node:
           return node

       if key < node.key:
           node.left = self._delete(node.left, key)
       elif key > node.key:
           node.right = self._delete(node.right, key)
       else:
           if not node.left:
               return node.right
           elif not node.right:
               return node.left
           else:
               node.key = self._min_value(node.right)
               node.right = self._delete(node.right, node.key)

       return node

   def _min_value(self, node):
       current = node
       while current.left:
           current = current.left
       return current.key

   def exists(self, key):
       return self._exists(self.root, key)

   def _exists(self, node, key):
       if not node:
           return False

       if node.key == key:
           return True
       elif key < node.key:
           return self._exists(node.left, key)
       else:
           return self._exists(node.right, key)

   def next(self, key):
       return self._next(self.root, key)

   def _next(self, node, key):
       if not node:
           return "none"

       if key < node.key:
           left_result = self._next(node.left, key)
           if left_result == "none" or left_result <= key:
               return node.key
           else:
               return left_result
       else:
           return self._next(node.right, key)

   def prev(self, key):
       return self._prev(self.root, key)

   def _prev(self, node, key):
       if not node:
           return "none"

       if key > node.key:
           right_result = self._prev(node.right, key)
           if right_result == "none" or right_result >= key:
               return node.key
           else:
               return right_result
       else:
           return self._prev(node.left, key)


bst = BinarySearchTree()

z = open('output.txt', 'w')
with open('input11.txt', 'r') as file:
   for line in file:
       operation, key = line.split()
       key = int(key)

       if operation == 'insert':
           bst.insert(key)
       elif operation == 'delete':
           bst.delete(key)
       elif operation == 'exists':
           z.write(str(bst.exists(key))+'\n')
       elif operation == 'next':
           z.write(str(bst.next(key))+'\n')
       elif operation == 'prev':
           z.write(str(bst.prev(key))+'\n')
