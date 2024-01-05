notes = []
count = 0
while count < 10:
    notes.append(int(input(f'Write the {count + 1}° number:')))
    count += 1

print(notes)

quant_neg = 0
sum_pos = 0

for i in notes:
    if i > 0:
        sum_pos += i
    elif i < 0:
        quant_neg += 1

print(quant_neg)
print(sum_pos)