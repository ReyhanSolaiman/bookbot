
def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    split_file = file_contents.split()
    
    count = 0
    for word in split_file:
        count += 1

    print(count)

main()