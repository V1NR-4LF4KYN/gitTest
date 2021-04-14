s = "Hello World"
arr = []

for letter in s:
    arr.append(letter)

arr = arr[::-1]

r = ''
for item in arr:
    r += item


print(r)

