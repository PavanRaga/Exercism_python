import re

with open("README.md","r") as f:
    file_content = f.read()

# Get the text from file
m = re.search('```text([\n\w\s:.,-]+)',file_content)
string = m.group(1)

#split them to form verse
new_string = list(filter(len, string.splitlines()))
len_text = len(new_string)

def recite(start_verse, end_verse):
    if start_verse > len_text or end_verse > len_text or end_verse < start_verse:
        print("Invalid request")
    if start_verse == end_verse:
        return [(new_string[start_verse-1])]
    else:
        return new_string[start_verse-1:end_verse]