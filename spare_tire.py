print("AI Planning Spare Tire Problem (Structured Plan)")

flat_tire = "axle"
spare_tire = "trunk"
tools = "trunk"
car = "ground"

print("\n--- Initial State ---")
print("Flat Tire:", flat_tire)
print("Spare Tire:", spare_tire)
print("Tools:", tools)
print("Car:", car)

print("\n--- Planning Execution ---")

print("\nStep 1: Open trunk")

if spare_tire == "trunk":
    print("Step 2: Take spare tire from trunk")
    spare_tire = "ground"

if tools == "trunk":
    print("Step 3: Take tools (jack & wrench)")
    tools = "ground"

if flat_tire == "axle":
    print("Step 4: Loosen nuts of flat tire")

print("Step 5: Lift car using jack")
car = "lifted"

if flat_tire == "axle":
    print("Step 6: Remove flat tire")
    flat_tire = "ground"

if spare_tire == "ground":
    print("Step 7: Mount spare tire on axle")
    spare_tire = "axle"

print("Step 8: Tighten nuts")

print("Step 9: Lower the car")
car = "ground"

print("Step 10: Close trunk")

print("\n--- Goal State ---")
print("Flat Tire:", flat_tire)
print("Spare Tire:", spare_tire)
print("Tools:", tools)
print("Car:", car)

if spare_tire == "axle" and flat_tire == "ground":
    print("\nGoal Achieved: Tire replaced successfully")
else:
    print("\nGoal Not Achieved")
    '''Experiment 8: Theory
Title:

Planning Programming (Spare Tyre Problem)

Theory:

Planning in Artificial Intelligence refers to the process of generating a sequence of actions to achieve a specific goal from an initial state.

The Spare Tyre Problem is a classic example used to demonstrate planning. In this problem, a car has a flat tyre, and a spare tyre is available in the boot. The objective is to replace the flat tyre with the spare tyre.

The problem is represented using:

Initial State: Flat tyre on the car, spare tyre in the boot
Goal State: Spare tyre on the car
Actions: Remove flat tyre, take spare tyre from boot, fix spare tyre

The planning system determines the correct sequence of actions required to reach the goal state.

Conclusion:

Planning helps in solving problems by finding an optimal sequence of actions, and the spare tyre problem illustrates how AI can model real-world tasks step by step.'''