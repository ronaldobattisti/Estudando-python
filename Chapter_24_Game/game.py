from models.calculate import Calculate


def main() -> None:
    points: int = 0
    play(points)


def play(point: int) -> None:
    difficulty: int = int(input("Input the difficult level(1, 2, 3 or 4): "))

    calc: Calculate = Calculate(difficulty)
    print('Input the answer for the following operation: ')
    calc.show_operation()
    result: int = int(input())

    if calc.check_answer(result):
        point += 1
        print(f"You have {point} points")

    contin: bool = bool(input("Want to continue? [1 - yes | 0 - no]"))

    if contin:
        play(point)
    else:
        print('You end with {points} points')


if __name__ == '__main__':
    main()
