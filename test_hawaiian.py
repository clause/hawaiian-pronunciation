from typing import Optional

import pytest

from hawaiian import *


@pytest.mark.parametrize("s,expected", [
    # Hawaiian Consonants
    ("h", None),
    ("k", None),
    ("l", None),
    ("m", None),
    ("n", None),
    ("p", None),
    ("w", None),
    ("'", None),

    # Hawaiian Vowels
    ("a", HawaiianVowel.A),
    ("e", HawaiianVowel.E),
    ("i", HawaiianVowel.I),
    ("o", HawaiianVowel.O),
    ("u", HawaiianVowel.U),

    # Hawaiian Vowel Pairs
    ("ai", None),
    ("ae", None),
    ("ao", None),
    ("au", None),
    ("ei", None),
    ("eu", None),
    ("iu", None),
    ("oi", None),
    ("ou", None),
    ("ui", None),

    # Other
    (".", None),
    ("!", None),
    ("?", None),
    ("b", None),
])
def test_vowel_from(s: str, expected: Optional[HawaiianVowel]):
    assert vowel_from(s) == expected


@pytest.mark.parametrize("s,expected", [
    # Hawaiian Consonant
    ("h", HawaiianConsonant.H),
    ("k", HawaiianConsonant.K),
    ("l", HawaiianConsonant.L),
    ("m", HawaiianConsonant.M),
    ("n", HawaiianConsonant.N),
    ("p", HawaiianConsonant.P),
    ("w", HawaiianConsonant.W),
    ("'", HawaiianConsonant.OKINE),

    # Hawaiian Vowels
    ("a", None),
    ("e", None),
    ("i", None),
    ("o", None),
    ("u", None),

    # Hawaiian Vowel Pairs
    ("ai", None),
    ("ae", None),
    ("ao", None),
    ("au", None),
    ("ei", None),
    ("eu", None),
    ("iu", None),
    ("oi", None),
    ("ou", None),
    ("ui", None),

    # Other
    (".", None),
    ("!", None),
    ("?", None),
    ("b", None),
])
def test_consonant_from(s: str, expected: Optional[HawaiianConsonant]):
    assert consonant_from(s) == expected


@pytest.mark.parametrize("s,expected", [
    # Hawaiian Consonants
    ("h", None),
    ("k", None),
    ("l", None),
    ("m", None),
    ("n", None),
    ("p", None),
    ("w", None),
    ("'", None),

    # Hawaiian Vowels
    ("a", None),
    ("e", None),
    ("i", None),
    ("o", None),
    ("u", None),

    # Hawaiian Vowel Pairs
    ("ai", HawaiianVowelPair.AI),
    ("ae", HawaiianVowelPair.AE),
    ("ao", HawaiianVowelPair.AO),
    ("au", HawaiianVowelPair.AU),
    ("ei", HawaiianVowelPair.EI),
    ("eu", HawaiianVowelPair.EU),
    ("iu", HawaiianVowelPair.IU),
    ("oi", HawaiianVowelPair.OI),
    ("ou", HawaiianVowelPair.OU),
    ("ui", HawaiianVowelPair.UI),

    # other
    (".", None),
    ("!", None),
    ("?", None),
    ("aa", None),
])
def test_vowel_pair_from(s: str, expected: Optional[HawaiianVowelPair]):
    assert vowel_pair_from(s) == expected


@pytest.mark.parametrize("word,pronunciation", [
    (HawaiianWord("aloha"), "ah-loh-hah"),
    (HawaiianWord("Kakahiaka"), "kah-kah-hee-ah-kah"),
    (HawaiianWord("Mahalo"), "mah-hah-loh"),
    (HawaiianWord("E"), "eh"),
    (HawaiianWord("kono"), "koh-moh"),
    (HawaiianWord("mai"), "meye"),
    (HawaiianWord("maui"), "mow-ee"),
    (HawaiianWord("kane"), "kah-neh"),
    (HawaiianWord("humuhumunukunukuapua'a"), "hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah'ah")
])
def test_pronounce_word(word: HawaiianWord, pronunciation: str):
    assert pronounce_word(word) == pronunciation


@pytest.mark.parametrize("phrase,pronunciation", [
    (HawaiianPhrase([HawaiianWord("aloha")]), "Ah-loh-hah"),
    (HawaiianPhrase([HawaiianWord("Kakahiaka")]), "Kah-kah-hee-ah-kah"),
    (HawaiianPhrase([HawaiianWord("Mahalo")]), "Mah-hah-loh"),
    (HawaiianPhrase([HawaiianWord("E"), HawaiianWord("komo"), HawaiianWord("mai")]), "Eh koh-moh meye"),
    (HawaiianPhrase([HawaiianWord("maui")]), "Mow-ee"),
    (HawaiianPhrase([HawaiianWord("kane")]), "Kah-neh"),
    (HawaiianPhrase([HawaiianWord("humuhumunukunukuapua'a")]), "Hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah'ah")
])
def test_pronounce_phrase(phrase: HawaiianPhrase, pronunciation: str):
    assert pronounce_phrase(phrase) == pronunciation
