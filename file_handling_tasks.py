# file_handling_tasks.py

# This file includes placeholders for file handling tasks.
# Students should complete each function according to the instructions.

def task1_create_file():
    with open("example.txt", "w") as file:
        file.write("Hello, world!")

def task2_read_file():
    with open("example.txt", "r") as file:
        contents = file.read()
        print(contents)

def task3_append_file():
    with open("example.txt", "a") as file:
        file.write("\nThis is a new line.")

def task4_count_lines():
    with open("example.txt", "r") as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))

def task5_find_word():
    word_to_find = "Hello"
    count = 0
    with open("example.txt", "r") as file:
        for line in file:
            count += line.count(word_to_find)
    print(f"The word '{word_to_find}' appears {count} times.")

def task6_copy_file():
    with open("source.txt", "r") as src, open("destination.txt", "w") as dest:
        dest.write(src.read())

def task7_replace_word():
    with open("example.txt", "r") as file:
        data = file.read()
    data = data.replace("oldword", "newword")
    with open("example.txt", "w") as file:
        file.write(data)

def task8_read_csv():
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def task9_write_csv():
    data = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
    with open("output.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerows(data)

def task10_json_file():
    data = {"name": "Alice", "age": 25}
    with open("data.json", "w") as file:
        json.dump(data, file)

    with open("data.json", "r") as file:
        loaded_data = json.load(file)
        print(loaded_data)

