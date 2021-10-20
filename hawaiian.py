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


def vowel_from(s: str) -> Optional[HawaiianVowel]:
    """
    Checks whether a string is a Hawaiian vowel
    :param s: a string
    :return: The corresponding HawaiianVowel if one exists
             None otherwise
    """
    try:
        return HawaiianVowel(s)
    except ValueError:
        return None


def consonant_from(s: str) -> Optional[HawaiianConsonant]:
    """
    Checks whether a string is a Hawaiian consonant
    :param s: a string
    :return: The corresponding HawaiianConsonant if one exists
             None otherwise
    """
    try:
        return HawaiianConsonant(s)
    except ValueError:
        return None


def vowel_pair_from(s: str) -> Optional[HawaiianVowelPair]:
    """
    Checks whether a string is a Hawaiian vowel pair
    :param s: a string
    :return: The corresponding HawaiianVowelPair if one exists
             None otherwise
    """
    try:
        return HawaiianVowelPair(s)
    except ValueError:
        return None


def pronounce_word(word: HawaiianWord) -> str:
    """
    Pronounces a given Hawaiian word
    :param word: a Hawaiian word
    :return: pronunciation of the given Hawaiian word
    """
    result = ""

    index = 0
    while index < len(word):
        character = word[index]
        next = word[index + 1]
        if vowel_from(character):
            result = result + pronounce_vowel(...)
            index += 1
        elif vowel_pair_from(character):
            result = result + pronounce_vowel_pair(character, next)
            index += 2
        elif consonant_from(character):
            result = result + pronounce_consonant(...)
            index += 1
        else:
            ...

    return result


def pronounce_phrase(phrase: HawaiianPhrase) -> str:
    """
    Pronounces a given Hawaiian phrase according to rules from: http://nifty.stanford.edu/2019/bingham-hawaiian-phonetic-generator/

    :param phrase: a Hawaiian phrase
    :return: pronunciation of the given Hawaiian phrase
    """
    return " ".join(pronounce_word(word) for word in phrase).capitalize()
