# Create a 2D array (3x3) filled with zeros
rows = 3
cols = 3
my_2d_array = [[0 for _ in range(cols)] for _ in range(rows)]

# Fill the 2D array with values
for i in range(rows):
    for j in range(cols):
        my_2d_array[i][j] = i * cols + j

# Access and print the elements of the 2D array
for i in range(rows):
    for j in range(cols):
        print(my_2d_array[i][j], end=' ')
    print()

# Example: accessing a specific element
element = my_2d_array[1][2]
print(f"Element at row 1, column 2: {element}")
