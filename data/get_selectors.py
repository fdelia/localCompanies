from bs4 import BeautifulSoup
import json
import re

# Load configs
data = {}
with open('get_selectors.json') as f:
    data = json.load(f)
   
soup = BeautifulSoup(open(data['json_file']), "html.parser")

# Find first elements containing given texts from search pair
container1 = soup.findAll(lambda tag: data['search_pair'][0] in tag.text)[-1:][0]
container2 = soup.findAll(lambda tag: data['search_pair'][1] in tag.text)[-1:][0]

# Find first common parent element of the pair
# Get parents as long as not same
el1 = container1
el2 = container2
for i in range(0, 10):
	el1 = el1.parent
	el2 = el2.parent

	if (el1 == el2):
		break

	if (i == 9):
		print("No parent found.")


# Generate code to get all elements like the pair
code = ""
code += f"parent = soup.find('{el1.name}', class_='{' '.join(el1['class'])}')"
code += "\n"
code += f"children = parent.findAll('{container1.name}', class_='{' '.join(container1['class'])}')"
code += "\nchildren = [x for x in children if x.text.strip() != '']"

print("")
print(code)
print("")

# Run it
exec(code)

# Show other elements
for child in children:
	print(child.text)
