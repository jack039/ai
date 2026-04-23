parent = {'A':['B','C'],'B':['D']}

def father(x,y): return y in parent.get(x,[])
def grandparent(x,z):
    return any(father(x,y) and father(y,z) for y in parent.get(x,[]))

print(father('A','B'))
print(grandparent('A','D'))
'''Experiment 6: Theory
Title:

Introduction to Prolog (Family Tree)

Theory:

Prolog is a logic programming language used in Artificial Intelligence for solving problems based on facts and rules.

In Prolog, knowledge is represented using:

Facts: Basic information (e.g., parent relationships)
Rules: Logical relationships between facts
Queries: Questions asked to the system

The Family Tree problem is a common example where relationships like parent, child, and grandparent are defined using facts and rules.

For example:

A fact: parent(A, B) means A is the parent of B
A rule: grandparent(A, C) if A is parent of B and B is parent of C

Prolog uses backtracking and logical inference to answer queries based on given facts and rules.

Conclusion:

Prolog helps in representing and solving problems using logic, and the family tree example demonstrates how relationships can be derived using rules.'''