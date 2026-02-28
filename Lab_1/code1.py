import nltk
from urllib import request
nltk.download('punkt')
nltk.download('punkt_tab')
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

# Read file as lines
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

start_index = None
end_index = None

# Find markers
for i, line in enumerate(lines):
    if "*** START OF THE PROJECT" in line and start_index is None:
        start_index = i
    if "*** END OF THE PROJECT" in line:
        end_index = i
        break

if start_index is None or end_index is None or end_index <= start_index:
    raise ValueError("Could not find valid START/END markers in the file.")

# How much to trim (in lines)
trim_begin_lines = start_index + 1            # lines removed from the beginning incl. START line
trim_end_lines = len(lines) - end_index       # lines removed from the end incl. END line

# Extract main content (exclude marker lines)
content = lines[start_index + 1:end_index]

# Remove empty lines after START
while content and content[0].strip() == "":
    content.pop(0)

# Remove empty lines before END
while content and content[-1].strip() == "":
    content.pop()

# Remove unnecessary paragraph marks / hard-wrapped lines
paragraphs = []
current = []

for line in content:
    if line.strip() == "":  # paragraph boundary
        if current:
            paragraphs.append(" ".join(s.strip() for s in current).strip())
            current = []
    else:
        current.append(line)

if current:
    paragraphs.append(" ".join(s.strip() for s in current).strip())

# New string + length
cleaned_text = "\n\n".join(paragraphs) + "\n"
print("Trimmed from beginning (lines):", trim_begin_lines)
print("Trimmed from end (lines):", trim_end_lines)
print("Length of cleaned text (characters):", len(cleaned_text))

# Save cleaned text
with open(output_file, "w", encoding="utf-8") as f:
    f.write(cleaned_text)

print(f"Cleaned file saved as: {output_file}")