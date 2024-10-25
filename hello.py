import pulp
from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Problem", LpMinimize)

# Define the variables
x1 = LpVariable("ChickenPercent", 0, None, LpInteger)
x2 = LpVariable("BeefPercent", 0)
x3 = LpVariable("PorkPercent", 0)

# Objective function: Minimize the total cost
prob += 0.013 * x1 + 0.008 * x2 + 0.010 * x3, "Total Cost of Ingredients per can"

# Constraints
prob += x1 + x2 + x3 == 100, "PercentagesSum"
prob += 0.100 * x1 + 0.200 * x2 + 0.150 * x3 >= 8.0, "ProteinRequirement"
prob += 0.080 * x1 + 0.100 * x2 + 0.090 * x3 >= 6.0, "FatRequirement"
prob += 0.001 * x1 + 0.005 * x2 + 0.004 * x3 <= 2.0, "FibreRequirement"
prob += 0.002 * x1 + 0.005 * x2 + 0.003 * x3 <= 0.4, "SaltRequirement"
prob += 0.010 * x1 + 0.020 * x2 + 0.015 * x3 >= 1.0, "VitaminRequirement"
prob += 0.005 * x1 + 0.010 * x2 + 0.007 * x3 >= 0.5, "MineralRequirement"

# Write the problem data to an .lp file
prob.writeLP("ExpandedWhiskasModel.lp")

# Solve the problem using PuLP's choice of Solver
prob.solve()

# Print the status of the solution
print("Status:", LpStatus[prob.status])

# Print the values of the variables
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the optimized objective function value
print("Total Cost of Ingredients per can = ", value(prob.objective))
