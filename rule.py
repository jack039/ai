rules = {
    "fever & cough": "Flu",
    "fever & rash": "Measles"
}

sym = "fever & cough"

print(rules.get(sym,"Unknown Disease"))
'''Experiment 10: Theory
Title:

Implementation of Rule-Based Expert System

Theory:

A Rule-Based Expert System is an Artificial Intelligence system that uses a set of predefined rules to make decisions or solve problems, similar to a human expert.

It consists of:

Knowledge Base: Contains facts and rules (IF–THEN statements)
Inference Engine: Applies rules to known facts to derive conclusions

The system works by matching input data with rules and generating an output based on logical reasoning.

Example:

IF patient has fever AND cough
THEN disease = Flu

Applications:
Medical diagnosis
Troubleshooting systems
Decision support systems
Conclusion:

Rule-based expert systems simulate human decision-making using logical rules and are useful in solving domain-specific problems.'''