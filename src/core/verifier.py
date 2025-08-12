"""Module for verifying cryptographic signatures"""

from ecdsa import VerifyingKey, SECP256k1, BadSignatureError
import hashlib

def verify_signature(message: str, signature_hex: str, public_key_hex: str) -> bool:
    """Verify ECDSA signature"""
    try:
        # Recreate public key object from hex string
        public_key = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=SECP256k1)
        
        # Hash the message using SHA-256
        message_hash = hashlib.sha256(message.encode()).digest()
        
        # Verify the signature
        return public_key.verify(bytes.fromhex(signature_hex), message_hash)
    except (BadSignatureError, ValueError):
        return False
