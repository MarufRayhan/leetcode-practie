def pair_sum(numbers, target_sum):
    previous_value = {}
    for idx, number in enumerate(numbers):
        complement = target_sum - number
 
        
        if complement in previous_value:
            print(f"Found complement {complement} at index {previous_value[complement]}")
            print(f"previous_value[complement] = {previous_value[complement]}")
            return (previous_value[complement], idx)
        
        previous_value[number] = idx  # Store AFTER checking
        print(f"Stored {number} at index {idx}")
        print("---")

pair_sum([3, 2, 5, 4, 1], 8)