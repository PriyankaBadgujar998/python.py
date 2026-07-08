# text = input("Enter a string: ")
# count = 0
# i = 0
# while i < len(text):
#     ch = text[i].lower()
#     if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
#          count = count + 1
#     i = i + 1

# print(count)



text = input("Enter a string: ")
result = ""
i = 0
while i < len(text):
    ch = text[i]
    if ch.isupper():
        result = result + ch.lower()
    elif ch.islower():
        result = result + ch.upper()
    else:
        result = result + ch
    i = i + 1
print(result)