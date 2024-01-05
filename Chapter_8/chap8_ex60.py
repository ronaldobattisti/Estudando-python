def subs(text):
    buffer = []
    if ' ' in text:
        buffer = text.split(' ')
        return buffer[0]
    return -1

str1 = 'Test string with space'
str2 = 'Test_string_WO_space'

print(subs(str1))
print(subs(str2))