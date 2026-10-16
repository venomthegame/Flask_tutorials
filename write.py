file = open("sample.txt", "w")

# Write content to the file
file.write("Welcome to Python File Handling.\n")
file.write("This is the first line of the file.\n")
file.write("This is the second line of the file.")

file.close()

print("Content written successfully!")