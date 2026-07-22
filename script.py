def print_numbers():
    """Print numbers from 1 to 100, replacing multiples of 3 with 'fizz'"""
    result = []
    for i in range(1, 101):
        if i % 3 == 0:
            result.append("fizz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    output = print_numbers()
    print(output)
