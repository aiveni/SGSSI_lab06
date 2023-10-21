import os
import hashlib

# Step 1: Read the pattern from the input file
with open('SGSSI-23.CB.03.txt', 'r') as f:
    pattern = f.readline().strip()

# Step 2: Iterate over all files in the directory and check for matches
matches = {}
for filename in os.listdir('SGSSI-23.S.6.2.CB.03.Candidatos'):
    filepath = os.path.join('SGSSI-23.S.6.2.CB.03.Candidatos', filename)
    with open(filepath, 'r') as f:
        # Check if the first line matches the pattern
        if f.readline().strip() == pattern:
            # Calculate the SHA-256 hash of the file
            hash_obj = hashlib.sha256()
            hash_obj.update(f.read().encode('utf-8'))
            hash_str = hash_obj.hexdigest()

            # Check if the hash starts with a sequence of 0's
            prefix_len = 0
            for c in hash_str:
                if c == '0':
                    prefix_len += 1
                else:
                    break

            # Store the filename and prefix length in the dictionary
            matches[filename] = prefix_len

# Step 3: Find the filename with the longest prefix and print it
longest_prefix = max(matches.values())
longest_prefix_files = [filename for filename, prefix_len in matches.items() if prefix_len == longest_prefix]
selected_file = longest_prefix_files[0]  # Choose the first file in case of ties
print(f"Selected file: {selected_file}, prefix length: {longest_prefix}")
