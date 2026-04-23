PEAS = {
    "Performance": "Clean rooms, minimize time",
    "Environment": ["Room A", "Room B"],
    "Actuators": ["Left", "Right", "Suck"],
    "Sensors": ["Location", "Dirt"]
}
tree = {'Start': ['A','B'], 'A': ['A1','A2'], 'B': ['B1','B2']}

def show(n, k=0):
    print("  "*k + n)
    for c in tree.get(n, []):
        show(c, k+1)

show('Start')
'''Title:
State Space Formulation and PEAS Representation

Theory:

Artificial Intelligence problems are often solved by representing them in a structured way so that a machine can process them effectively. Two important concepts used for this purpose are State Space Formulation and PEAS Representation.

1. State Space Formulation

State space formulation is a method of representing a problem in terms of:

States: All possible configurations of the system
Initial State: The starting point of the problem
Goal State: The desired final outcome
Operators (Actions): Steps used to move from one state to another

In this approach, a problem is viewed as a search through a space of possible states to find a path from the initial state to the goal state.

Example:
In the 8-puzzle problem, each arrangement of tiles represents a state, and moving tiles represents actions.

2. PEAS Representation

PEAS stands for:

P – Performance Measure: Criteria to evaluate success
E – Environment: The surroundings in which the agent operates
A – Actuators: Actions the agent can perform
S – Sensors: Inputs the agent receives

PEAS is used to define an intelligent agent clearly and helps in designing AI systems.

Example of PEAS (Vacuum Cleaner Agent):
Performance: Cleanliness, time efficiency
Environment: Rooms (A and B)
Actuators: Move left/right, suck dirt
Sensors: Detect location and dirt
Conclusion:

State space formulation helps in solving problems using search techniques, while PEAS representation helps in designing intelligent agents by defining their environment and behavior. Both are fundamental concepts in Artificial Intelligence.'''