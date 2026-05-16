import pandas as pd
import numpy as np
import glob

files = glob.glob("./data/*.csv")
df_list = []

# loading and cleaning headers
for f in files:
    print(f"Reading:: {f.split('/')[-1]}")
    temp_df = pd.read_csv(f)

    # taking out whitespace from headers
    temp_df.columns = temp_df.columns.str.strip()
    df_list.append(temp_df)

# concatenating
combined_df = pd.concat(df_list, ignore_index= True)
print(f"Successfully combined {len(combined_df):,} rows.")

# handeling infinity and NaNs
combined_df.replace([np.inf, -np.inf], np.nan, inplace=True)
combined_df.fillna(combined_df.median(numeric_only=True), inplace=True)

# output 10% only
sample_df = combined_df.sample(frac=1, random_state=42)
sample_df.to_csv("CTSA_cleaned_whole.csv", index=False)
print("Sample created")


