from enum import Enum
from typing import NewType, List, Optional

HawaiianWord = NewType('HawaiianWord', str)
HawaiianPhrase = NewType('HawaiianPhrase', List[HawaiianWord])


class HawaiianVowel(Enum):
    A = "a"
    E = "e"
    I = "i"
    O = "o"
    U = "u"


class HawaiianConsonant(Enum):
    H = "h"
    K = "k"
    L = "l"
    M = "m"
    N = "n"
    P = "p"
    W = "w"
    OKINE = "'"


class HawaiianVowelPair(Enum):
    AE = "ae"
    AI = "ai"
    AO = "ao"
    AU = "au"

    EI = "ei"
    EU = "eu"

    IU = "iu"

    OI = "oi"
    OU = "ou"

    UI = "ui"


def vowel_from(s: str, index: int = 0) -> Optional[HawaiianVowel]:
    """
    Checks whether a string is a Hawaiian vowel.

    :param s: a string
    :return: The corresponding HawaiianVowel if one exists
             None otherwise
    """
    try:
        return HawaiianVowel(s[index])
    except ValueError:
        return None


def consonant_from(s: str, index: int = 0) -> Optional[HawaiianConsonant]:
    """
    Checks whether a string is a Hawaiian consonant.

    :param s: a string
    :return: The corresponding HawaiianConsonant if one exists
             None otherwise
    """
    try:
        return HawaiianConsonant(s[index])
    except ValueError:
        return None


def vowel_pair_from(s: str, index: int = 0) -> Optional[HawaiianVowelPair]:
    """
    Checks whether a string is a Hawaiian vowel pair.

    :param s: a string
    :return: The corresponding HawaiianVowelPair if one exists
             None otherwise
    """
    try:
        return HawaiianVowelPair(s[index:index + 2])
    except ValueError:
        return None


def pronounce_vowel_pair(word: HawaiianWord, index: int) -> str:
    """

    :param word:
    :param index:
    :return:
    """
    pronunciaiton = {
        "ai": "eye",
        "ae": "eye",
        "ao": "ow",
        "au": "ow",
        "ei": "ay",
        "eu": "eh-oo",
        "iu": "ew",
        "oi": "oy",
        "ou": "ow",
        "ui": "ooey",
    }[word[index:index + 2]]

    return pronunciaiton


def pronounce_vowel(word: HawaiianWord, index: int) -> str:
    pronunciation = {
        "a": "ah",
        "e": "eh",
        "i": "ee",
        "o": "oh",
        "u": "oo",
    }[word[index]]

    return pronunciation


def pronounce_consonant(word: HawaiianWord, index: int) -> str:
    pronunciation = {
        "h": "h",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "p": "p",
        "'": "'"
    }.get(word[index])

    if pronunciation:
        return pronunciation

    # At this point, I know the consonant is "w"
    if index == 0:
        return "w"
    elif word[index - 1] in ["a", "o", "u"]:
        return "w"
    elif word[index - 1] in ["i", "e"]:
        return "v"
    else:
        raise AssertionError("Shouldn't get here!")


def should_insert_hyphen(word: str, index: int) -> bool:
    """
    returns true if a hyphen should be inserted
    :param word:
    :param index:
    :return:
    """
    if index >= len(word):
        return False

    if word[index] == "'":
        return False

    return True


def pronounce_word(word: HawaiianWord) -> str:
    """
    Pronounces a given Hawaiian word.

    :param word: a Hawaiian word
    :return: pronunciation of the given Hawaiian word
    """
    # TODO: Fix this up with a general validation approach
    word = word.lower()

    result = ""

    index = 0
    while index < len(word):
        if vowel_pair_from(word, index):
            result = result + pronounce_vowel_pair(word, index)
            index += 2
            if should_insert_hyphen(word, index):
                result = result + "-"
        elif vowel_from(word, index):
            result = result + pronounce_vowel(word, index)
            index += 1
            if should_insert_hyphen(word, index):
                result = result + "-"
        elif consonant_from(word, index):
            result = result + pronounce_consonant(word, index)
            index += 1
        else:
            raise AssertionError(f"Shouldn't get here, at index {index}!")
    return result


def pronounce_phrase(phrase: HawaiianPhrase) -> str:
    """
    Pronounces a given Hawaiian phrase according to rules from: http://nifty.stanford.edu/2019/bingham-hawaiian-phonetic-generator/

    :param phrase: a Hawaiian phrase
    :return: pronunciation of the given Hawaiian phrase
    """
    return " ".join(pronounce_word(word) for word in phrase).capitalize()
