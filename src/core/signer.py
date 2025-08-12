"""Module for generating cryptographic signatures"""

from ecdsa import SigningKey, SECP256k1
import hashlib

def generate_keypair():
    """Generate ECDSA key pair using secp256k1 curve"""
    # Create a new private key using secp256k1 curve (same as Bitcoin/Ethereum)
    private_key = SigningKey.generate(curve=SECP256k1)
    
    # Derive the public key from the private key
    public_key = private_key.get_verifying_key()
    
    return {
        'private_key': private_key.to_string().hex(),
        'public_key': public_key.to_string().hex()
    }

def sign_message(message: str, private_key_hex: str) -> dict:
    """Sign message with ECDSA private key"""
    # Recreate private key object from hex string
    private_key = SigningKey.from_string(bytes.fromhex(private_key_hex), curve=SECP256k1)
    
    # Hash the message using SHA-256
    message_hash = hashlib.sha256(message.encode()).digest()
    
    # Sign the message hash
    signature = private_key.sign(message_hash)
    
    return {
        'message': message,
        'signature': signature.hex(),
        'public_key': private_key.get_verifying_key().to_string().hex()
    }
