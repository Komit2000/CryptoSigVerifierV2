import time
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from ..core import eth_utils

def run_benchmark(iterations=1000):
    """Run performance benchmarks for cryptographic operations"""
    results = {
        'key_generation': [],
        'signing': [],
        'verification': []
    }
    
    # Generate test data
    test_message = "Benchmark test message"
    keypair = eth_utils.generate_eth_keypair()
    
    # Benchmark key generation
    print("Benchmarking key generation...")
    for _ in tqdm(range(iterations)):
        start = time.perf_counter_ns()
        eth_utils.generate_eth_keypair()
        results['key_generation'].append(time.perf_counter_ns() - start)
    
    # Benchmark signing
    print("Benchmarking message signing...")
    for _ in tqdm(range(iterations)):
        start = time.perf_counter_ns()
        eth_utils.eth_sign_message(test_message, keypair['private_key'])
        results['signing'].append(time.perf_counter_ns() - start)
    
    # Benchmark verification
    signature = eth_utils.eth_sign_message(test_message, keypair['private_key'])
    print("Benchmarking signature verification...")
    for _ in tqdm(range(iterations)):
        start = time.perf_counter_ns()
        eth_utils.eth_verify_signature(
            test_message,
            signature['signature'],
            keypair['address']
        )
        results['verification'].append(time.perf_counter_ns() - start)
    
    # Convert to milliseconds
    for key in results:
        results[key] = np.array(results[key]) / 1e6
    
    # Generate performance plot
    _generate_plot(results, iterations)
    return results

def _generate_plot(results, iterations):
    """Generate performance plot with error bars"""
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Prepare data
    labels = list(results.keys())
    means = [np.mean(data) for data in results.values()]
    stds = [np.std(data) for data in results.values()]
    
    # Create bar plot with error bars
    bars = ax.bar(labels, means, yerr=stds, capsize=5, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.2f} ms', ha='center', va='bottom')
    
    ax.set_title(f'Cryptographic Operations Performance ({iterations} iterations)')
    ax.set_ylabel('Time (milliseconds)')
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig('benchmark_results.png', dpi=300)
    print("Benchmark plot saved as 'benchmark_results.png'")
