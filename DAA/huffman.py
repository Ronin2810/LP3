import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_map):
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged_node = HuffmanNode(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right

        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(root):
    codes = {}
    def traverse(node, code=""):
        if node:
            if node.char is not None:
                codes[node.char] = code
            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

    traverse(root)
    return codes

def huffman_encoding(text):
    freq_map = defaultdict(int)
    for char in text:
        freq_map[char] += 1

    if len(freq_map) == 1:
        char = next(iter(freq_map))
        return "0" * freq_map[char], {char: "0"}

    root = build_huffman_tree(freq_map)
    huffman_codes = build_huffman_codes(root)

    encoded_text = "".join(huffman_codes[char] for char in text)
    return encoded_text, huffman_codes

def huffman_decoding(encoded_text, huffman_codes):
    reversed_codes = {code: char for char, code in huffman_codes.items()}
    current_code = ""
    decoded_text = ""

    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_codes:
            decoded_text += reversed_codes[current_code]
            current_code = ""

    return decoded_text

# Example usage:
text = "hello, world!"
encoded_text, huffman_codes = huffman_encoding(text)
print(f"Encoded text: {encoded_text}")
decoded_text = huffman_decoding(encoded_text, huffman_codes)
print(f"Decoded text: {decoded_text}")
