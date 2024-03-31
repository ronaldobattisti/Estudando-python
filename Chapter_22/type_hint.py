def greet(name: str) -> str:
    return f"Hello, {name}!"


print(greet('Ronaldo'))


def header(text: str, alignment: bool = True) -> str:
    if alignment:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f"{text.title()}".center(50, '*')


print(header('Ronaldo Battisti', alignment=True))

print(header('Ronaldo Battisti', alignment=True))
