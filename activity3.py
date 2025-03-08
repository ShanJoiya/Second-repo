def test(lst):
    result = {}
    for item in lst:
        result[item[0]] = item[1:]
    return result    
students = [[1, 'Jean Castro', 'v'], [2, 'Lula Powell', 'V']]


print("\nOrignal List of Lists:")
print(students)
print("\Converted List to a dictionary:")
print(test(students))