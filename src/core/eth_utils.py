import os
import json
from eth_keys import keys
from eth_utils import keccak, to_checksum_address

def generate_eth_keypair():
    """Generate Ethereum-compatible key pair (private key, public key, address)"""
    private_key_bytes = os.urandom(32)
    private_key = keys.PrivateKey(private_key_bytes)
    public_key = private_key.public_key
    address = to_checksum_address(public_key.to_address())
    return {
        'private_key': private_key.to_hex(),
        'public_key': public_key.to_hex(),
        'address': address
    }

def eth_sign_message(message: str, private_key_hex: str) -> dict:
    """Sign message with Ethereum private key (EIP-191 personal_sign)"""
    # Remove '0x' prefix if present
    if private_key_hex.startswith('0x'):
        private_key_hex = private_key_hex[2:]
    
    private_key = keys.PrivateKey(bytes.fromhex(private_key_hex))
    message_bytes = message.encode('utf-8')
    
    # Ethereum-specific signing (personal_sign)
    prefix = f"\x19Ethereum Signed Message:\n{len(message_bytes)}".encode()
    signable_message = keccak(prefix + message_bytes)
    signature = private_key.sign_msg_hash(signable_message)
    
    return {
        'message': message,
        'signature': '0x' + signature.to_bytes().hex(),
        'v': signature.v,
        'r': hex(signature.r),
        's': hex(signature.s)
    }

def eth_verify_signature(message: str, signature_hex: str, address: str) -> bool:
    """Verify Ethereum signature (EIP-191 personal_sign)"""
    # Prepare message with Ethereum prefix
    message_bytes = message.encode('utf-8')
    prefix = f"\x19Ethereum Signed Message:\n{len(message_bytes)}".encode()
    signable_message = keccak(prefix + message_bytes)
    
    # Decode signature
    if signature_hex.startswith('0x'):
        signature_hex = signature_hex[2:]
    signature_bytes = bytes.fromhex(signature_hex)
    signature = keys.Signature(signature_bytes=signature_bytes)
    
    # Recover public key
    public_key = signature.recover_public_key_from_msg_hash(signable_message)
    recovered_address = to_checksum_address(public_key.to_address())
    
    return recovered_address.lower() == address.lower()
