"""
Consecutive Increasing Numbers
Competitive Programming Solution
"""

def consecutive_increasing_numbers(ch):
    """
    Determines if a string of digits can be split into consecutive increasing numbers.
    
    Args:
        ch: String containing only digits
    
    Returns:
        True if valid split exists, False otherwise
    
    Rules:
    - At least two positive integers
    - Numbers are strictly increasing (each exactly 1 greater than previous)
    - All digits used in order
    - No leading zeros (except for single digit '0')
    
    Time Complexity: O(n²) where n is the length of the string
    Space Complexity: O(n) for storing numbers
    """
    if not ch:
        return False
    
    n = len(ch)
    
    # Try different lengths for the first number
    # First number can be at most half the string length (need at least 2 numbers)
    for first_len in range(1, n):
        # Extract first number
        first_num_str = ch[:first_len]
        
        # Check for leading zeros (except single '0')
        if first_len > 1 and first_num_str[0] == '0':
            continue
        
        first_num = int(first_num_str)
        
        # Try to build consecutive sequence
        if validate_sequence(ch, first_num):
            return True
    
    return False


def validate_sequence(ch, start_num):
    """
    Validates if the string can be split into consecutive numbers starting with start_num.
    
    Args:
        ch: String of digits
        start_num: Starting number of the sequence
    
    Returns:
        True if valid sequence exists, False otherwise
    """
    pos = 0
    current_num = start_num
    count = 0
    
    while pos < len(ch):
        current_str = str(current_num)
        
        # Check if current number matches the string at current position
        if ch[pos:pos + len(current_str)] == current_str:
            pos += len(current_str)
            current_num += 1
            count += 1
        else:
            return False
    
    # Must have at least 2 numbers
    return count >= 2


def consecutive_increasing_numbers_with_sequence(ch):
    """
    Extended version that returns the actual sequence if it exists.
    
    Args:
        ch: String containing only digits
    
    Returns:
        Tuple (is_valid, sequence) where sequence is list of integers if valid, empty list otherwise
    """
    if not ch:
        return (False, [])
    
    n = len(ch)
    
    for first_len in range(1, n):
        first_num_str = ch[:first_len]
        
        # Check for leading zeros
        if first_len > 1 and first_num_str[0] == '0':
            continue
        
        first_num = int(first_num_str)
        sequence = get_sequence(ch, first_num)
        
        if sequence and len(sequence) >= 2:
            return (True, sequence)
    
    return (False, [])


def get_sequence(ch, start_num):
    """
    Extracts the sequence of consecutive numbers starting with start_num.
    
    Args:
        ch: String of digits
        start_num: Starting number
    
    Returns:
        List of integers if valid, empty list otherwise
    """
    pos = 0
    current_num = start_num
    sequence = []
    
    while pos < len(ch):
        current_str = str(current_num)
        
        if ch[pos:pos + len(current_str)] == current_str:
            sequence.append(current_num)
            pos += len(current_str)
            current_num += 1
        else:
            return []
    
    return sequence


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("99100", True, "99, 100"),
        ("979899100101", True, "97, 98, 99, 100, 101"),
        ("12", True, "1, 2"),
        ("123", True, "1, 2, 3"),
        ("91011", True, "9, 10, 11"),
        ("99991000010001", True, "9999, 10000, 10001"),
        ("010", False, "Leading zeros not allowed"),
        ("111", False, "Can't split into consecutive increasing"),
        ("1", False, "Need at least 2 numbers"),
        ("191011", False, "19, 10, 11 - not increasing"),
        ("12345", True, "1, 2, 3, 4, 5 or 123, 124, 125"),
        ("67891011", True, "6, 7, 8, 9, 10, 11"),
    ]
    
    print("=" * 70)
    print("CONSECUTIVE INCREASING NUMBERS - TEST RESULTS")
    print("=" * 70)
    
    for i, (ch, expected, description) in enumerate(test_cases, 1):
        result = consecutive_increasing_numbers(ch)
        is_valid, sequence = consecutive_increasing_numbers_with_sequence(ch)
        
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        print(f"\nTest {i}: {status}")
        print(f"  Input:    '{ch}'")
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        
        if is_valid:
            print(f"  Sequence: {' -> '.join(map(str, sequence))}")
        else:
            print(f"  Note:     {description}")
    
    print("\n" + "=" * 70)
    
    # Interactive test
    print("\n\nInteractive Test:")
    print("-" * 40)
    test_strings = ["99100", "979899100101", "123456", "91011"]
    
    for test_str in test_strings:
        is_valid, sequence = consecutive_increasing_numbers_with_sequence(test_str)
        print(f"\nInput: {test_str}")
        if is_valid:
            print(f"Valid! Sequence: {sequence}")
        else:
            print("Invalid - cannot be split into consecutive increasing numbers")
