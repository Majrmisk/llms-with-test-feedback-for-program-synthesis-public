from generated_function import verify_digital_signature

def test_valid_signature():
    message = b"Test"
    public_key = (3233, 17)
    hash_value = 416
    signature_int = pow(hash_value, 2753, 3233)
    signature = signature_int.to_bytes(2, 'big')
    assert verify_digital_signature(message, signature, public_key) is True

def test_invalid_signature():
    message = b"Test"
    public_key = (3233, 17)
    hash_value = 416
    signature_int = pow(hash_value, 2753, 3233)
    signature = signature_int.to_bytes(2, 'big')
    tampered = bytearray(signature)
    tampered[0] ^= 0x01
    assert verify_digital_signature(message, bytes(tampered), public_key) is False

def test_corrupted_signature():
    message = b"Another message"
    public_key = (3233, 17)
    corrupted_signature = b"\x00"
    assert verify_digital_signature(message, corrupted_signature, public_key) is False

def test_empty_message_signature():
    message = b""
    public_key = (3233, 17)
    signature = (0).to_bytes(1, 'big')
    assert verify_digital_signature(message, signature, public_key) is True
