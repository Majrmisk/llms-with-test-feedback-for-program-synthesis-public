import pytest
from generated_function import diffie_hellman_key_exchange

def test_valid_shared_secret_1():
    assert diffie_hellman_key_exchange(6, 5, 23, 2) == 8

def test_valid_shared_secret_2():
    assert diffie_hellman_key_exchange(3, 7, 13, 2) == 5

def test_non_prime_modulus():
    with pytest.raises(ValueError):
        diffie_hellman_key_exchange(5, 4, 15, 2)

def test_invalid_private_key_zero():
    with pytest.raises(ValueError):
        diffie_hellman_key_exchange(0, 5, 23, 2)

def test_negative_public_component():
    with pytest.raises(ValueError):
        diffie_hellman_key_exchange(6, -3, 23, 2)

def test_valid_shared_secret_large():
    assert diffie_hellman_key_exchange(10, 45, 97, 5) == 70

def test_public_component_one():
    assert diffie_hellman_key_exchange(7, 1, 23, 2) == 1

def test_public_component_equals_prime_minus_one():
    assert diffie_hellman_key_exchange(3, 22, 23, 2) == 22
