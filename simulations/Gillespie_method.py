import random
from typing import List


def get_rates(
        X: List[int],
        restrictions:  list[list[int]],
        epsilon: float,
):
    """  Calculates the transitions rates of each opinion.
        Input:
            X - opinion vector.
            restrictions - array of restrictions, 1  meaning that "communication" is restricted.
            epsilon - rate of spontaneous opinion switch.

        Output:
            Array with specific rates as well as total_rate that is the sum of all the rates.
        """
    opinions = len(X)
    rates = [[0 for _ in range(opinions)] for _ in range(opinions)]
    total_rate = 0
    for i in range(opinions):
        for j in range(opinions):
            if i != j and restrictions[i][j] == 0:
                rates[i][j] = X[i] * (epsilon + X[j])
                total_rate += rates[i][j]

    return rates, total_rate


def find_next_event(
        rates:  list[list[float]],
        total_rate: float,
):
    """ Determines which event happens next.
        Input:
            rates - array of rates for specific events.
            total_rate - total rate of all events.
        Output:
            coordinates of the next event.
        """
    target = random.uniform(0, total_rate)
    current_sum = 0

    for row_index, row in enumerate(rates):
        for column_index, column in enumerate(row):
            current_sum += column
            if current_sum >= target:
                return row_index, column_index


def get_series(
        X: List[int],
        time_step: float,
        n_steps: int,
        restrictions:  list[list[int]],
        epsilon: float,
):
    """ Generates series with observed values.
        Input:
            X - opinion vector.
            time_step - time step between observations.
            n_steps - number of steps; length of simulation.
            restrictions - array of restrictions.
            epsilon - rate of spontaneous opinion switch.
        Output:
            Array with observed values at each time step.
        """

    # Set parameters
    current_time = 0
    series = [[0 for _ in range(len(X))] for _ in range(n_steps + 1)]

    for i in range(len(X)):
        series[0][i] = X[i]

    step_idx = 1
    observation_time = step_idx * time_step

    # Get initial rates
    all_rates, total_rate = get_rates(X, restrictions, epsilon)

    tau = random.expovariate(total_rate)

    while step_idx <= n_steps:
        while current_time + tau < observation_time:
            current_time += tau
            curr_row, curr_column = find_next_event(all_rates, total_rate)
            X[curr_row] -= 1
            X[curr_column] += 1

            all_rates, total_rate = get_rates(X, restrictions, epsilon)
            tau = random.expovariate(float(total_rate))

        while observation_time <= current_time + tau:
            for i in range(len(X)):
                series[step_idx][i] = X[i]
            step_idx += 1
            if step_idx > n_steps:
                break
            observation_time = step_idx * time_step
    return series
