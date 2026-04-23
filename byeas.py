# P(A|B) = P(B|A)*P(A)/P(B)

P_A = 0.2
P_B_given_A = 0.8
P_B = 0.5

P_A_given_B = (P_B_given_A * P_A) / P_B
print(P_A_given_B)
'''Experiment 9: Theory
Title:

Implementation of Bayes Belief Network

Theory:

A Bayes Belief Network (BBN), also known as a Bayesian Network, is a probabilistic graphical model used in Artificial Intelligence to represent uncertain knowledge.

It consists of:

Nodes: Represent random variables
Edges: Represent dependencies between variables
Conditional Probability Tables (CPT): Show probability relationships

BBN is based on Bayes' Theorem, which is used to calculate the probability of an event based on prior knowledge.

It helps in reasoning under uncertainty by updating probabilities when new evidence is available.

Example:

In a medical diagnosis system:

Disease → Fever → Test Result
The network predicts the probability of a disease based on symptoms.
Applications:
Medical diagnosis
Risk analysis
Decision support systems
Conclusion:

Bayesian Networks provide a powerful way to model uncertainty and make predictions using probability.'''