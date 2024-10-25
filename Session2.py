# %%
import pulp
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl


def plot_x_y(x, y, x_label, y_label, title) -> None:
    # plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker="o", linestyle="-", color="b")
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(True)
    plt.show()


# %%
def problem1():
    # List available solvers:
    print(pulp.listSolvers(onlyAvailable=True))

    # Declare numerical value
    MaxWarehousesP = 3

    # Index sets: We use the type list
    Customers = [
        "Chicago",
        "Atlanta",
        "NewYork",
        "StLouis",
        "Detroit",
        "Cincinnati",
        "Pittsburgh",
        "Charlotte",
        "Boston",
    ]
    Warehouses = [
        "Chicago",
        "Atlanta",
        "NewYork",
        "StLouis",
        "Detroit",
        "Cincinnati",
        "Pittsburgh",
        "Charlotte",
        "Boston",
    ]

    # Dictionary for the demand
    demand = {
        "Chicago": 2870000,
        "Atlanta": 572000,
        "NewYork": 8450000,
        "StLouis": 350000,
        "Detroit": 901000,
        "Cincinnati": 333000,
        "Pittsburgh": 306000,
        "Charlotte": 723000,
        "Boston": 610000,
    }

    # Nested dictionary
    distance = {
        "Chicago": {
            "Chicago": 0,
            "Atlanta": 720,
            "NewYork": 790,
            "StLouis": 297,
            "Detroit": 283,
            "Cincinnati": 296,
            "Pittsburgh": 461,
            "Charlotte": 769,
            "Boston": 996,
        },
        "Atlanta": {
            "Chicago": 720,
            "Atlanta": 0,
            "NewYork": 884,
            "StLouis": 555,
            "Detroit": 722,
            "Cincinnati": 461,
            "Pittsburgh": 685,
            "Charlotte": 245,
            "Boston": 1099,
        },
        "NewYork": {
            "Chicago": 790,
            "Atlanta": 884,
            "NewYork": 0,
            "StLouis": 976,
            "Detroit": 614,
            "Cincinnati": 667,
            "Pittsburgh": 371,
            "Charlotte": 645,
            "Boston": 219,
        },
        "StLouis": {
            "Chicago": 297,
            "Atlanta": 555,
            "NewYork": 976,
            "StLouis": 0,
            "Detroit": 531,
            "Cincinnati": 359,
            "Pittsburgh": 602,
            "Charlotte": 715,
            "Boston": 1217,
        },
        "Detroit": {
            "Chicago": 283,
            "Atlanta": 722,
            "NewYork": 614,
            "StLouis": 531,
            "Detroit": 0,
            "Cincinnati": 263,
            "Pittsburgh": 286,
            "Charlotte": 629,
            "Boston": 721,
        },
        "Cincinnati": {
            "Chicago": 296,
            "Atlanta": 461,
            "NewYork": 667,
            "StLouis": 359,
            "Detroit": 263,
            "Cincinnati": 0,
            "Pittsburgh": 288,
            "Charlotte": 479,
            "Boston": 907,
        },
        "Pittsburgh": {
            "Chicago": 461,
            "Atlanta": 685,
            "NewYork": 371,
            "StLouis": 602,
            "Detroit": 286,
            "Cincinnati": 288,
            "Pittsburgh": 0,
            "Charlotte": 448,
            "Boston": 589,
        },
        "Charlotte": {
            "Chicago": 769,
            "Atlanta": 245,
            "NewYork": 645,
            "StLouis": 715,
            "Detroit": 629,
            "Cincinnati": 479,
            "Pittsburgh": 448,
            "Charlotte": 0,
            "Boston": 867,
        },
        "Boston": {
            "Chicago": 996,
            "Atlanta": 1099,
            "NewYork": 219,
            "StLouis": 1217,
            "Detroit": 721,
            "Cincinnati": 907,
            "Pittsburgh": 589,
            "Charlotte": 867,
            "Boston": 0,
        },
    }

    # Setup costs
    setup_costs = 100000
    # Declaring a problem
    plp = pulp.LpProblem("Problem_1", pulp.LpMinimize)

    # Declaring variables
    y = pulp.LpVariable.dicts("y", (Warehouses), 0, 1, pulp.LpBinary)
    x = pulp.LpVariable.dicts("x", (Warehouses, Customers), 0, 1, pulp.LpBinary)

    # Adding objective function
    plp += pulp.lpSum(
        distance[i][j] * x[i][j] for i in Warehouses for j in Customers
    ) + pulp.lpSum(setup_costs * y[i] for i in Warehouses)

    # Constraints
    # Customer demand must be met
    for j in Customers:
        plp += pulp.lpSum(x[i][j] for i in Warehouses) == 1

    # # Use only p warehouses
    # plp += pulp.lpSum(y[i] for i in Warehouses) == MaxWarehousesP

    # Linking constraints
    for j in Customers:
        for i in Warehouses:
            plp += x[i][j] <= y[i]

    # Create an LP File that shows the model that was created in a certain format.
    # It can be helpful for debugging for instance.
    plp.writeLP("Problem_1.pl")

    # Solve the model with the default solver (CBC)
    plp.solve()

    # Or pick a different solver
    # cplex = pulp.CPLEX_CMD()
    # plp.solve(cplex)

    # Print status and objective function value
    print(" Status:", pulp.LpStatus[plp.status])
    print(" objective value: ", pulp.value(plp.objective))

    # Show values of decision variables
    for var in plp.variables():
        if var.varValue > 0 and var.name.startswith("y_"):
            print("Open", str(var.name).replace("y_", ""))


# Call the function
problem1()


# %%
# Added Capacity Limitations
def problem2() -> None:
    # Declare numerical value
    MaxWarehousesP = 3

    # Index sets: We use the type list
    Customers = [
        "Chicago",
        "Atlanta",
        "NewYork",
        "StLouis",
        "Detroit",
        "Cincinnati",
        "Pittsburgh",
        "Charlotte",
        "Boston",
    ]
    Warehouses = [
        "Chicago",
        "Atlanta",
        "NewYork",
        "StLouis",
        "Detroit",
        "Cincinnati",
        "Pittsburgh",
        "Charlotte",
        "Boston",
    ]

    # Dictionary for the demand
    demand = {
        "Chicago": 2870000,
        "Atlanta": 572000,
        "NewYork": 8450000,
        "StLouis": 350000,
        "Detroit": 901000,
        "Cincinnati": 333000,
        "Pittsburgh": 306000,
        "Charlotte": 723000,
        "Boston": 610000,
    }

    # Nested dictionary
    distance = {
        "Chicago": {
            "Chicago": 0,
            "Atlanta": 720,
            "NewYork": 790,
            "StLouis": 297,
            "Detroit": 283,
            "Cincinnati": 296,
            "Pittsburgh": 461,
            "Charlotte": 769,
            "Boston": 996,
        },
        "Atlanta": {
            "Chicago": 720,
            "Atlanta": 0,
            "NewYork": 884,
            "StLouis": 555,
            "Detroit": 722,
            "Cincinnati": 461,
            "Pittsburgh": 685,
            "Charlotte": 245,
            "Boston": 1099,
        },
        "NewYork": {
            "Chicago": 790,
            "Atlanta": 884,
            "NewYork": 0,
            "StLouis": 976,
            "Detroit": 614,
            "Cincinnati": 667,
            "Pittsburgh": 371,
            "Charlotte": 645,
            "Boston": 219,
        },
        "StLouis": {
            "Chicago": 297,
            "Atlanta": 555,
            "NewYork": 976,
            "StLouis": 0,
            "Detroit": 531,
            "Cincinnati": 359,
            "Pittsburgh": 602,
            "Charlotte": 715,
            "Boston": 1217,
        },
        "Detroit": {
            "Chicago": 283,
            "Atlanta": 722,
            "NewYork": 614,
            "StLouis": 531,
            "Detroit": 0,
            "Cincinnati": 263,
            "Pittsburgh": 286,
            "Charlotte": 629,
            "Boston": 721,
        },
        "Cincinnati": {
            "Chicago": 296,
            "Atlanta": 461,
            "NewYork": 667,
            "StLouis": 359,
            "Detroit": 263,
            "Cincinnati": 0,
            "Pittsburgh": 288,
            "Charlotte": 479,
            "Boston": 907,
        },
        "Pittsburgh": {
            "Chicago": 461,
            "Atlanta": 685,
            "NewYork": 371,
            "StLouis": 602,
            "Detroit": 286,
            "Cincinnati": 288,
            "Pittsburgh": 0,
            "Charlotte": 448,
            "Boston": 589,
        },
        "Charlotte": {
            "Chicago": 769,
            "Atlanta": 245,
            "NewYork": 645,
            "StLouis": 715,
            "Detroit": 629,
            "Cincinnati": 479,
            "Pittsburgh": 448,
            "Charlotte": 0,
            "Boston": 867,
        },
        "Boston": {
            "Chicago": 996,
            "Atlanta": 1099,
            "NewYork": 219,
            "StLouis": 1217,
            "Detroit": 721,
            "Cincinnati": 907,
            "Pittsburgh": 589,
            "Charlotte": 867,
            "Boston": 0,
        },
    }

    # Setup costs
    setup_costs = 100000
    # Capacity Limitations
    ## Dictionary comprehension
    capacity = {city: value * 3 for city, value in demand.items()}
    print(capacity)

    # Declaring a problem
    plp = pulp.LpProblem("Problem_2", pulp.LpMinimize)

    # Declaring variables
    y = pulp.LpVariable.dicts("y", (Warehouses), 0, 1, pulp.LpBinary)
    x = pulp.LpVariable.dicts("x", (Warehouses, Customers), 0, 1, pulp.LpBinary)

    # Adding objective function
    plp += pulp.lpSum(
        distance[i][j] * x[i][j] for i in Warehouses for j in Customers
    ) + pulp.lpSum(setup_costs * y[i] for i in Warehouses)

    # Constraints
    # Customer demand must be met
    for j in Customers:
        plp += pulp.lpSum(x[i][j] for i in Warehouses) == 1

    # Add Capacity Constraint
    for i in Warehouses:
        plp += pulp.lpSum(x[i][j] * demand[j] for j in Customers) <= capacity[i] * y[i]
    # plp += pulp.lpSum(y[i] for i in Warehouses) == MaxWarehousesP

    # Linking constraints
    for j in Customers:
        for i in Warehouses:
            plp += x[i][j] <= y[i]

    # Create an LP File that shows the model that was created in a certain format.
    # It can be helpful for debugging for instance.
    plp.writeLP("Problem_2.pl")

    # Solve the model with the default solver (CBC)
    plp.solve()

    # Print status and objective function value
    print(" Status:", pulp.LpStatus[plp.status])
    print(" objective value: ", pulp.value(plp.objective))

    # Show values of decision variables
    for var in plp.variables():
        if var.varValue > 0 and var.name.startswith("y_"):
            print("Open", str(var.name).replace("y_", ""))


# Call the function
problem2()


# %%
def problem3() -> None:
    # Declare numerical value
    MaxFacilities = 1

    # Index sets: We use the type list
    Customers = list(range(1, 6))
    Facilities = ["New1", "New2", "New3", "New4"]

    demand = {1: 1, 2: 1, 3: 3, 5: 1, 5: 1}
    # Distance dictionary
    distance = {
        "New1": {
            1: 5,
            2: 6,
            3: 12,
            4: 2,
            5: 5,
        },
        "New2": {
            1: 2,
            2: 20,
            3: 10,
            4: 2,
            5: 9,
        },
        "New3": {
            1: 5,
            2: 4,
            3: 9,
            4: 13,
            5: 2,
        },
        "New4": {
            1: 13,
            2: 2,
            3: 2,
            4: 1,
            5: 3,
        },
    }

    # Declaring a problem
    plp = pulp.LpProblem("Problem_3", pulp.LpMinimize)

    # Declaring variables
    x = pulp.LpVariable.dicts("x", (Facilities, Customers), 0, 1, pulp.LpBinary)
    y = pulp.LpVariable.dicts("y", (Facilities), 0, 1, pulp.LpBinary)
    z = pulp.LpVariable("z")

    # Adding objective function
    plp += z

    # Constraints
    # Distance must be under z
    for j in Customers:
        plp += pulp.lpSum(distance[i][j] * x[i][j] for i in Facilities) <= z

    for j in Customers:
        plp += pulp.lpSum(x[i][j] for i in Facilities) == 1

    for j in Customers:
        for i in Facilities:
            plp += x[i][j] <= y[i]
    # Open facilities
    plp += pulp.lpSum(y[i] for i in Facilities) == MaxFacilities

    # Create an LP File that shows the model that was created in a certain format.
    # It can be helpful for debugging for instance.
    plp.writeLP("Problem_3.pl")

    # Solve the model with the default solver (CBC)
    plp.solve()

    # Or pick a different solver
    # cplex = pulp.CPLEX_CMD()
    # plp.solve(cplex)

    # Print status and objective function value
    print(" Status:", pulp.LpStatus[plp.status])
    print(" objective value: ", pulp.value(plp.objective))

    # Show values of decision variables
    for var in plp.variables():
        if var.varValue > 0 and var.name.startswith("y_"):
            print("Open", str(var.name).replace("y_", ""))


# Call the function
problem3()


# %%
def problem4() -> None:  # Multiple objectives
    Customers = list(range(0, 5))
    Warehouses = ["New1", "New2", "New3", "New4"]
    MaxWarehousesP = 1
    demand = {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}

    distance = {
        "New1": {0: 5, 1: 6, 2: 12, 3: 2, 4: 5},
        "New2": {0: 2, 1: 20, 2: 10, 3: 2, 4: 9},
        "New3": {0: 5, 1: 4, 2: 9, 3: 13, 4: 2},
        "New4": {0: 13, 1: 2, 2: 2, 3: 1, 4: 3},
    }

    # model
    # create object that represents the specific instance of the model
    plp = pulp.LpProblem(" The plant center problem ", pulp.LpMinimize)  # problem

    # variables
    y = pulp.LpVariable.dicts("y", (Warehouses), 0, 1, pulp.LpBinary)
    x = pulp.LpVariable.dicts("x", (Warehouses, Customers), 0, 1, pulp.LpBinary)
    z = pulp.LpVariable("z")

    # add objective
    # The objective function is logically entered first, with an important comma , at the end of the statement and a short string explaining what this objective function is:
    # plp += pulp.lpSum(distance[i][j] * x[i][j] for i in Warehouses for j in Customers )
    plp += z

    # add constraints
    for j in Customers:
        plp += pulp.lpSum(x[i][j] for i in Warehouses) == 1

    plp += pulp.lpSum(y[i] for i in Warehouses) == MaxWarehousesP

    for j in Customers:
        for i in Warehouses:
            plp += x[i][j] <= y[i]

    #  for i in Warehouses:
    #     plp+=pulp.lpSum(x[i][j]*demand[j] for j in Customers)<=y[i]*capacity[i]

    for j in Customers:
        plp += pulp.lpSum(x[i][j] * distance[i][j] for i in Warehouses) <= z

    # optional: generate an lp file
    plp.writeLP("warehouseLocation.lp")

    # solve with default solver
    plp.solve()

    # solution output
    print(" Status:", pulp.LpStatus[plp.status])
    print(" objective  value: ", pulp.value(plp.objective))
    # total distance:
    tot_dist = 0
    for i in Warehouses:
        for j in Customers:
            if x[i][j].value() > 0:
                tot_dist += distance[i][j]

    max_dist = 0
    for i in Warehouses:
        for j in Customers:
            if x[i][j].value() > 0:
                if distance[i][j] > max_dist:
                    max_dist = distance[i][j]

    for var in plp.variables():
        if var.varValue > 0:
            print(var.name, "=", var.varValue)


problem4()


# %%
def problem5() -> None:  ## Weighted objective - pCenter
    Customers = [
        "Chicago",
        "Atlanta",
        "NewYork",
        "StLouis",
        "Detroit",
        "Cincinnati",
        "Pittsburgh",
        "Charlotte",
        "Boston",
    ]
    Warehouses = [
        "Chicago",
        "Atlanta",
        "NewYork",
        "StLouis",
        "Detroit",
        "Cincinnati",
        "Pittsburgh",
        "Charlotte",
        "Boston",
    ]
    MaxWarehousesP = 3
    demand = {
        "Chicago": 2870000,
        "Atlanta": 572000,
        "NewYork": 8450000,
        "StLouis": 350000,
        "Detroit": 901000,
        "Cincinnati": 333000,
        "Pittsburgh": 306000,
        "Charlotte": 723000,
        "Boston": 610000,
    }
    setup_cost = {
        "Chicago": 10000,
        "Atlanta": 15000,
        "NewYork": 20000,
        "StLouis": 25000,
        "Detroit": 30000,
        "Cincinnati": 35000,
        "Pittsburgh": 40000,
        "Charlotte": 45000,
        "Boston": 50000,
    }
    # use a dictionary comprehension
    capacity = {city: value * 3 for city, value in demand.items()}

    distance = {
        "Chicago": {
            "Chicago": 0,
            "Atlanta": 720,
            "NewYork": 790,
            "StLouis": 297,
            "Detroit": 283,
            "Cincinnati": 296,
            "Pittsburgh": 461,
            "Charlotte": 769,
            "Boston": 996,
        },
        "Atlanta": {
            "Chicago": 720,
            "Atlanta": 0,
            "NewYork": 884,
            "StLouis": 555,
            "Detroit": 722,
            "Cincinnati": 461,
            "Pittsburgh": 685,
            "Charlotte": 245,
            "Boston": 1099,
        },
        "NewYork": {
            "Chicago": 790,
            "Atlanta": 884,
            "NewYork": 0,
            "StLouis": 976,
            "Detroit": 614,
            "Cincinnati": 667,
            "Pittsburgh": 371,
            "Charlotte": 645,
            "Boston": 219,
        },
        "StLouis": {
            "Chicago": 297,
            "Atlanta": 555,
            "NewYork": 976,
            "StLouis": 0,
            "Detroit": 531,
            "Cincinnati": 359,
            "Pittsburgh": 602,
            "Charlotte": 715,
            "Boston": 1217,
        },
        "Detroit": {
            "Chicago": 283,
            "Atlanta": 722,
            "NewYork": 614,
            "StLouis": 531,
            "Detroit": 0,
            "Cincinnati": 263,
            "Pittsburgh": 286,
            "Charlotte": 629,
            "Boston": 721,
        },
        "Cincinnati": {
            "Chicago": 296,
            "Atlanta": 461,
            "NewYork": 667,
            "StLouis": 359,
            "Detroit": 263,
            "Cincinnati": 0,
            "Pittsburgh": 288,
            "Charlotte": 479,
            "Boston": 907,
        },
        "Pittsburgh": {
            "Chicago": 461,
            "Atlanta": 685,
            "NewYork": 371,
            "StLouis": 602,
            "Detroit": 286,
            "Cincinnati": 288,
            "Pittsburgh": 0,
            "Charlotte": 448,
            "Boston": 589,
        },
        "Charlotte": {
            "Chicago": 769,
            "Atlanta": 245,
            "NewYork": 645,
            "StLouis": 715,
            "Detroit": 629,
            "Cincinnati": 479,
            "Pittsburgh": 448,
            "Charlotte": 0,
            "Boston": 867,
        },
        "Boston": {
            "Chicago": 996,
            "Atlanta": 1099,
            "NewYork": 219,
            "StLouis": 1217,
            "Detroit": 721,
            "Cincinnati": 907,
            "Pittsburgh": 589,
            "Charlotte": 867,
            "Boston": 0,
        },
    }

    # model
    # create object that represents the specific instance of the model
    plp = pulp.LpProblem(" The plant center problem ", pulp.LpMinimize)  # problem

    # variables
    y = pulp.LpVariable.dicts("y", (Warehouses), 0, 1, pulp.LpBinary)
    x = pulp.LpVariable.dicts("x", (Warehouses, Customers), 0, 1, pulp.LpBinary)
    z = pulp.LpVariable("z")

    # add objective
    # The objective function is logically entered first, with an important comma , at the end of the statement and a short string explaining what this objective function is:
    plp += pulp.lpSum(
        distance[i][j] * x[i][j] for i in Warehouses for j in Customers
    ) + pulp.lpSum(setup_cost[i] * y[i] for i in Warehouses)
    # plp += z

    # epsilon constraint
    # plp += z <= 296

    # add constraints
    for j in Customers:
        plp += pulp.lpSum(x[i][j] for i in Warehouses) == 1

    # plp+=pulp.lpSum(y[i] for i in Warehouses)==MaxWarehousesP

    ##    for j in Customers:
    ##        for i in Warehouses:
    ##            plp += x[i][j] <= y[i]

    for i in Warehouses:
        plp += pulp.lpSum(x[i][j] * demand[j] for j in Customers) <= y[i] * capacity[i]

    for j in Customers:
        plp += pulp.lpSum(x[i][j] * distance[i][j] for i in Warehouses) <= z

    # for lexicographic optimization
    # plp+=(pulp.lpSum(distance[i][j] * x[i][j] for i in Warehouses for j in Customers )+pulp.lpSum(setup_cost[i]* y[i] for i in Warehouses))<=25166
    # optional: generate an lp file
    plp.writeLP("warehouseLocation.lp")

    # solve with default solver
    default_solver = pulp.getSolver("PULP_CBC_CMD")
    default_solver.msg = False
    plp.solve(default_solver)

    # solution output
    # print(" Status:", pulp.LpStatus[plp.status])
    # print(" objective  value: ", pulp.value(plp.objective))

    for var in plp.variables():
        if var.varValue > 0:
            print(var.name, "=", var.varValue)

    # total distance:
    tot_cost = 0
    for i in Warehouses:
        if y[i].value() > 0:
            tot_cost += setup_cost[i]
            for j in Customers:
                print(tot_cost, setup_cost[i])
                if x[i][j].value() > 0:
                    tot_cost += distance[i][j]
                    print(distance[i][j])

    max_dist = 0
    for i in Warehouses:
        for j in Customers:
            if x[i][j].value() > 0:
                if distance[i][j] > max_dist:
                    max_dist = distance[i][j]

    result = []
    iteration = 0
    while max_dist > 0:
        iteration += 1
        epsilon = max_dist - 1
        plp += z <= epsilon
        plp.solve(default_solver)
        if pulp.LpStatus[plp.status] != "Optimal":
            break
        tot_cost = 0
        for i in Warehouses:
            if y[i].value() > 0:
                tot_cost += setup_cost[i]
                for j in Customers:
                    print(tot_cost, setup_cost[i])
                    if x[i][j].value() > 0:
                        tot_cost += distance[i][j]
                        print(distance[i][j])

        max_dist = 0
        for i in Warehouses:
            for j in Customers:
                if x[i][j].value() > 0:
                    if distance[i][j] > max_dist:
                        max_dist = distance[i][j]
        result.append(
            {
                "iteration": iteration,
                "epsilon": epsilon,
                "totalCost": tot_cost,
                "maxDistance": max_dist,
            }
        )

    # print("total cost", tot_cost)
    # print("max distance", max_dist)
    print(result)

    plot_x_y(
        [entry["totalCost"] for entry in result],
        [entry["maxDistance"] for entry in result],
        "Total Cost",
        "Max Distance",
        "Epsilon results",
    )


problem5()


# %%
def MilatogPart1() -> None:
    FarmsDemand = {"F1": 36, "F2": 42, "F3": 34, "F4": 50, "F5": 27, "F6": 30, "F7": 43}
    SitesThroughput = {1: 80, 2: 90, 3: 110, 4: 120, 5: 100, 6: 120}

    # Import excel files
    filename = "Milatog.xlsx"
    fixedCostsExcel = pd.read_excel(filename, sheet_name="fixedCost", index_col=0)
    dm_df = pd.read_excel("Milatog.xlsx", sheet_name="DistanceMatrix", index_col=0)
    dem_df = pd.read_excel("Milatog.xlsx", sheet_name="Demand", index_col=0).squeeze(
        "columns"
    )
    transportationCost = 0.06
    # DataFrame for the assignment cost
    # index_col =0 means that column 0 is used as row label

    # Series for the opening cost
    # squeeze=: If the parsed data only contains one column then return a Series

    assignment_cost = dm_df.to_dict(orient="index")

    # loc_data=fixedCostsExcel.to_dict(orient="dict")

    fixed_cost = fixedCostsExcel["Fixed cost for four years (€)"].to_dict()
    # for key in fixed_cost:
    #     fixed_cost[key] = fixed_cost[key] / (365 * 3 + 366)

    capacity = fixedCostsExcel["Forage throughtput (q/g)"].to_dict()

    demand = dem_df.to_dict()
    rc = fixedCostsExcel["Running cost (€/q)"].to_dict()

    for key_i in assignment_cost:
        for key_j in assignment_cost[key_i]:
            # print(assignment_cost[key_i][key_j])
            assignment_cost[key_i][key_j] = (
                transportationCost * 2 * assignment_cost[key_i][key_j] * demand[key_j]
                + demand[key_j] * rc[key_i]
            )

    potFacilities = dm_df.index.tolist()

    # taken from columns label
    demandPoints = dm_df.columns.tolist()

    operation_running_time = 365 * 4 + 1

    plp = pulp.LpProblem("Milatog 1", pulp.LpMinimize)

    # variables
    y = pulp.LpVariable.dicts("y", (potFacilities), 0, 1, pulp.LpBinary)
    x = pulp.LpVariable.dicts(
        "x", (potFacilities, demandPoints), 0, 1, pulp.LpContinuous
    )

    fixed_cost_objective = pulp.lpSum(fixed_cost[i] * y[i] for i in potFacilities)
    assignment_cost_objective = pulp.lpSum(
        operation_running_time * assignment_cost[i][j] * x[i][j]
        for i in potFacilities
        for j in demandPoints
    )

    # Objective function
    plp += fixed_cost_objective + assignment_cost_objective

    # add constraints
    ## Satisfy demand
    for i in demandPoints:
        plp += pulp.lpSum(capacity[j] * x[i][j] for j in potFacilities) == demand

    # for lexicographic optimization
    # plp+=(pulp.lpSum(distance[i][j] * x[i][j] for i in Warehouses for j in Customers )+pulp.lpSum(setup_cost[i]* y[i] for i in Warehouses))<=25166
    # optional: generate an lp file
    plp.writeLP("Milatog1.lp")

    # solve with default solver
    default_solver = pulp.getSolver("PULP_CBC_CMD")
    default_solver.msg = False
    plp.solve(default_solver)

    print(" Status:", pulp.LpStatus[plp.status])
    print(" objective value: ", pulp.value(plp.objective))


MilatogPart1()

# %%
