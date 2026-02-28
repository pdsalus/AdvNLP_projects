import nltk
from urllib import request

#1a
import os
# Book download
url = "https://www.gutenberg.org/ebooks/7290.txt.utf-8"
filename = "book.txt"

# Download the file
response = request.urlopen(url)
data = response.read()

# Save it locally
with open(filename, "wb") as f:
    f.write(data)

print("Book download complete.")

# Book file size
file_size = os.path.getsize("book.txt")
print("Book size in bytes:", file_size)


#1b
input_file = "book.txt"
output_file = "book_cleaned.txt"

# Read file
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

start_index = None
end_index = None

# Find markers
for i, line in enumerate(lines):
    if "*** START OF THE PROJECT" in line:
        start_index = i
    if "*** END OF THE PROJECT" in line:
        end_index = i
        break

# Extract main content (exclude marker lines)
content = lines[start_index + 1:end_index]

# Remove empty lines at the beginning
while content and content[0].strip() == "":
    content.pop(0)

# Remove empty lines at the end
while content and content[-1].strip() == "":
    content.pop()

# Save cleaned text
with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(content)

print(f"Cleaned file saved as: {output_file}")