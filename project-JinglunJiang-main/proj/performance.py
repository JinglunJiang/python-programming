import sys
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from markov import identify_speaker

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print(
            f"Usage: python3 {sys.argv[0]} <filenameA> <filenameB> <filenameC> <max-k> <runs>"
        )
        sys.exit(1)

    # extract parameters from command line & convert types
    filenameA, filenameB, filenameC, max_k, runs = sys.argv[1:]
    max_k = int(max_k)
    runs = int(runs)

    # TODO: add code here to open files & read text
    with open(filenameA, 'r') as file:
        speech1 = file.read()
    with open(filenameB, 'r') as file:
        speech2 = file.read()
    with open(filenameC, 'r') as file:
        speech3 = file.read()

    # TODO: run performance tests as outlined in README.md
    results = []

    for use_hashtable in [True, False]:
        for k in range(1, max_k + 1):
            sum_time = 0
            for run in range(1, runs + 1):
                start = time.perf_counter()
                identify_speaker(speech1, speech2, speech3, k, use_hashtable)
                elapsed = time.perf_counter() - start
                sum_time += elapsed
            
            avg_time = sum_time / runs
            results.append(("hashtable" if use_hashtable else "dict", k, avg_time))

    df = pd.DataFrame(results, columns=['Implementation', 'K', 'Time'])

    # TODO: write execution_graph.png
    sns.set(style="whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    plt.figure(figsize=(10, 6))
    sns.pointplot(data=df, x='K', y='Time', hue='Implementation', linestyle='-', marker='o')
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.title('HashTable vs Python dict')
    plt.xlabel('K')
    plt.ylabel(f'Average Time (Runs={runs})')
    plt.savefig('execution_graph.png')
