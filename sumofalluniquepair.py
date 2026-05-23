def find_pairs(arr, target):
    if not arr or len(arr) < 2:
        return []
    
    # Sort the array
    arr = sorted(arr)
    result = []
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            # Add the pair (already sorted because array is sorted)
            result.append([arr[left], arr[right]])
            
            # Move both pointers
            left += 1
            right -= 1
            
            # Skip duplicates for left
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            # Skip duplicates for right
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
                
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return result


if __name__ == "__main__":
    print("=== Find All Unique Pairs with Target Sum ===\n")
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 5),
        ([2, 7, 11, 15], 9),
        ([1, 1, 2, 3], 4),
        ([3, 3, 3], 6),
        ([1, 2, 3], 10),
        ([1, 5, 1, 5], 6),
        ([-1, -2, 3, 5, -3], 2)
    ]
    
    for arr, target in test_cases:
        result = find_pairs(arr, target)
        print(f"Input: arr={arr}, target={target}")
        print(f"Output: {result}\n")