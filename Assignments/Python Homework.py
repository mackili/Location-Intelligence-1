# %%
import pulp
import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go
import numpy as np

random.seed(1)

floors = 7
rows = 20
columns = 7
num_points = 200
floor_height = 3
row_length = 1.5
column_width = 2.5
random_generated_ap_locations = False
# Distance threshold necessary for good signal (in centimeters)
S = 750


def plot_solution(
    access_points: dict, desks: dict, chosen_access_point_keys: list
) -> None:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot access points
    not_chosen_access_points = {
        key: access_points[key]
        for key in access_points
        if key not in chosen_access_point_keys
    }
    ap_xs = [ap["row"] for ap in not_chosen_access_points.values()]
    ap_ys = [ap["column"] for ap in not_chosen_access_points.values()]
    ap_zs = [ap["floor"] for ap in not_chosen_access_points.values()]
    ax.scatter(ap_xs, ap_ys, ap_zs, c="r", marker="o", label="Unutilized Points", s=1)

    # Plot desks
    desk_xs = [desk["row"] for desk in desks.values()]
    desk_ys = [desk["column"] for desk in desks.values()]
    desk_zs = [desk["floor"] for desk in desks.values()]
    ax.scatter(desk_xs, desk_ys, desk_zs, c="b", marker="s", label="Desks", s=1)

    # Highlight chosen access points
    chosen_access_points = {key: access_points[key] for key in chosen_access_point_keys}
    chosen_ap_xs = [ap["row"] for ap in chosen_access_points.values()]
    chosen_ap_ys = [ap["column"] for ap in chosen_access_points.values()]
    chosen_ap_zs = [ap["floor"] for ap in chosen_access_points.values()]
    ax.scatter(
        chosen_ap_xs,
        chosen_ap_ys,
        chosen_ap_zs,
        c="g",
        marker="o",
        label="Chosen Access Points",
        s=40,
    )

    ax.set_xlabel("Row")
    ax.set_ylabel("Column")
    ax.set_zlabel("Floor")
    ax.legend()

    plt.savefig("assignments/access_point_plot.svg")
    plt.show()


def plot_solution_interactive(
    access_points: dict, desks: dict, chosen_access_point_keys: list
) -> None:
    fig = go.Figure()

    # Plot access points excluding the chosen ones
    not_chosen_access_points = {
        key: access_points[key]
        for key in access_points
        if key not in chosen_access_point_keys
    }
    not_chosen_ap_xs = [ap["row"] for ap in not_chosen_access_points.values()]
    not_chosen_ap_ys = [ap["column"] for ap in not_chosen_access_points.values()]
    not_chosen_ap_zs = [ap["floor"] for ap in not_chosen_access_points.values()]
    fig.add_trace(
        go.Scatter3d(
            x=not_chosen_ap_xs,
            y=not_chosen_ap_ys,
            z=not_chosen_ap_zs,
            mode="markers",
            marker=dict(size=1, color="red"),
            name="Unutilized Points",
        )
    )

    # Plot desks
    desk_xs = [desk["row"] for desk in desks.values()]
    desk_ys = [desk["column"] for desk in desks.values()]
    desk_zs = [desk["floor"] for desk in desks.values()]
    fig.add_trace(
        go.Scatter3d(
            x=desk_xs,
            y=desk_ys,
            z=desk_zs,
            mode="markers",
            marker=dict(size=2, color="blue"),
            name="Desks",
        )
    )

    # Highlight chosen access points
    chosen_access_points = {key: access_points[key] for key in chosen_access_point_keys}
    chosen_ap_xs = [ap["row"] for ap in chosen_access_points.values()]
    chosen_ap_ys = [ap["column"] for ap in chosen_access_points.values()]
    chosen_ap_zs = [ap["floor"] for ap in chosen_access_points.values()]
    fig.add_trace(
        go.Scatter3d(
            x=chosen_ap_xs,
            y=chosen_ap_ys,
            z=chosen_ap_zs,
            mode="markers",
            marker=dict(size=6, color="green"),
            name="Chosen Access Points",
        )
    )

    fig.update_layout(
        scene=dict(xaxis_title="Row", yaxis_title="Column", zaxis_title="Floor")
    )

    fig.write_html(
        "assignments/access_point_plot.html", full_html=False, include_plotlyjs="cdn"
    )


def calculate_distance(desk, access_point) -> float:
    # Extract coordinates
    desk_row, desk_column, desk_floor = desk["row"], desk["column"], desk["floor"]
    ap_row, ap_column, ap_floor = (
        access_point["row"],
        access_point["column"],
        access_point["floor"],
    )

    # Calculate Euclidean distance
    distance = math.ceil(
        math.sqrt(
            ((desk_row - ap_row) * row_length) ** 2
            + ((desk_column - ap_column) * column_width) ** 2
            + ((desk_floor - ap_floor) * floor_height) ** 2
        )
        * 100
    )
    return distance


def generate_desk_locations(floors=floors, rows=rows, columns=columns) -> dict:
    desk_locations = {}
    for floor in range(1, floors + 1):
        for row in range(1, rows + 1):
            for column in range(1, columns + 1):
                desk_id = f"{row}-{column}-{floor}"
                desk_locations[desk_id] = {"row": row, "column": column, "floor": floor}
    return desk_locations


def generate_access_points(
    num_points=num_points,
    floors=floors,
    rows=rows,
    columns=columns,
    random_locations=random_generated_ap_locations,
) -> dict:
    access_points = {}
    if random_locations:
        for i in range(1, num_points + 1):
            floor = random.randint(1, floors) + 0.8
            row = random.randint(1, rows) + (random.random() - 1)
            column = random.randint(1, columns) + (random.random() - 1)
            access_point_id = f"AP-{i}"
            access_points[access_point_id] = {
                "row": row,
                "column": column,
                "floor": floor,
            }
    else:
        for floor in range(1, floors + 1):
            for row in range(1, rows + 1):
                for column in range(1, columns + 1):
                    access_point_id = f"AP-{floor}-{row}-{column}"
                    access_points[access_point_id] = {
                        "row": row,
                        "column": column,
                        "floor": floor + 0.8,
                    }
    return access_points


def calculate_distances(desk_locations: dict, access_point_locations: dict) -> dict:
    distances = {}
    for ap_id, ap_location in access_point_locations.items():
        distances[ap_id] = {}
        for desk_id, desk_location in desk_locations.items():
            distance = calculate_distance(desk_location, ap_location)
            distances[ap_id][desk_id] = distance
    return distances


def problem() -> None:
    # We want to maximize WiFi coverage in an office. We want to buy as few hotspots as possible,
    # while having the best possible coverage. The office has 3 floors, with 30 desks on each floor.
    # Their places are generated as [row, column, floor]. The names are corresponding: 'row-column-floor'.
    # Defining desks
    desk_locations = generate_desk_locations()
    desks = desk_locations.keys()
    # Defining demand points
    access_point_locations = generate_access_points()
    access_points = access_point_locations.keys()

    # response time/distance from facility i to demand point j
    distance_matrix = calculate_distances(desk_locations, access_point_locations)

    # is distance within a threshold
    a = {
        i: {j: 1 if distance_matrix[i][j] <= S else 0 for j in desks}
        for i in access_points
    }

    plp = pulp.LpProblem("AssignmentProblem", pulp.LpMinimize)

    # Declaring variables
    y = pulp.LpVariable.dicts("y", (access_points), 0, 1, pulp.LpBinary)
    # a = pulp.LpVariable.dicts("a", (access_points, desks), 0, 1, pulp.LpBinary)

    # Adding objective function
    plp += pulp.lpSum(y[i] for i in access_points)

    # Constraints
    for j in desks:
        plp += pulp.lpSum(a[i][j] * y[i] for i in access_points) >= 1

    # Create an LP File that shows the model that was created in a certain format.
    # It can be helpful for debugging for instance.
    plp.writeLP("AssignmentProblem.pl")

    # Solve the model with the default solver (CBC)
    plp.solve()

    print(" Status:", pulp.LpStatus[plp.status])
    print(" objective value: ", pulp.value(plp.objective))
    chosen_access_points = [i for i in access_points if pulp.value(y[i]) == 1]
    print(chosen_access_points)
    plot_solution(access_point_locations, desk_locations, chosen_access_points)
    plot_solution_interactive(
        access_point_locations, desk_locations, chosen_access_points
    )


problem()
