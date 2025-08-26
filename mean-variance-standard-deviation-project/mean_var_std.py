import numpy as np

def calculate(list_of_numbers):

    if len(list_of_numbers) != 9:
        raise ValueError("List must contain nine numbers.")


    arr = np.array(list_of_numbers).reshape(3, 3)

    results = {}

    calculations = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum
    }


    for stat_name, stat_func in calculations.items():
        results[stat_name] = [stat_func(arr, axis=0).tolist(), stat_func(arr, axis=1).tolist(), stat_func(arr).tolist()]

    for stat_name in results:
        flattened_val = results[stat_name][2]
        if isinstance(flattened_val, list) and len(flattened_val) == 1:
            calculations[stat_name][2] = flattened_val[0]

    return results
