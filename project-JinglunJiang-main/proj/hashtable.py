from collections.abc import MutableMapping

class Hashtable(MutableMapping):
    # polynomial constant, used for _hash
    P_CONSTANT = 37

    def __init__(self, capacity, default_value, load_factor, growth_factor):
        """
        Constructor that initiate the hashtable data structure
        Inputs: self: the data structure itself
                capacity: the initial capacity set to the hashtable (how many cells it starts with)
                default_value: the return value when looking up a key that has not been inserted
                load_factor: between (0, 1], the threshold when exceed this proportion, the hashtable will be rehashed
                growth_factors: the factor used when expanding the hashtable
        Outputs: None
        """
        self._items = [LinkedList() for _ in range(capacity)]
        # Do not change into [LinkedList()] * capacity since lists are mutable!
        self.capacity = capacity
        self.default_value = default_value
        self.load_factor = load_factor
        self.growth_factor = growth_factor
        self.size = 0 # Keep track of the occupied cells in the Hashtable for rehashing

    def _hash(self, key):
        """
        This method takes in a string and returns an integer value.

        This particular hash function uses Horner's rule to compute a large polynomial.

        See https://www.cs.umd.edu/class/fall2019/cmsc420-0201/Lects/lect10-hash-basics.pdf

        DO NOT CHANGE THIS FUNCTION
        """
        val = 0
        for letter in key:
            val = self.P_CONSTANT * val + ord(letter)
        return val
    
    def _get_linked_list(self, key):
        """
        Helper function helps to get the specific linkedlist in the hashtable
        Inputs: the hashtable and the key of the aiming node
        Outputs: the LinkedList in the hashtable
        """
        index = self._hash(key) % self.capacity
        return self._items[index]
    
    def _get_node(self, key):
        """
        Another helper function helps in find the aiming node
        Inputs: the key of the node
        Outputs: the node in the hashtable
        """
        linked_list = self._get_linked_list(key)
        return linked_list.find_node(key) if linked_list.find_node(key) else None

    def __setitem__(self, key, val):
        """
        Adding new node / replacing the val of a already existing key
        Inputs: key and value of the to be hashed node
        Outputs: None
        """
        current_list = self._get_linked_list(key)
        existing_node = self._get_node(key)
        if existing_node:
            existing_node.val = val
        else:
            current_list.add_node(key, val)
            self.size += 1
        if self._load_factor() > self.load_factor:
            self._rehash()

    def __getitem__(self, key):
        """
        Get the value of the node provided the key
        Inputs: key of the node
        Outputs: the value of the node
        """
        node = self._get_node(key)
        return node.val if node else self.default_value

    def __delitem__(self, key):
        """
        Deletion method of the hashtable
        Inputs: the key of the node to be deleted
        Outputs: None
        """
        current_list = self._get_linked_list(key)
        existing_node = self._get_node(key)
        if existing_node:
            current_list.remove_node(key)
            self.size -= 1
        else:
            raise KeyError

    def __len__(self):
        """
        Returns the length of the current hashtable
        Inputs: None
        Outputs: the size
        """
        return self.size

    def __iter__(self):
        """
        You do not need to implement __iter__ for this assignment.
        This stub is needed to satisfy `MutableMapping` however.)

        Note, by not implementing __iter__ your implementation of Markov will
        not be able to use things that depend upon it,
        that shouldn't be a problem but you'll want to keep that in mind.
        """
        raise NotImplementedError("__iter__ not implemented")
    
    def _load_factor(self):
        """
        Method for calculating the current load factor
        Inputs: None
        Outputs: None
        """
        return self.size / self.capacity
    
    def _rehash(self):
        """
        Method for rehashing the current hashtable
        Inputs: None
        Outputs: None
        """
        new_capacity = self.capacity * self.growth_factor
        new_items = [LinkedList() for _ in range(new_capacity)]

        for linked_list in self._items:
            current_node = linked_list.head
            while current_node:
                new_index = self._hash(current_node.key) % new_capacity
                new_items[new_index].add_node(current_node.key, current_node.val)
                current_node = current_node.next
        
        self._items = new_items
        self.capacity = new_capacity
    
class Node():
    def __init__(self, key, val):
        """
        Constructor for the Node object.
        Inputs: key: Identifies the entry in the hashtable and is used for hashing
                val: The data associated with the key
        """
        self.key = key
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        """
        Constructor for LinkedList object
        """
        self.head = None

    def add_node(self, key, val):
        """
        Method for adding a node to the existing linkedlist
        Inputs: key: the key of the new node
                val: the value associated with the key
        Outputs: None
        """
        new_node = Node(key, val)
        if not self.head:
        # If current linkedlist is empty, add the new_node as the head of the linkedlist
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
            # Move the pointer to the last item in the linkedlist
                current_node = current_node.next
            current_node.next = new_node

    def remove_node(self, key):
        """
        Method for removing a specific node from the list
        Inputs: key: the key for the to be removed node
        Outputs: None
        """
        current_node = self.head
        if current_node and current_node.key == key:
            self.head = current_node.next
            return
        while current_node.next: 
            # cannot iterate by current_node, since the pointer of current has to be reserved
            if current_node.next.key == key:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
        raise KeyError

    def find_node(self, key):
        """
        Method for finding a specific node by its key
        Inputs: key: the key for the Node
        Outputs: the node if finded, None if otherwise
        """
        current_node = self.head
        while current_node:
            if current_node.key == key:
                return current_node
            if current_node.next:
                current_node = current_node.next
            else:
                return None
