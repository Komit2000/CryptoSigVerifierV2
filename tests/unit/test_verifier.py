"""Unit tests for signature verification"""

import unittest
from src.core import signer, verifier

class TestVerifier(unittest.TestCase):
    def test_valid_signature(self):
        """Test verification of valid signature"""
        # Generate key pair
        keypair = signer.generate_keypair()
        message = "Test message"
        
        # Sign message
        signature_data = signer.sign_message(message, keypair['private_key'])
        
        # Verify signature
        self.assertTrue(verifier.verify_signature(
            message,
            signature_data['signature'],
            signature_data['public_key']
        ))
    
    def test_invalid_signature(self):
        """Test detection of invalid signature"""
        # Generate key pair
        keypair = signer.generate_keypair()
        message = "Test message"
        
        # Sign message
        signature_data = signer.sign_message(message, keypair['private_key'])
        
        # Corrupt the signature
        corrupted_signature = signature_data['signature'][:-2] + "ff"
        
        # Verify should fail
        self.assertFalse(verifier.verify_signature(
            message,
            corrupted_signature,
            signature_data['public_key']
        ))
    
    def test_wrong_message(self):
        """Test detection of signature for wrong message"""
        # Generate key pair
        keypair = signer.generate_keypair()
        message = "Original message"
        
        # Sign message
        signature_data = signer.sign_message(message, keypair['private_key'])
        
        # Verify with different message
        self.assertFalse(verifier.verify_signature(
            "Modified message",
            signature_data['signature'],
            signature_data['public_key']
        ))
