"""Integration tests for Ethereum-specific functionality"""

import unittest
from src.core.eth_utils import generate_eth_keypair, eth_sign_message, eth_verify_signature

class TestEthIntegration(unittest.TestCase):
    def test_ethereum_keypair(self):
        """Test generation of Ethereum-compatible key pair"""
        keypair = generate_eth_keypair()
        
        # Check keys have correct format
        self.assertTrue(keypair['private_key'].startswith('0x'))
        self.assertTrue(keypair['public_key'].startswith('0x'))
        self.assertTrue(keypair['address'].startswith('0x'))
        
        # Check address length (20 bytes)
        self.assertEqual(len(keypair['address']), 42)
    
    def test_ethereum_signing_verification(self):
        """Test Ethereum signing and verification flow"""
        keypair = generate_eth_keypair()
        message = "Ethereum test message"
        
        # Sign message
        signature_data = eth_sign_message(message, keypair['private_key'])
        
        # Check signature format
        self.assertTrue(signature_data['signature'].startswith('0x'))
        
        # Verify signature
        self.assertTrue(eth_verify_signature(
            message,
            signature_data['signature'],
            keypair['address']
        ))
    
    def test_ethereum_verification_failure(self):
        """Test Ethereum verification fails with wrong address"""
        keypair1 = generate_eth_keypair()
        keypair2 = generate_eth_keypair()
        message = "Ethereum test message"
        
        # Sign with keypair1
        signature_data = eth_sign_message(message, keypair1['private_key'])
        
        # Try to verify with keypair2's address
        self.assertFalse(eth_verify_signature(
            message,
            signature_data['signature'],
            keypair2['address']
        ))
