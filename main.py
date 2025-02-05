def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    split_file = file_contents.split()
    
    count = 0
    for word in split_file:
        count += 1

    counted_chars = count_each_character(file_contents)

    alpha_list = alpha_character_count(counted_chars)

    sorted_list = sort_character_count(alpha_list)

    print(f"--- Begin report of {path_to_file} ---")
    print(count, " words found in the document")
    print("")
    for item in sorted_list:
        print(f"The '{item["char"]}' character was found {item["count"]} times")
    print("--- End report ---")


def count_each_character(file_contents):
    character_count = {}
    for char in file_contents:
        low_char = char.lower()
        if low_char in character_count:
            character_count[low_char] += 1
        else:
            character_count[low_char] = 1
    return character_count

def alpha_character_count(character_count):    
    alpha_list = []
    for char, char_count in character_count.items():
        if char.isalpha():
            alpha_list.append({"char": char, "count": char_count})
    return alpha_list

def sort_on(dict):
    return dict["count"]

def sort_character_count(alpha_list):
    alpha_list.sort(key=sort_on, reverse = True)
    return alpha_list


main()