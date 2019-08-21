# Excessively short identifiers
def x(y, z):
    return y * z


# Excessively long identifiers
def my_name_is_grayson_orr_how_are_you_today():
    return 'Grayson, how are you today?'


# Embedding types in identifiers
def embedding_types():
    list_of_names = ['Grayson', 'John', 'Jane']
    return list_of_names


# Cyclomatic complexity
def cyclomatic_complexity(n):
    if (n == 0):
        return 'Zero'
    elif (n == 1):
        return 'One'
    elif (n == 2):
        return 'Two'
    elif (n == 3):
        return 'Three'
    elif (n == 4):
        return 'Four'
    else:
        return 'N/A'


def refactor_cyclomatic_complexity(n):
    num = ['Zero', 'One', 'Two', 'Three', 'Four']
    if ((n >= 0) and (n <= 4)):
        return num[n]
    else:
        return 'N/A'

print(cyclomatic_complexity(5))
print(refactor_cyclomatic_complexity(3))

