from file import write_to_file, read_from_file
from solver import solve_all_numbers


def main():
    # If you provide a txt file to read_from_file() it will read from that txt
    int_numbers = read_from_file()

    results = solve_all_numbers(int_numbers)

    write_to_file(results)


if __name__ == "__main__":
    main()
