import sys
import re
import string
 
'''
HOW TO USE
 
In your terminal, make sure you have python3 installed
 
then make sure all of the files are in the same directory
 
terminal$ python3 shuffle.py listings.txt
 
shuffle.py - name of this script
listings.txt - where you will have the entries
 
 
sample listings.txt
////////////////////////////////////
Listing
 
Kaniq - UC Faerie Xwee (T6)
 
Quiggled pls
 
@maria
 
Listing
Arkimadei - UC Mallow (T2) QUIGGLE
@maylie
 
////////////////////////////////////
 
 
 
output for
 
python3 shuffle.py listings.txt
 
/////////////////////////////////////
<br>
<br> 
 
Arkimadei - UC Mallow (T2) QUIGGLE
 
<br>
 
<br> 
 
Kaniq - UC Faerie Xwee (T6)
 
<br>
////////////////////////////////////
 
'''
finalDict = {"T1": [], "T2": [], "T3": [], "T4": [], "T5": [], "T6": [], "T7": [], "T8": [], "T9": [], "T10": []}

class Listing:
  def __init__(self, listing, tier, petname="", username="", accepts=""):
    self.listing = listing
    self.tier = tier
    self.username = username
    self.petname = petname
    self.accepts = accepts
 
def getCurrentTier(line):
    if "T10" in line.upper():
        return "T10"
    for tier in finalDict.keys():
        if tier in line.upper():
            return tier

def extract_pet_name(listing):
    words = listing.split()
    first_word = words[0]
    if len(first_word) > 2:
        return first_word
    return "" 
 
def replace_cant_initiate(string):
    # Define a regular expression pattern to match different permutations of "can't initiate"
    pattern = r"(?i)\b(?:can't\s+initiate|\*cant\s+initiate\*|\{cant\s+initiate\}|can't\s+ini|cant\s+initiate|cant\s+ini)\b"
 
    # Replace the matched patterns with "✪"
    replaced_string = re.sub(pattern, "✪", string)
 
 
    replaced_string = replaced_string.replace("*✪*", " ✪ ")
    replaced_string = replaced_string.replace("{✪}"," ✪ ")
    replaced_string = replaced_string.replace("(✪)"," ✪ ")
    replaced_string = replaced_string.replace("*", " ")
 
 
    replaced_string = replaced_string.replace(" uc ", " UC ")
    replaced_string = replaced_string.replace(" the ", " - ") 
 
    return replaced_string
 
def prettyFormat(text):
    asci = ''.join(char for char in text if char in string.printable)
    return capitalizeAfterDash(replace_cant_initiate(capitalizeInsideParentheses(asci.replace('Listing:', ''))))
 
def capitalizeInsideParentheses(string):
    # Find the starting and ending positions of the parentheses
    start = string.find('(')
    end = string.find(')')
 
    # Check if both parentheses are present and the text inside is non-empty
    if start != -1 and end != -1 and start < end - 1:
        # Extract the text inside the parentheses
        inside_parentheses = string[start + 1:end]
 
        # Capitalize the extracted text
        capitalized_inside_parentheses = inside_parentheses.capitalize()
 
        # Replace the original text inside the parentheses with the capitalized text
        capitalized_string = string[:start + 1] + capitalized_inside_parentheses + string[end:]
        return capitalized_string
 
    # Return the original string if no parentheses or empty text inside parentheses
    return string

def capitalizeAfterDash(string):
    # Find the position of " UC "
    dash_index = string.find(" UC ")
 
    if dash_index != -1:
        capitalized_string = string[:dash_index+3] + string[dash_index+3:].title()
        return capitalized_string
 
    return string

def printListings(): 
    for tier in finalDict:
        if len(finalDict[tier]) == 0:
            continue
        print("<br> \n")
        for pet in finalDict[tier]:
            print(pet.listing)
            print("\n<br>\n")
    print("************************************")
    print()
    for tier in finalDict:
        if len(finalDict[tier]) == 0:
            continue
        print("<br> \n")
        for pet in finalDict[tier]:
            print(pet.username)
            print("\n<br>\n")
def printAccepts(): 
    for tier in finalDict:
        if len(finalDict[tier]) == 0:
            continue
        print("<br> \n")
        for pet in finalDict[tier]:
            if pet.accepts:
                print(pet.accepts)
            else:
                print(pet.listing)
            print("\n<br>\n")

def printMissing():
     print("\nMISSING DECISIONS ON THE FOLLOWING PETS, let me know if I missed you \n")
     for tier in finalDict:
        if len(finalDict[tier]) == 0:
            continue
        for pet in finalDict[tier]:
            if not pet.accepts:
                print(pet.listing, "\n")
            
def extract_accept_details(line):
    match = re.search(r"(?i)(accept|accepting|accepts:)([^.]+)", line)
    if match:
        return match.group(2).strip()
    return ""

def remove_after_for(line):
    match = re.search(r"(?i)\bfor\b", line)
    if match:
        return line[:match.start()].strip()
    return line

def cleanup(line):
    line = remove_after_for(line)
    line = line.replace(":", "")
    line = re.sub(r'\bing\b', '', line, flags=re.IGNORECASE)
    return re.sub(r'\bed\b', '', line)


def shouldPass(line):
    for sentence in line.split('.'):
        if 'pass' in sentence.lower():
            return True
    return False
                    
def addAccepts(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            for pet in finalDict.values():
                for item in pet:
                    if item.petname.lower() in line.lower():
                        accepts = cleanup(extract_accept_details(line))
                        if accepts:
                            item.accepts = f"{item.listing} ACCEPTS {accepts}"
                        if shouldPass(line):
                            item.accepts = f"{item.listing} PASS"
            
def shuffle():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            current_tier = None
            current_list = []
            for line in file:
                line = line.strip()
                if line.startswith('@'):
                    for item in current_list:
                        item.username = line
                        finalDict[item.tier].append(item)
                    current_list = []
                    current_tier = None
     
                if line.startswith('Listing:'):
                    current_tier = None
     
                current_tier = getCurrentTier(line)
                listing = prettyFormat(line)
                if line and current_tier:
                    current_list.append(Listing(listing, current_tier, extract_pet_name(listing)))
        if len(sys.argv) > 2:
            second_filename = sys.argv[2]
            print("************************************")
            print()
            addAccepts(second_filename)
            printAccepts()
            if len(sys.argv) > 3:
                printMissing()
        else:
            printListings()
    else:
        print("Text file not provided.")
     
shuffle()
