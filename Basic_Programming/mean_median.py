def mean_median(array_input):

    mean = sum(array_input) / len(array_input)
    

    n = len(array_input)
    if n % 2 == 1:

        median = array_input[n // 2]
    else:

        median = (array_input[n // 2 - 1] + array_input[n // 2]) / 2
    
    return (mean, median)


print(mean_median([1, 2, 3, 4]))  # outpunya adalah (2.5, 2.5)
print(mean_median([1, 2, 3, 4, 5]))  # outputnya adalah (3.0, 3)
print(mean_median([7, 8, 9, 13, 15]))  # outputnya adalah (10.4, 9)
print(mean_median([10, 20, 30, 40, 50]))  # outputnya adalah (30.0, 30)
print(mean_median([15, 20, 30, 60, 120]))  # outputnya adalah (49.0, 30)
