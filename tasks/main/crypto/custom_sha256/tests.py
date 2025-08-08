from generated_function import custom_sha256

def test_empty_message():
    expected = bytes.fromhex("e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    assert custom_sha256(b"") == expected

def test_abc_message():
    expected = bytes.fromhex("ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
    assert custom_sha256(b"abc") == expected

def test_hello_world():
    expected = bytes.fromhex("b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9")
    assert custom_sha256(b"hello world") == expected

def test_thousand_a():
    expected = bytes.fromhex("41edece42d63e8d9bf515a9ba6932e1c20cbc9f5a5d134645adb5db1b9737ea3")
    assert custom_sha256(b"a" * 1000) == expected

def test_special_characters():
    expected = bytes.fromhex("2076d3edf9910b166ebfaa09f4dcb7c41ab300466a75495a4e28286339eb1b39")
    assert custom_sha256(b"!@#$%^&()") == expected

def test_sentence():
    expected = bytes.fromhex("8f1ad6dfff1a460eb4ab78a5a7c3576209628ea200c1dbc70bda69938b401309")
    assert custom_sha256(b"a quick brown fox jumps over the lazy dog") == expected
