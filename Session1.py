import random
import pulp


def main() -> None:
    # List of the same type
    fruits = ["apple", "banana", "orange"]
    customers = ["Chicago", "New York"]

    # Print the whole list
    print(fruits)

    # Print just one element
    print(customers[1])

    # JSON-like key-value pair called DICTIONARY
    fixed_cost = {"A": 5, "B": 7, "C": 5, "D": 6, "E": 5}
    print(fixed_cost["B"])

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

    # List 1 to 10
    listOneTen = list(range(1, 11))
    print(listOneTen)

    # Dictionary for stock levels
    stock_levels = {"apple": 50, "banana": 30, "orange": 20, "grape": 15, "mango": 10}
    print(stock_levels)

    # Stock levels for WH1-4 and products 1-3
    stock_levels2 = generate_stock_levels()
    print(stock_levels2)
    print(
        "There are "
        + str(stock_levels2["WH1"]["product1"])
        + " units of product 1 in WH1"
    )
    # create_stock_level_plot(stock_levels=stock_levels2)


def generate_stock_levels() -> dict:
    products = ["product1", "product2", "product3"]
    warehouses = ["WH1", "WH2", "WH3", "WH4"]

    stock_levels = {}
    for warehouse in warehouses:
        stock_levels[warehouse] = {}
        for product in products:
            stock_levels[warehouse][product] = random.randint(
                0, 100
            )  # Initialize stock level to 0

    return stock_levels


def create_stock_level_plot(stock_levels: dict):
    import matplotlib.pyplot as plt
    import numpy as np

    # Extract products and warehouses from the stock_levels dictionary
    warehouses = list(stock_levels.keys())
    products = list(stock_levels[warehouses[0]].keys())

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Define the bar width
    bar_width = 0.2

    # Create an array for the x-axis positions
    x = np.arange(len(warehouses))

    # Plot bars for each product
    for i, product in enumerate(products):
        stock = [stock_levels[warehouse][product] for warehouse in warehouses]
        ax.bar(x + i * bar_width, stock, width=bar_width, label=product)

    # Set the x-axis ticks and labels
    ax.set_xticks(x + bar_width * (len(products) - 1) / 2)
    ax.set_xticklabels(warehouses)
    ax.set_xlabel("Warehouses")
    ax.set_ylabel("Stock Levels")
    ax.set_title("Stock Levels per Product per Warehouse")
    ax.legend()

    # Show the plot
    plt.show()


def problem():
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
    # Declaring a problem
    plp = pulp.LpProblem("Problem_1", pulp.LpMinimize)

    # Declaring variables
    y = pulp.LpVariable.dicts("y", (Warehouses), 0, 1, pulp.LpBinary)
    x = pulp.LpVariable.dicts("x", (Warehouses, Customers), 0, 1, pulp.LpBinary)

    # Adding objective function
    plp += pulp.lpSum(distance[i][j] * x[i][j] for i in Warehouses for j in Customers)

    # Constraints
    # Customer demand must be met
    for j in Customers:
        plp += pulp.lpSum(x[i][j] for i in Warehouses) == 1

    # Use only p warehouses
    plp += pulp.lpSum(y[i] for i in Warehouses) == MaxWarehousesP

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
main()
problem()
