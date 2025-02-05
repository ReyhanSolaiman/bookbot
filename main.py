
def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    split_file = file_contents.split()
    
    count = 0
    for word in split_file:
        count += 1

    print(count)

    counted_chars = count_each_character(file_contents)
    print(counted_chars)

def count_each_character(file_contents):
    character_count = {}
    for char in file_contents:
        low_char = char.lower()
        if low_char in character_count:
            character_count[low_char] += 1
        else:
            character_count[low_char] = 1
    return character_count

main()