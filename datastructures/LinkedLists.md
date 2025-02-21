# Linked Lists

One of the most useful data structures

A sequential list of nodes which point to other notes also containing data

Nodes are always structs or classes

Last node always points to `null`

___Head___ = First Node

___Tail___ = Last Node

References (pointers) use memory, which is why we care about the distinction between uses:

* On a 64 bit machine, __8 bytes__ each
* On a 32 bit machine, __4 bytes__ each

## Uses

* Used in lists, stacks, queues for their great time complexity
* Creating circular lists
* Easily model real world objects such as trains
* Used in certain hashmap implementations to deal with hashing collisions
* Often used in implementation of adjacency lists for graphs

## Singly Linked Lists

Nodes only hold a reference to the next node

___Always___ maintain a reference to the head and tail nodes for quick additions/removals

Pros:

* Uses less memory
* Simpler implementation

Cons:

* Cannot easily access previous elements

### Singly Linked List Implementation

___Insert___: Create a traverse pointer, travel to the node at the "index" to insert.. Add a new node which copies the current nodes "next". Change the "next" pointer of the current node to the new inserted node.

___Remove___: Create two traversal pointers, with one pointing to the head and the other pointing to the heads "next". Traverse both until the forward traverse is on the removal node. Create temp pointer to removal node for deallocation and move forward traversal to the deletion nodes "next". Set the rear traversal nodes next to the forward traversal node. Deallocate temp.

## Doubly Linked Lists

Pros:

* Can be traversed backwards
* We can remove a node in constant time because we have the bidirectional references and can easily patch the hole

Cons:

* Takes 2x more memory than the singly linked list

### Doubly Linked List Implementation

___Insert___: Very similar to singly linked list. Create a traverse pointer, travel to the node at the "index" to insert. Add a new node which copies the current nodes "next", and add the current node to the new nodes "previous" pointer. Change the "next" pointer of the current node to the new inserted node, and the previous pointer of the new node to the current traverse node.

___Remove___: Create __one__ traversal pointer, at the head. Seek until we hit the removal target. Set removal nodes "previous" node's "next" pointer to the removal node's "next". Also set removal node's "next" node's previous to removal's "previous". Remove traversal/removal node.

## Complexity

| Function         | Singly Linked | Doubly Linked  |
| :--------------- | :-----------: | -------------: |
| Search           | $O(n)$        | $O(n)$         |
| Insert At Head   | $O(1)$        | $O(1)$         |
| Insert At Tail   | $O(1)$        | $O(1)$         |
| Remove At Head   | $O(1)$        | $O(1)$         |
| Remove At Tail   | $O(n)$        | $O(1)$         |
| Remove In Middle | $O(n)$        | $O(n)$         |

* Note ___inserting at tail for a singly linked list___ is __only__ $O(1)$ if we maintain a pointer to the tail. Otherwise it is $O(n)$.
* Always remember these are the ___worst___ case scenarios

## Source Code Implementation

Implemented doubly linked lists in python [here](/datastructures/src/DoublyLinkedList.py)
