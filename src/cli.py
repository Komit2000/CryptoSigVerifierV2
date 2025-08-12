import argparse
import json
from .core import eth_utils
from .performance import benchmark

def main():
    parser = argparse.ArgumentParser(description='CryptoSigVerifier CLI')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Key generation command
    key_parser = subparsers.add_parser('generate-keys', help='Generate Ethereum key pair')
    
    # Signing command
    sign_parser = subparsers.add_parser('sign', help='Sign a message')
    sign_parser.add_argument('-m', '--message', required=True, help='Message to sign')
    sign_parser.add_argument('-p', '--private-key', required=True, help='Private key for signing')
    
    # Verification command
    verify_parser = subparsers.add_parser('verify', help='Verify a signature')
    verify_parser.add_argument('-m', '--message', required=True, help='Original message')
    verify_parser.add_argument('-s', '--signature', required=True, help='Signature to verify')
    verify_parser.add_argument('-a', '--address', required=True, help='Signer address')
    
    # Benchmark command
    bench_parser = subparsers.add_parser('benchmark', help='Run performance benchmarks')
    bench_parser.add_argument('-i', '--iterations', type=int, default=1000, help='Number of iterations')
    
    args = parser.parse_args()
    
    if args.command == 'generate-keys':
        keypair = eth_utils.generate_eth_keypair()
        print(json.dumps(keypair, indent=2))
    
    elif args.command == 'sign':
        result = eth_utils.eth_sign_message(args.message, args.private_key)
        print(json.dumps(result, indent=2))
    
    elif args.command == 'verify':
        valid = eth_utils.eth_verify_signature(
            args.message,
            args.signature,
            args.address
        )
        print(f"Signature valid: {valid}")
    
    elif args.command == 'benchmark':
        print(f"Running benchmarks with {args.iterations} iterations...")
        results = benchmark.run_benchmark(args.iterations)
        print("\nBenchmark results (ms):")
        for op, times in results.items():
            print(f"- {op}: avg={np.mean(times):.4f}, min={np.min(times):.4f}, max={np.max(times):.4f}")

if __name__ == "__main__":
    main()
