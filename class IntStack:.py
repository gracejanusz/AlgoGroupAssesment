class IntStack:
    def __init__(self) -> None:
        """initialize an empty stack."""
        self.top = None
        self._size = 0

    def size(self) -> int:
        """returns the number of integers in the stack."""
        return self._size

    def push(self, item: int) -> None:
        """push an integer onto the top of the stack.

        pre: a valid integer is passed in.
        post: the integer is added to the top of the stack, and the size of the stack is incremented by 1.
        """
        self.top = (item, self.top)
        self._size += 1

    def pop(self) -> int:
        """remove and return the item at the top of the stack.

        pre: stack is passed in.
        post: the top item is removed from the stack, and the size of the stack is decremented by 1.
        """
        if self.top is None:
            raise IndexError("pop from empty stack")
        else: 
            result, previous_top = self.top
            self.top = previous_top
            self._size -= 1
            return result

    def peek(self) -> int:
        """return the item at the top of the stack without popping it.

        pre: stack is passed in.
        post: the top item is returned, and the stack remains unchanged.
        """
        if self.top is None:
            raise IndexError("peek from empty stack")
        result, _ = self.top
        return result

import unittest

class Test_IntStack(unittest.TestCase):

    def setUp(self):
        self.stack = IntStack()

    def test_initial_size(self):
        """check that intial size is 0"""
        self.assertEqual(self.stack.size(), 0)

    def test_push_increases_size(self):
        """check that pushing an int onto stack increases size of stack"""
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

    def test_push_items(self):
        """make sure ints are correctly pushed onto stack"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.peek(), 3)

    def test_pop_decreases_size(self):
        """Testing that Popping decreases the size of the stack"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

    def test_pop_returns_last_item(self):
        """Check that popping pops the most recently addded item"""
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_empty_stack(self):
        """Error is thrown when you try to pop empty stack"""
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek(self):
        """check that peek does not pop top item from stack"""
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(self.stack.size(), 2)  # The size should remain unchanged.

    def test_peek_empty_stack(self):
        """check that you can't peek on an empty stack"""
        with self.assertRaises(IndexError):
            self.stack.peek()

if __name__ == '__main__':
    unittest.main()


