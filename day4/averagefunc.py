def average(*args):
    if len(args) == 0:
        return "No marks provided"

    return sum(args) / len(args)

print(average(80, 90, 70))
print(average(50, 60))
print(average())