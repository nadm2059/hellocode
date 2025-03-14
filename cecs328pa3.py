# Name: [Your Name]
# CECS 328 - Programming Assignment 3
# Filename: cecs328pa3.py
def cargo(crates, T, W, D):
    """
    Determines the maximum number of crates that can be transported without exceeding 
    the limits on toasters (T), washers (W), and dryers (D).

    Args:
    crates (list): List of strings, where each string represents a crate containing 't' (toaster), 
                   'w' (washer), and 'd' (dryer).
    T (int): Maximum number of toasters allowed.
    W (int): Maximum number of washers allowed.
    D (int): Maximum number of dryers allowed.

    Returns:
    int: Maximum number of crates that can be selected without exceeding the given limits.
    """

    # Sort crates based on their total number of items using a basic selection sort.
    # This ensures we prioritize smaller crates first to maximize the number of crates we can take.
    for i in range(len(crates)):  # Iterate over each crate
        for j in range(i + 1, len(crates)):  # Compare with remaining crates
            # Count total items (toasters, washers, and dryers) in both crates
            count_i = crates[i].count('t') + crates[i].count('w') + crates[i].count('d')
            count_j = crates[j].count('t') + crates[j].count('w') + crates[j].count('d')

            # Swap if the later crate has fewer total items
            if count_i > count_j:
                crates[i], crates[j] = crates[j], crates[i]

    # Initialize counters for the number of toasters, washers, and dryers currently selected
    t_count = 0  # Current count of toasters in selected crates
    w_count = 0  # Current count of washers in selected crates
    d_count = 0  # Current count of dryers in selected crates

    # Initialize the maximum number of crates that can be selected
    max_length = 0  

    # Iterate through the sorted crates and add them one by one if they fit within the limits
    for crate in crates:
        # Compute the new total after adding this crate
        new_t = t_count + crate.count('t')  # New toaster count
        new_w = w_count + crate.count('w')  # New washer count
        new_d = d_count + crate.count('d')  # New dryer count

        # Check if adding this crate exceeds the allowed limits
        if new_t > T or new_w > W or new_d > D:
            continue  # Skip this crate if it exceeds any limit

        # If valid, update the current counts to include this crate
        t_count, w_count, d_count = new_t, new_w, new_d  

        # Increase the count of selected crates
        max_length += 1  

    # Return the maximum number of crates that can be transported within limits
    return max_length



print(cargo(["d"],21,22,23))
print(cargo(["d"],1,1,1))
print(cargo(["tttt", "wwww", "dddd"], 1, 1, 1))  # Expected: 0 (all exceed limits)
print(cargo(["twd"], 0, 0, 0))  # Expected: 0 (no capacity for any items)

print(cargo(['twwddwwdtdtdddddwwwtwtttdddwwtdwt', 'td', 'wddddwwwwwttwwdwdtddwttdww',
     'ddtttwwwwwwwtttwwdwdwwttdwtwdwwtdwt', 'wtt', 'ttdtdtdddwtdtwtwwtwtwwwdwwwtdddtwtd',
     'dwwtwtdwddddt', 'twtttw', 'ddttdwwttdtwwdwtddddddwttdddwdtwwwddwddtdw', 'ddtdddttt',
     'wttdttdddwdttwtww', 't', 'ttwttdtwdtwwd', 'wdtwdwdttdwwdwdwtwtt',
     'twwwdtttttdwttdttdtdwdwdwwtwdttwwddt', 'dwtwtwwttdtdwwdwddttwtwwtwtwttdwdtwtwtddwdttt',
     'twtwdddttwtwtdwwwddwdttwwwtddwdtwtdddwd',
     'wtttwwtwwwdwddwtddwwwwdwttwwdttdtdwttw', 'twtwdddtwddttttddwtddwwtddtwdwtt',
     'wtdwwwddtttwtddtdwwdwwwdtddd', 'wwwt', 'ddtttwwdw', 'ttdwwwwwwwdddttttddwwd', 'd',
     'dwwwwddwwdddtwtwdttwtdw', 'tddddtwtttwttttt',
     'dtwwtdwtddddwdddwwwdwwwwwdtdddtdwwdtdddwtd', 'wdttwwwtwtwt',
     'tdtwwwwwwtwttdtwdddd', 'dwwwddwddddtttwdwtdwttdtdtdtd',
     'wwdtddtdwdtdwwtdttddwttdwwtwwtwdtwttwwwddtddt',
     'wtdddtttwdtdddwwtddtdwdtdwwdtwttdddwtwtwtttdtdwtd',
     'wdwdddtdddtddtdwtdtdtwwttwtwwwwwtdddwwdddwdtwwt',
     'wdwtdwttdddwwwwtwdddtdtdwdtwwddttt', 'dtddtttwdtw', 'dwwddwwdwtdwd',
     'twwtdwdwtwtttwddwttdwtddwtdwwttwddwwtdtttdttddt', 'ttwtwddtwdwdt',
     'wdwwdddddtwdwwddwdtttwwttdwdwttdwttddttwtdww', 'tddddwwtdwddd',
     'dtwwdttdttdwwwtdtdwtwwwdwdddtdd', 'twwwddwtdtdttddtwdtwtdtd',
     'ttttwtdwwwtddwdwddwdwdwdwtwtdtwddttw', 'dwddtdwwwtdwwwtddtwdtdddtwtdww',
     'dwdwwtwwdddttdwdwtw', 'wwwtwdddwdtddwddddddwddttdwwt', 'wtttttttddwwtdwdtd',
     'dwwwddwttwdwtwddtdwddtdddddwddddwwddwdt', 'dwwwwwdttdtwtwwtttdddwwtwtwwwdt',
     'wdtwtwdwtttwddtwdwwwwwddddddtwdwttw'],20,20,20))
print(cargo(["tdwwddt", "t", "dwww", "ddww", "wwww"], 3, 5, 4))  # Expected: 3
print(cargo(["dwtd", "td", "td", "ddd", "www"], 2, 1, 1))  # Expected: 1
print(cargo(["d", "t", "w", "wdw", "tdt"], 2, 1, 2))  # Expected: 3
print(cargo(["tt", "ww", "dd"], 2, 2, 2))  # Expected: 3 (all fit exactly)
print(cargo(["tw", "wd", "dt"], 3, 3, 3))  # Expected: 3 (all fit within limits)
print(cargo(["ttt", "w", "d", "tw"], 3, 1, 1))  # Expected: 2 (either "ttt" or "tw" + "w")
crates_large = ["twd" * 16] * 50  # 50 crates, each containing "twd" repeated 16 times
print(cargo(crates_large, 50, 50, 50))  # Expected: should not exceed 5-second limit
print(cargo(["t"] * 50, 50, 0, 0))  # Expected: 50 (since we can take all toasters)
print(cargo(["t"] * 50, 49, 0, 0))  # Expected: 49 (since we must leave 1 out)
print(cargo(["t" * 50, "t", "t", "t"], 5, 0, 0))  # Expected: 3 (better to take small ones)
print(cargo(["t" * 50, "t" * 5], 50, 0, 0))  # Expected: 1 (can only take one crate)
