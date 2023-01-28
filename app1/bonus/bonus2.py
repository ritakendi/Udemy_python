def get_average():
    """A function that gets numbers from a text file 
        and returns the average of those numbers
    """
    with open("files/data.txt", 'r') as file:
        data = file.readlines()

    values = data[1:]
    values = [float(i)for i in values]

    average = sum(values) / len(values)
    return average


average = get_average()
print(average)
