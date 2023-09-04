#vsCode

class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

def main():
    word_dict = WordDictionary()
    
    while True:
        print("Choose an operation:")
        print("1. Add a word")
        print("2. Search for a word (including '.')")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            word = input("Enter the word to add: ")
            word_dict.addWord(word)
            print(f"'{word}' has been added to the Word Dictionary.")
        elif choice == 2:
            word = input("Enter the word to search for (you can use '.' as a wildcard): ")
            if word_dict.search(word):
                print(f"'{word}' is in the Word Dictionary.")
            else:
                print(f"'{word}' is not in the Word Dictionary.")
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please choose a valid operation.")

if __name__ == "__main__":
    main()
