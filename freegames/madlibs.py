"""Mad Libs: Funny Story Creation Game

Exercises:

1. How to replace the story?
2. How load the story and from a file?
3. How to add additional parts of speech?

"""

# The quick brown fox jumps over the lazy dog.
template = 'The |1| |2| |3| |4| over the |5| |6|.'
parts = {
    '1': 'adjective',
    '2': 'adjective',
    '3': 'noun',
    '4': 'verb',
    '5': 'adjective',
    '6': 'noun',
}

chunks = []

for chunk in template.split('|'):
    if chunk in parts:
        description = parts[chunk]
        prompt = 'Enter [{}]: '.format(description)
        word = input(prompt)
        chunks.append(word)
    else:
        chunks.append(chunk)

print('=' * 80)
story = ''.join(chunks)
print(story)
