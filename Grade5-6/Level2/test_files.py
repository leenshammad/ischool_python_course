# Writing to a file
file = open("data.txt", "w")
file.write("Saving some important data. name is leen")
file.close()

# Reading from a file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()