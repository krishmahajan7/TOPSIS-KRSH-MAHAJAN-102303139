import sys
sys.path.insert(0, r'c:\Users\DELL\Desktop\Predictive Analysis\topsis\TOPSIS-KRISH-MAHAJAN')

# Import the topsis function
from topsis1 import topsis
import pandas as pd

print("=" * 60)
print("TOPSIS Analysis on Laptop Comparison Data")
print("=" * 60)

# Run TOPSIS analysis
topsis(
    input_file=r'c:\Users\DELL\Desktop\Predictive Analysis\topsis\example_data.csv',
    weights='2,1,2,2',  # Price (2x weight), Battery, Camera (2x), Performance (2x)
    impacts='-,+,+,+',  # Price is cost (-), others are benefit (+)
    result_file=r'c:\Users\DELL\Desktop\Predictive Analysis\topsis\example_results.csv'
)

print("\nAnalysis Complete!")
print("\nResults saved to: example_results.csv")

# Display the results
print("\n" + "=" * 60)
print("TOPSIS Results:")
print("=" * 60)
results = pd.read_csv(r'c:\Users\DELL\Desktop\Predictive Analysis\topsis\example_results.csv')
print(results.to_string(index=False))

print("\n" + "=" * 60)
print("Interpretation:")
print("=" * 60)
for idx, row in results.iterrows():
    print(f"Rank {int(row['Rank'])}: {row['Product']} (TOPSIS Score: {row['Topsis_Score']:.4f})")


