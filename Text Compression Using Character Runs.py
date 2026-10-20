
# Text Compression Using Character Runs

original = input("Enter a string: ")

compressed = ""
count = 1

for i in range(1, len(original)):
    if original[i] == original[i - 1]:
        count += 1
    else:
        compressed += original[i - 1] + str(count)
        count = 1

# Add the final character and its count
if original:
    compressed += original[-1] + str(count)

# Calculate lengths
original_length = len(original)
compressed_length = len(compressed)

# Display results
print("Original String:", original)
print("Compressed String:", compressed)
print("Original Length:", original_length)
print("Compressed Length:", compressed_length)

if compressed_length < original_length:
    print("Compression is effective.")
elif compressed_length > original_length:
    print("Compressed string is longer than the original.")
else:
    print("Both strings have the same length.")
