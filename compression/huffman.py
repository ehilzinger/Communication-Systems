import heapq
from collections import Counter, namedtuple


class Node:
    def __init__(self, char, frequency):
        self.char = char
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(text):
    # Count the frequency of each character in the text
    frequency = Counter(text)

    # Create leaf nodes for each character
    nodes = [Node(char, freq) for char, freq in frequency.items()]

    # Build the Huffman tree
    heapq.heapify(nodes)
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(nodes, merged)

    return nodes[0]


def build_huffman_code(node, prefix="", code={}):
    if node is not None:
        if node.char is not None:
            code[node.char] = prefix
        build_huffman_code(node.left, prefix + "0", code)
        build_huffman_code(node.right, prefix + "1", code)
    return code


def compress(text):
    root = build_huffman_tree(text)
    code = build_huffman_code(root)
    encoded_text = "".join(code[char] for char in text)
    return encoded_text, code


def decompress(encoded_text, code):
    reversed_code = {v: k for k, v in code.items()}
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_code:
            decoded_text += reversed_code[current_code]
            current_code = ""
    return decoded_text


if __name__ == "__main__":
    # Example usage
    text = "this is an example for huffman encoding"

    # Compress the text
    encoded_text, huffman_code = compress(text)
    print("Compressed text:", encoded_text)

    # Decompress the text
    decoded_text = decompress(encoded_text, huffman_code)
    print("Decompressed text:", decoded_text)
