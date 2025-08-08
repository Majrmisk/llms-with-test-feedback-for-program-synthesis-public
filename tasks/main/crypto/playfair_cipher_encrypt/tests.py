from generated_function import playfair_cipher_encrypt

def test_known_example():
    plaintext = "HIDETHEGOLDINTHETREESTUMP"
    key = "PLAYFAIREXAMPLE"
    expected = "BMODZBXDNABEKUDMUIXMMOUVIF"
    ciphertext = playfair_cipher_encrypt(plaintext, key)
    assert ciphertext == expected

def test_balloon_monarchy():
    plaintext = "BALLOON"
    key = "MONARCHY"
    expected = "IBSUPMNA"
    ciphertext = playfair_cipher_encrypt(plaintext, key)
    assert ciphertext == expected

def test_secretmessage_balloon():
    plaintext = "SECRETMESSAGE"
    key = "BALLOON"
    expected = "XKDQFSKFXLRLCF"
    ciphertext = playfair_cipher_encrypt(plaintext, key)
    assert ciphertext == expected

def test_hello_keyword():
    plaintext = "HELLO"
    key = "KEYWORD"
    expected = "GYIZSC"
    ciphertext = playfair_cipher_encrypt(plaintext, key)
    assert ciphertext == expected

def test_sentence():
    plaintext = "aquickbrownfoxjumpsoverthelazydog"
    key = "PLAYFAIR"
    expected = "BWPEKSCBQVTPSVEPEFTQUGDOKGAYXFRTKV"
    ciphertext = playfair_cipher_encrypt(plaintext, key)
    assert ciphertext == expected
