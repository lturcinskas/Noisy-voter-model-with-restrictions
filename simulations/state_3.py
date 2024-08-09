import numpy as np
import typer
from typing import List
from typing_extensions import Annotated
from Gillespie_method import get_series
from unique_file import unique_file


def main(
        epsilon: float,
        n_steps: int,
        time_step: float,
        initial_condition: Annotated[List[int], typer.Option()] = [],
) -> None:
    """
        Input:
            epsilon - rate of spontaneous opinion switch.
            n_steps - number of steps; length of simulation.
            time_step - time step between observations.
            initial_condition - initial distribution of opinions.
        Output:
            None. Function saves file with array of observed values.
    """
    restrictions = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    result = get_series(initial_condition, time_step, n_steps, restrictions, epsilon)

    data_name = unique_file(f"3_data_{epsilon}", "txt")

    np.savetxt(data_name, result, fmt="%.4f", delimiter=",",
               header=f" epsilon = {epsilon}, time_step = {time_step}, n_steps = {n_steps}, "
                      f"restrictions = {restrictions}")
