import pytest

from hawaiian import HawaiianPhrase, HawaiianWord, pronounce_phrase


@pytest.mark.parametrize("phrase,pronunciation", [
    (HawaiianPhrase([HawaiianWord("aloha")]), "Ah-loh-hah"),
    (HawaiianPhrase([HawaiianWord("Kakahiaka")]), "Kah-kah-hee-ah-kah"),
    (HawaiianPhrase([HawaiianWord("Mahalo")]), "Mah-hah-loh"),
    (HawaiianPhrase([HawaiianWord("E komo mai")]), "Eh koh-moh meye"),
    (HawaiianPhrase([HawaiianWord("maui")]), "Mow-ee"),
    (HawaiianPhrase([HawaiianWord("kane")]), "Kah-neh"),
    (HawaiianPhrase([HawaiianWord("humuhumunukunukuapua'a")]), "Hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah'ah")
])
def test_pronounce_phrase(phrase: HawaiianPhrase, pronunciation: str):
    assert pronounce_phrase(phrase) == pronunciation
