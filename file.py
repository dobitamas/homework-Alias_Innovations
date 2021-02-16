def read_from_file(file_name="input.txt"):
    results = open(file_name).readlines()
    
    return results


def write_to_file(numbers, file_name="output.txt"):
    output = open(file_name, "w+")

    for number in numbers:
        output.write(number + "\r\n")
