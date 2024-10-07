# AlgoGroupAssesment

An answer to AlgoGroup's take-home-assesment question 2. 

### Implement an integer stack WITHOUT containers (list, vector, array, etc.).

I decided to attack this question by implementing a linked list structure, where each IntStack has a self.top, a node that keeps track of its own value and the previous node using a tuple, and an integer value variable size, representing the size of the IntStack.
