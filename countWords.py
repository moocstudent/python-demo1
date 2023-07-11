import re
from collections import Counter

# The original text
text = """
Upgrading from 1.1.x to 1.2.x
Spring Data R2DBC was developed with the intent to evaluate how well R2DBC can integrate with Spring applications. 
One of the main aspects was to move core support into Spring Framework once R2DBC support has proven useful. 
Spring Framework 5.3 ships with a new module: Spring R2DBC (spring-r2dbc).
"""

# Convert the text to lowercase
text = text.lower()

# Remove non-alphabetic characters
text = re.sub('[^a-z]', ' ', text)

# Split the text into words
words = text.split()

# Count the frequency of each word
word_frequencies = Counter(words)

# Print the word frequencies
print(word_frequencies)
