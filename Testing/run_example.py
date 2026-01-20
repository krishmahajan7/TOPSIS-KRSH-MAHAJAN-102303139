import pandas as pd
import numpy as np
import sys
import os

os.chdir(r'c:\Users\DELL\Desktop\Predictive Analysis\topsis')

# ERROR FUNCTION 
def error(msg):
    print("Error:", msg)
    sys.exit(1)

# MAIN TOPSIS FUNCTION 
def topsis(input_file, weights, impacts, result_file):

    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        error("Input file not found")

    if data.shape[1] < 3:
        error("Input file must contain at least 3 columns")

    alternatives = data.iloc[:, 0]
    matrix = data.iloc[:, 1:].copy()

    try:
        matrix = matrix.astype(float).values
    except:
        error("Columns from 2nd to last must contain numeric values only")

    if isinstance(weights, str):
        weights = weights.split(',')

    if isinstance(impacts, str):
        impacts = impacts.split(',')

    if len(weights) != matrix.shape[1]:
        error("Number of weights must match number of criteria columns")

    if len(impacts) != matrix.shape[1]:
        error("Number of impacts must match number of criteria columns")

    try:
        weights = np.array(weights, dtype=float)
    except:
        error("Weights must be numeric and separated by commas")

    for imp in impacts:
        if imp not in ['+', '-']:
            error("Impacts must be either + or - and separated by commas")

    impacts = np.array(impacts)

    # Step 1 Normalize
    norm = np.sqrt((matrix**2).sum(axis=0))
    normalized = matrix / norm

    # Step 2 Weighted normalization
    weighted = normalized * weights

    # Step 3 Ideal best & worst
    ideal_best = []
    ideal_worst = []

    for j in range(weighted.shape[1]):
        if impacts[j] == '+':
            ideal_best.append(weighted[:, j].max())
            ideal_worst.append(weighted[:, j].min())
        else:
            ideal_best.append(weighted[:, j].min())
            ideal_worst.append(weighted[:, j].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # Step 4 Distance
    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5 Score
    score = dist_worst / (dist_best + dist_worst)

    data['Topsis_Score'] = score
    data['Rank'] = pd.Series(score).rank(ascending=False).astype(int)

    data.to_csv(result_file, index=False)

    print("\n" + "="*60)
    print("TOPSIS Analysis Results")
    print("="*60)
    print(data.to_string(index=False))
    print("\n" + "="*60)
    print("Analysis Summary:")
    print("="*60)
    print(f"Total alternatives: {len(data)}")
    print(f"Total criteria: {matrix.shape[1]}")
    print(f"\nRanking (from best to worst):")
    ranked = data.sort_values('Rank')
    for idx, row in ranked.iterrows():
        print(f"  Rank {int(row['Rank'])}: {row['Product']} (Score: {row['Topsis_Score']:.4f})")
    print(f"\nResults saved to: {result_file}")

# Run TOPSIS
topsis('example_data.csv', '2,1,2,2', '-,+,+,+', 'example_results.csv')
