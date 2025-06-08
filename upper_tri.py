def upper_triangular(n):
    for i in range(n):
        print("  " * i + "* " * (n - i))

upper_triangular(5)