def find_longest_words(filename):
    try:
        with open(filename, 'r') as file:
            words = [word.strip() for line in file for word in line.split()]
            longest_words = [word for word in words if len(word) == max(map(len, words))]
            return longest_words
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

if __name__ == "__main__":
    filename = "test.txt"
    result = find_longest_words(filename)
    print(result)