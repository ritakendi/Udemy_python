def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return f"min:{ maximum}\nmax:{minimum}"


print(get_max())
