numbers = [10, 2, 4, 5, 1, 29]

print(sum(numbers))

print(max(numbers))

new_numbers = [1, 20, 4, 6, 7]

new_numbers.sort()
print(new_numbers[-1])


test = [1, 3, 5, 2, 8]
temp = 0
for i in test:
    if i > temp:
        temp = i

print(temp)
