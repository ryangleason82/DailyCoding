# DailyCoding

#### Mistakes I Have Made

5/31/19

- When iterating through list in python:
  - list index out of range
  - Index out of range unless you use range(len(lst))
- When adding to a list:

  - list assignment index out of range
  - lst.append(val)

6/1/19

- For Jun1st.py, attempted to use a linked list and "Runner Method"

  - It would end up needing two loops which is just as inefficient as the brute force method I developed
  - Only use when you know you need to iterate once and not go back to the beginning
  - I still need to understand the solution

6/3/19

- Sets are unordered in python. In order to loop through a set by a given index,

  - while i in s: i += 1

- Swaps are easy
  - nums[i], nums[v-1] = nums[v-1], nums[i]

6/4/19

- Functional programming is back!
- Use closures
  - Look at the signature type of cons to retrieve its first and last elements
  - Take in a and b, return new anonymous function
    - This takes in f and call f with a and b
  - Input to car and cdr is the anonymous function (pair)
  - So in order to get a and b back, we feed it another function
    - One that atkes in two parameters and returns the first if car, last if cdr.

6/5/19

- A good opportunity to learn about XOR Linked list
- Instead of storing actual memory addresses, every node stores the XOR of address of prev and next nodes
- Ordinary representation of linked list:

  - Node A: prev = NULL, next = add(B) // Prev is NULL and next is address of B
  - Node B: prev = add(A), next = add(C)
  - Node C: prev = add(B), next = add(D)
  - Node D: prev = add(C), next = NULL

- XOR List Representation npx (XOR of next and prev)

  - Node A: npx = 0 XOR add(B) //bitwise XOR of zero and address of B
  - Node B: npx = add(A) XOR add(c)
  - Node C: npx = add(B) XOR add(d)
  - Node D: npx = add(c) xor 0

  - When traversing we must remember the address of the previous and next nodes
