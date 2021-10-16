from typing import NewType, List

HawaiianWord = NewType('HawaiianWord', str)
HawaiianPhrase = NewType('HawaiianPhrase', List[HawaiianWord])


def pronounce_phrase(phrase: HawaiianPhrase) -> str:
    """
    Pronounces a given Hawaiian phrase according to rules from: http://nifty.stanford.edu/2019/bingham-hawaiian-phonetic-generator/

    :param phrase: a Hawaiian phrase
    :return: pronunciation of the given Hawaiian phrase
    """
    pass
