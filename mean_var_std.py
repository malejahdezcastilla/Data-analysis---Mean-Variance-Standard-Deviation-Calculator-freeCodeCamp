import numpy as np

def calculate (list) :
    if len (list) == 9 :
        initial_array = np.array (list)
        reshaped_array = initial_array.reshape (3,3)
        mean_array_column= np.mean (reshaped_array, axis = 0).tolist ()
        mean_array_row= np.mean (reshaped_array, axis = 1).tolist ()
        mean_array_flattened = np.mean (reshaped_array).tolist ()

        var_array_column= np.var (reshaped_array, axis = 0).tolist ()
        var_array_row= np.var (reshaped_array, axis = 1).tolist ()
        var_array_flattened = np.var (reshaped_array).tolist ()

        std_array_column= np.std (reshaped_array, axis = 0).tolist ()
        std_array_row= np.std (reshaped_array, axis = 1).tolist ()
        std_array_flattened = np.std (reshaped_array).tolist ()

        max_array_column= np.max (reshaped_array, axis = 0).tolist ()
        max_array_row= np.max (reshaped_array, axis = 1).tolist ()
        max_array_flattened = np.max (reshaped_array).tolist ()

        min_array_column= np.min (reshaped_array, axis = 0).tolist ()
        min_array_row= np.min (reshaped_array, axis = 1).tolist ()
        min_array_flattened = np.min (reshaped_array).tolist ()

        sum_array_column= np.sum (reshaped_array, axis = 0).tolist ()
        sum_array_row= np.sum (reshaped_array, axis = 1).tolist ()
        sum_array_flattened = np.sum (reshaped_array).tolist ()


        calculations = {
        'mean': [mean_array_column, mean_array_row, mean_array_flattened],
        'variance': [var_array_column, var_array_row,var_array_flattened],
        'standard deviation': [std_array_column, std_array_row, std_array_flattened],
        'max': [max_array_column, max_array_row, max_array_flattened],
        'min': [min_array_column, min_array_row, min_array_flattened],
        'sum': [sum_array_column, sum_array_row, sum_array_flattened]
        }
        return calculations
    else :
        raise ValueError ('List must contain nine numbers.')