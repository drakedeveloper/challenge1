"""
Snail Matrix Traversal - Clockwise Spiral Order
Competitive Programming Solution
"""

def snail_matrix(matrix):
    """
    Returns all elements of a square matrix in clockwise spiral order.
    
    Args:
        matrix: n×n square matrix of integers
    
    Returns:
        List of integers in spiral order
    
    Time Complexity: O(n²)
    Space Complexity: O(1) excluding output array
    """
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    result = []
    
    # Define boundaries
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        # Traverse right along the top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Traverse down along the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Traverse left along the bottom row (if there's a row remaining)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Traverse up along the left column (if there's a column remaining)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result


def print_matrix(matrix):
    """Helper function to print matrix in readable format"""
    for row in matrix:
        print(' '.join(f'{x:3}' for x in row))
    print()


# Test cases
if __name__ == "__main__":
    # Test case 1: 3×3 matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Test Case 1:")
    print("Matrix:")
    print_matrix(matrix1)
    print("Spiral Order:", snail_matrix(matrix1))
    print("Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]")
    print()
    
    # Test case 2: 4×4 matrix
    matrix2 = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("Test Case 2:")
    print("Matrix:")
    print_matrix(matrix2)
    print("Spiral Order:", snail_matrix(matrix2))
    print("Expected: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]")
    print()
    
    # Test case 3: 1×1 matrix
    matrix3 = [[5]]
    print("Test Case 3:")
    print("Matrix:")
    print_matrix(matrix3)
    print("Spiral Order:", snail_matrix(matrix3))
    print("Expected: [5]")
    print()
    
    # Test case 4: 5×5 matrix
    matrix4 = [
        [1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    print("Test Case 4:")
    print("Matrix:")
    print_matrix(matrix4)
    result = snail_matrix(matrix4)
    print("Spiral Order:", result)
    print()
