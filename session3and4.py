
#%%

file = open("hello.txt")

for line in file:
    print(line)
# %%

with open("hello.txt") as file:
    for line in file:
        print(line)
# %%

with open("hello.txt", "w") as file:
    file.writelines(["Hello this was written with Python"])
# %%

with open("hello.txt", "a") as file:
    file.writelines(["\nthis would be the second line"])
# %%

with open("programs.csv") as file:
    for line in file:
        cells = line.split(",")
        print(cells)
# %%

import csv

with open("programs.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        for cell in row:
            print(cell)

        print("")
# %%
import csv

clazz = [
    ["Luca", 66],
    ["Pepe", 67],
    ["Fran", 66]
]

with open("class.csv", "a") as file:
    writer = csv.writer(file)
    for person in clazz:
        writer.writerow(person)
# %%
import csv

clazz = [
    {"name": "Luca", "age": 66},
    {"name": "Pepe", "age": 667},
    {"name": "Fran", "age": 66},
]

with open("class.csv", "w") as file:
    writer = csv.DictWriter(file, ["name", "age"])
    for person in clazz:
        writer.writerow(person)


# %%

import csv

with open("class.csv") as file:
    reader = csv.reader(file)

    num_of_students = 0
    total_age = 0
    for line in reader:
        age = int(line[1])
        total_age = total_age + age
        num_of_students = num_of_students + 1
        
    print(total_age / num_of_students)


# %%

string = ""

with open("wikipedia_article.txt") as file:
    for line in file:
        string = string + line

def calculate_frequencies(text):
    clean_text = ""
    for character in text:
        if character.isalpha() or character == "'" or character == " ":
            clean_text = clean_text + character

    words = clean_text.split()
    frequencies = {}

    for word in words:
        if word in frequencies:
            frequencies[word] = frequencies[word] + 1
        else:
            frequencies[word] = 1

    return frequencies

def calculate_longest_word(frequencies):
    longest = 0
    for word in frequencies:
        if len(word) > longest:
            longest = len(word)
    return longest

def show_frequencies(frequencies):
    longest = calculate_longest_word(frequencies)

    for word in frequencies:
        number_of_spaces = longest - len(word)
        print(word + number_of_spaces * " " + " | " + frequencies[word] * "*")

show_frequencies(calculate_frequencies(string))
# %%

import json

with open('programs.json') as file:
    data = json.load(file)

    print(data["MCSBT"])

# %%

import json

students = [
    "JJ",
    "Fran",
    "others"
]

with open("students.json", "w") as file:
    json.dump(students, file)
# %%
