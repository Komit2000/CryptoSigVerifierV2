"""Main package for CryptoSigVerifier"""

# Export public API
from .core.signer import generate_keypair, sign_message
from .core.verifier import verify_signature
from .core.eth_utils import generate_eth_keypair, eth_sign_message, eth_verify_signature
from .performance.benchmark import run_benchmark
