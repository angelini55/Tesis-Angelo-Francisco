selected_dropdown_option = "Rr"  #  Value to get from the interface
reference_value = 0.3            #  Value to get from the interface

database_dict = {
    "alpha": [],
    "beta": [],
    "Rr": [],
    "alpha_diff": [],
    "beta_diff": [],
    "Rr_diff": []
}

#  Connect to database to get this
table_data = [(0.5, 0.938, 1.875), (0.4, 0.947, 1.578), (0.3, 0.957, 1.367), (0.2, 0.969, 1.212), (0.1, 0.983, 1.093), (0, 1, 1)]

for Rr, alpha, beta in table_data:
    database_dict["alpha"].append(alpha)
    database_dict["beta"].append(beta)
    database_dict["Rr"].append(Rr)
    database_dict["alpha_diff"].append((alpha - reference_value) if (alpha - reference_value) >= 0 else (alpha - reference_value) * (-1))
    database_dict["beta_diff"].append((beta - reference_value) if (beta - reference_value) >= 0 else (beta - reference_value) * (-1))
    database_dict["Rr_diff"].append((Rr - reference_value) if (Rr - reference_value) >= 0 else (Rr - reference_value) * (-1))


if (reference_value >= min(database_dict[selected_dropdown_option])) and (reference_value <= max(database_dict[selected_dropdown_option])):

    interpolation_indexes = []
    i = 0
    while i <= 1:
        value = min(database_dict[selected_dropdown_option + "_diff"])
        index = database_dict[selected_dropdown_option + "_diff"].index(value)
        interpolation_indexes.append(index)
        database_dict[selected_dropdown_option + "_diff"][index] += 100
        i += 1

    parameters_for_interpolation = [key for key in database_dict.keys() if ((selected_dropdown_option not in key) and ("diff" not in key))]

    interpolation_results = {}
    i0, i1 = interpolation_indexes
    for parameter in parameters_for_interpolation:

        #  Interpolation Equation: y = y0 + (x-x0)*((y1-y0)/(x1-x0))
        interpolation_results[parameter] = database_dict[parameter][i0] + (
            reference_value - database_dict[selected_dropdown_option][i0]) * (
                (database_dict[parameter][i1] - database_dict[parameter][i0]) / (
                    database_dict[selected_dropdown_option][i1] - database_dict[selected_dropdown_option][i0]))

    print(interpolation_results)

else:
    raise Exception("Value out of range")