def sum_of_series(n):
    if n<1:
        return 0
    else:

        return n+sum_of_series(n-2)
print(sum_of_series(10))