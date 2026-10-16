# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(1, i + 1):  # Inner loop for columns
#         print("*", end=" ")   # Print star
#     print()




# rows = int(input("Enter the row size for the pattern: "))
# for i in range(1, rows + 1):  # Outer loop for rows
#     for j in range(rows  - i):  # Inner loop for spaces
#         print(" ", end=" ")
#     for k in range(1, 2 * i):  # Inner loop for stars
#         print("*", end=" ")
#     print()





rows = int(input("Enter the row size for the pattern: "))
for i in range(1,rows + 1):  # Upper part of diamond
    for j in range(rows  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()
for i in range(rows  - 1, 0, -1):  # Lower part of diamond
    for j in range(rows  - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print("*", end=" ")
    print()



