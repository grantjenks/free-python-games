""" Mad Libs: Funny Story Creation Game.

Exercises:

1. Can you create functionality to replace the given story?
2. Can you load the story and template from a file?
3. Can you add additional parts of speech?
4. Can you add flexibility in a loaded story template?
5. Can you adjust for grammar? (past tense, etc.)
6. Can you fix the bug that occurs if there is a period after the story?
7. At what point would you need to encapsulate into a function?
8. Can you use a function for this?
9. What problems can occur to the expected output if the program were to 
    crash mid-run (ex: due to power failure, unexpected computer freeze etc.)
10. How could you re-engineer this to allow for more robust retention of 
    the original story and/or the input collected?
"""

story_template = "The [adj] [adj] [n] [v] over the [adj] [n]"
# The quick brown fox jumps over the lazy dog

new_story = ""

word_type_key = {
    "[adj]": "adjective",
    "[n]": "noun",
    "[v]": "verb",
    "[adv]": "adverb"
}

"Replace word types with user provided words"
for char_block in story_template.split(' '):
    if char_block in word_type_key:
        new_word = input("Please enter a {}: ".format(
            word_type_key[char_block]))
        new_story += " {} ".format(new_word)
    else:
        new_story += " {} ".format(char_block)

print("Your new story:")
print(new_story)
