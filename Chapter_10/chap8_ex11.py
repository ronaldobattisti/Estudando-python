notes = []
for ind in range(3):
    notes.append(int(input(f"insert the {ind + 1}º note: ")))

buff = 0

for item in notes:
    buff += item

print(buff/len(notes))