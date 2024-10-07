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

    

