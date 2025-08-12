"""Unit tests for signature generation"""

import unittest
from src.core import signer

class TestSigner(unittest.TestCase):
    def test_keypair_generation(self):
        """Test generation of valid key pairs"""
        keypair = signer.generate_keypair()
        
        # Check keys have correct lengths
        self.assertEqual(len(keypair['private_key']), 64)  # 32 bytes in hex
        self.assertEqual(len(keypair['public_key']), 128)  # 64 bytes in hex
    
    def test_message_signing(self):
        """Test message signing produces valid signature"""
        keypair = signer.generate_keypair()
        message = "Test message"
        
        signature_data = signer.sign_message(message, keypair['private_key'])
        
        # Check all required fields are present
        self.assertIn('message', signature_data)
        self.assertIn('signature', signature_data)
        self.assertIn('public_key', signature_data)
        
        # Check signature length (typically 70-72 bytes in hex)
        self.assertTrue(128 <= len(signature_data['signature']) <= 144)
