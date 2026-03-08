"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    return 'un'+word


def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.
    """

    seperator = ' :: ' + vocab_words[0]
    joined = seperator.join(vocab_words)
    return joined


def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    if word[-5] == 'i':
        word = word[:-5]
        return word + 'y'
    else:
        return word[:-4]


def adjective_to_verb(sentence, index):
    """Changes the adjective within the sentence to a verb.
    """
    sentence = sentence.split( )
    if sentence[index][-1] == '.':
        sentence[index] = sentence[index][ :-1]
    return sentence[index]+'en'
