# CryptoSigVerifier 🔐

Professional toolkit for cryptographic signature operations with Ethereum support

[![CI Status](https://github.com/komit2000/CryptoSigVerifierV2/workflows/CI/badge.svg)](https://github.com/komit2000/CryptoSigVerifierV2/actions)
[![Docker Image](https://img.shields.io/docker/v/komit2000/CryptoSigVerifierV2?sort=semver)](https://hub.docker.com/r/komit2000/CryptoSigVerifierV2)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features ✨
- ✅ Ethereum-compatible key generation (secp256k1)
- ✅ EIP-191 message signing and verification
- ⚡ Performance benchmarking
- 🐳 Docker support
- 📊 Automated CI/CD

## Installation
```bash
# Clone repository
git clone https://github.com/komit2000/CryptoSigVerifierV2.git
cd CryptoSigVerifierV2

# Install dependencies
pip install -r requirements.txt


## Features ✨
- ✅ Ethereum-compatible key generation (secp256k1)
- ✅ EIP-191 message signing and verification
- ⚡ Performance benchmarking
- 🐳 Docker support
- 📊 Automated CI/CD


# Install dependencies
pip install -r requirements.txt
Usage
bash
# Generate Ethereum key pair
python -m src.cli generate-keys

# Sign message
python -m src.cli sign -m "Hello Crypto" -p <private_key>

# Verify signature
python -m src.cli verify -m "Hello Crypto" -s <signature> -a <address>

# Run benchmarks (default: 1000 iterations)
python -m src.cli benchmark --iterations 5000
Docker Support
bash
# Build image
docker build -t cryptosigverifier .

# Run commands
docker run cryptosigverifier generate-keys
docker run cryptosigverifier sign -m "Test" -p 0x...
Performance Example
https://docs/benchmark_example.png

Support the Project ❤️
Your sponsorship helps make this project better:

GitHub Sponsors
Sponsor via GitHub

Crypto Payments
ETH: 0xE578FfE7e3c05e1dbd2D68e72440cd77fac40329

USDC (BEP20): 0x6b0c18ba0c30556fc16c38c43f6207ea339a1773

USDT (TRC20): TP5mibvk4X7Spmmm9hSvJZ1Fy3n93PunQi

BTC: 143x835kXPxWoFR7q8DQJdVXjmw57Nche2

License
MIT License - see LICENSE for details.

text

**requirements.txt**
```text
eth-keys==0.5.0
eth-utils==2.3.1
tqdm==4.66.2
matplotlib==3.8.2
numpy==1.26.4


## Quick Crypto Support

I create professional cryptography tools. Support my open-source project!

Send ETH to: 0xE578FfE7e3c05e1dbd2D68e72440cd77fac40329

USDC (BEP20) to: 0x6b0c18ba0c30556fc16c38c43f6207ea339a1773

USDT (TRC20) to: TP5mibvk4X7Spmmm9hSvJZ1Fy3n93PunQi

BTC to: 143x835kXPxWoFR7q8DQJdVXjmw57Nche2

SOL to: G21J7jW7VTJxwtGNwB4yAJo22hSAq4rkdmRWAJPkVJrX
