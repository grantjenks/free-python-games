""" Mad Libs: Funny Story Creation Game.

Exercises:

1. Can you create functionality to replace the given story?
2. Can you load the story and template from a file?
3. Can you add additional tenses?
4. Can you add flexibility in a loaded story template?
5. Can you adjust for grammar? (past tense, etc.)

"""

story = "The [adj] [adj] [n] [v] over the [adj] [adj] [n]"
# The quick black fox jumped over the lazy brown dog.

word_type_counter = {}

word_storage = {}

word_type_key = {
    "adj": "adjective",
    "n": "noun",
    "v": "verb",
    "adv": "adverb"
}

def extract_word_types():
    "Word types required extracted from story"
    for w_type in word_type_key:
        lookup = "[{}]".format(w_type)
        word_type_counter[w_type] = story.count(lookup)

def get_words():
    "Get words from user"
    for word in word_type_counter:
        while word_type_counter[word] > 0:
            question = input("Please enter a {}.({} remaining):".format(
                word_type_key[word].upper(),
                word_type_counter[word]))
            if word not in word_storage:
                word_storage[word] = [question]
            else:
                word_storage[word].append(question)
            word_type_counter[word] -= 1

def get_new_story():
    "Return new madlibbed story"
    new_story = story
    for word_type in word_storage:
        for i, word in enumerate(word_storage[word_type]):
            lookup = "[{}]".format(word_type)
            new_story = new_story.replace(lookup, word, 1)
    return new_story


extract_word_types()
get_words()
print("Your new story:")
print(get_new_story())
