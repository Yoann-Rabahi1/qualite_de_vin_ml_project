import pandas as pd
from src.features import qualite_binaire, norm


def test_mauvais_vin():
    assert qualite_binaire(6) == "0"


def test_bon_vin():
    assert qualite_binaire(8) == "1"


def test_note_limite():
    assert qualite_binaire(7) == "1"


def test_normalisation_moyenne():
    donnees = pd.DataFrame({
        "alcool": [10, 12, 14],
        "sucre": [2, 4, 6]
    })

    resultat = norm(donnees)
    assert (resultat.mean().abs() < 0.00001).all()


def test_normalisation_ecart_type():
    donnees = pd.DataFrame({
        "alcool": [10, 12, 14],
        "sucre": [2, 4, 6]
    })

    resultat = norm(donnees)
    assert ((resultat.std() - 1).abs() < 0.00001).all()