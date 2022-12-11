# -- Day 1: Calorie Counting ---

def get_puzzle_input(file):
    with open(file, 'r') as reader:
        return reader.readlines()


def get_elves_with_calories(file):
    elf_calories = []
    calories = 0

    for i in get_puzzle_input(file):

        calorie = i.strip('\n')
        if calorie.isdigit():
            calories += int(calorie)
            continue

        elf_calories.append(calories)
        calories = 0
    else:
        elf_calories.append(calories)

    return elf_calories


def part1(file):
    return max(get_elves_with_calories(file))


def part2(file):
    elves_with_calories_sorted = sorted(
        get_elves_with_calories(file),
        reverse=True
    )
    return sum(elves_with_calories_sorted[:3])


if __name__ == "__main__":

    puzzle_input = 'input.txt'
    print(
        f'Puzzle answer 1: {part1(puzzle_input)}',
        f'Puzzle answer 2: {part2(puzzle_input)}',
        sep='\n'
    )
