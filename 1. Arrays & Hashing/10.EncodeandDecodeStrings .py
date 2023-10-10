#vsCode

class Codec:
    def encode(self, strs):
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    def decode(self, s):
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res

def main():
    codec = Codec()

    # Encode a list of strings
    input_strings = input("Enter a list of strings (comma-separated): ").split(',')
    encoded_string = codec.encode(input_strings)
    print("Encoded string:", encoded_string)

    # Decode a string
    encoded_input = input("Enter the encoded string: ")
    decoded_strings = codec.decode(encoded_input)
    print("Decoded strings:", decoded_strings)

if __name__ == "__main__":
    main()
