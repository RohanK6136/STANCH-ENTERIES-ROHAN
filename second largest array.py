def second_largest_distinct(arr):
    if not arr or len(arr) < 2:
        return -1
    
    first = float('-inf')
    second = float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else -1
print(second_largest_distinct([1, 2, 3, 4, 5])) 