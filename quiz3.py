
file_name = 'romeo.txt'
file = open(file_name)


word_list = []


for line in file:
    words = line.split()
    for word in words:
        if word not in word_list:
            word_list.append(word)

# Close the file
file.close()

# Sort and print the unique words
word_list.sort()
for word in word_list:
    print(word)
