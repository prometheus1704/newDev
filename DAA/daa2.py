import heapq

# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # define comparison for priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Step 1 & 2: Build Huffman Tree
def build_huffman_tree(text):
    # frequency dictionary
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1

    # priority queue
    heap = [Node(ch, fr) for ch, fr in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # pick 2 smallest nodes
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        # create new internal node
        new_node = Node(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right

        heapq.heappush(heap, new_node)

    return heap[0]

# Step 3: Generate Huffman Codes
def generate_codes(root, current_code, codes):
    if root is None:
        return
    if root.char is not None:
        codes[root.char] = current_code
        return
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

# Step 4: Encode the Text
def huffman_encode(text, codes):
    return ''.join(codes[ch] for ch in text)

# Step 5: Decode the Encoded Text
def huffman_decode(encoded_text, root):
    decoded = ''
    current = root
    for bit in encoded_text:
        current = current.left if bit == '0' else current.right
        if current.char:
            decoded += current.char
            current = root
    return decoded


# ------------------- MAIN -------------------
text = input("Enter text to encode: ")
root = build_huffman_tree(text)

codes = {}
generate_codes(root, "", codes)

print("\nCharacter Codes:")
for ch in codes:
    print(f"{ch} : {codes[ch]}")

encoded = huffman_encode(text, codes)
print("\nEncoded Text:", encoded)

decoded = huffman_decode(encoded, root)
print("\nDecoded Text:", decoded)
print()
