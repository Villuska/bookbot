
def get_words(string):
    words = string.split()
    return words

def count_char(string):
    char_counts = {}
    string_low = string.lower()
    lista = get_words(string_low)
    for word in lista:
        for char in word:
            if char not in char_counts and char.isalpha():
                char_counts[char] = 1
            elif char.isalpha():
                char_counts[char] += 1
    return char_counts

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = len(get_words(file_contents))
    char = count_char(file_contents)
    char = dict(sorted(char.items(), key=lambda item: item[1], reverse=True))
    print(words)
    print(char)
main()