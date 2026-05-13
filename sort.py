# Selection Sort using User Input

# Input number of elements
n = int(input("Enter number of elements: "))

# Empty list
arr = []

# Taking elements from user
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Selection Sort
for i in range(n):

    min_index = i

    for j in range(i + 1, n):

        if arr[j] < arr[min_index]:
            min_index = j

    # Swap
    arr[i], arr[min_index] = arr[min_index], arr[i]

# Output
print("Sorted Array:")
print(arr)
--------------------

# Enter number of elements: 5
# Enter element: 64
# Enter element: 25
# Enter element: 12
# Enter element: 22
# Enter element: 11

# Sorted Array:
# [11, 12, 22, 25, 64]



15. Why is time complexity always O(n²)?
Because Selection Sort always performs comparisons even if array is already sorted.

16. What is the space complexity of Selection Sort?
O(1) because no extra array is used.

17. How many passes are required in Selection Sort?
For n elements:n−1
passes are required.

18. How many comparisons occur in Selection Sort?
Maximum comparisons:n(n−1)/2

What are advantages of Selection Sort?

Advantages:

Simple implementation
Less memory usage
Fewer swaps
27. What are disadvantages of Selection Sort?

Disadvantages:

Slow for large data
Time complexity always high
Not adaptive
	​
