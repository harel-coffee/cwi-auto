"""
Phonetic features.

This module contains functions to extract features concerning phonetics from a target word or phrase

"""


import pyphen



def consonant_frequency(target_word):
    """
    Compute the frequency of consonants in the target word

    Args:
        target_word (str): word or phrase candidate.

    Returns:
        float - the frequency of consonants
    """

    consonants = set("aeiou")
    freq = len([letter for letter in target_word if letter not in consonants]) / len(target_word)

    return freq


def num_syllables(target_word, language):
    """
    Compute the number syllables in the target word

    Args:
        target_word (str): word or phrase candidate
        language (str): the language of word or phrase candidate

    Returns:
        float - the number of syllables

    Raises:
        ValueError
    """

    if language == 'english':
        hyph_dictionary = pyphen.Pyphen(lang='en')
    elif language == 'spanish':
        hyph_dictionary = pyphen.Pyphen(lang='es')
    elif language == 'german':
        hyph_dictionary = pyphen.Pyphen(lang='de')

    else:
        raise ValueError("Language specified ({}) not supported.".format(language))

    num_syllables = 0

    for token in target_word.split():  # split up multiword phrases
        hyphenated = hyph_dictionary.inserted(token)
        num_syllables += len(hyphenated.split('-'))

    return num_syllables