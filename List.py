# 1. Create a List
numbers = [10, 20, 30, 40, 50]
print(numbers)

# 2. Access Elements
numbers = [10, 20, 30, 40]
print(numbers[0])
print(numbers[-1]

      # 3. Add Elements
numbers = [1, 2, 3]
numbers.append(4)
numbers.insert(1, 100)
print(numbers)

# 4. Extend List
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

# 5. Remove Elements
numbers = [10, 20, 30, 40]
numbers.remove(20)
numbers.pop()
del numbers[0]
print(numbers)

# 6. Find Length
numbers = [1, 2, 3, 4, 5]
print(len(numbers))

# 7. Sum of List
numbers = [10, 20, 30]
print(sum(numbers))

# 8. Maximum and Minimum
numbers = [5, 2, 8, 1]
print(max(numbers))
print(min(numbers))

# 9. Sort List
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)


# Descending
numbers.sort(reverse=True)
print(numbers)

# 10. Reverse List
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)

# 11. Copy List
a = [1, 2, 3]
b = a.copy()
print(b)

# 12. Count Occurrences
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))


# 13. Find Index
numbers = [10, 20, 30]
print(numbers.index(20))

# 14. Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)

# 15. Merge Two Lists
a = [1, 2]
b = [3, 4]
print(a + b)

# 16. Nested List
matrix = [
    [1, 2],
    [3, 4]
]
print(matrix[1][0])

# 17. List Comprehension
square = [x*x for x in range(1, 6)]
print(square)

# 18. Even Numbers
numbers = [1, 2, 3, 4, 5, 6]
even = [x for x in numbers if x % 2 == 0]
print(even)

# 19. Largest Element Without max()
numbers = [12, 45, 7, 89, 23]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print(largest)


# 20. Smallest Element Without min()
numbers = [12, 45, 7, 89, 23]

smallest = numbers[0]

for i in numbers:
    if i < smallest:
        smallest = i

print(smallest)
