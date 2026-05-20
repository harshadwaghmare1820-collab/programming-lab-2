# File Handling

# 1. Write data to file
file = open("data.txt", "w")
file.write("Hello Python\n")
file.write("This is File Handling Experiment\n")
file.close()

# 2. Read data from file
file = open("data.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

# 3. Append data to file
file = open("data.txt", "a")
file.write("This line is appended\n")
file.close()

# 4. Read file line by line
file = open("data.txt", "r")
print("Reading line by line:")
for line in file:
    print(line.strip())
file.close()