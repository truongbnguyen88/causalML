"""
Download LaLonde NSW dataset from NBER.

This script downloads the LaLonde job training dataset used in:
- Lalonde, R. (1986). "Evaluating the Econometric Evaluations of Training Programs"
- Dehejia, R. and Wahba, S. (1999). "Causal Effects in Non-Experimental Studies"

Data source: http://users.nber.org/~rdehejia/data/
"""

import urllib.request
import pandas as pd

# Column names for the dataset
COLUMNS = ['treat', 'age', 'education', 'black', 'hispanic', 'married',
           'nodegree', 're74', 're75', 're78']

def download_file(url, filename):
    """Download file from URL."""
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, filename)
        print(f"[OK] Downloaded {filename}")
        return True
    except Exception as e:
        print(f"[FAIL] Failed to download {filename}: {e}")
        return False

def load_and_save_csv(txt_file, csv_file, treat_value):
    """Load text file and save as CSV with proper column names."""
    try:
        # Read the text file (space-separated)
        df = pd.read_csv(txt_file, sep=r'\s+', header=None, names=COLUMNS[1:])
        # Add treatment indicator
        df.insert(0, 'treat', treat_value)
        # Save as CSV
        df.to_csv(csv_file, index=False)
        print(f"[OK] Converted {txt_file} to {csv_file} ({len(df)} rows)")
        return df
    except Exception as e:
        print(f"[FAIL] Failed to process {txt_file}: {e}")
        return None

if __name__ == "__main__":
    base_url = "http://www.nber.org/~rdehejia/data/"

    # Download NSW Dehejia-Wahba sample (with RE74 data)
    files_to_download = [
        ("nswre74_treated.txt", "nsw_dw_treated.txt"),
        ("nswre74_control.txt", "nsw_dw_control.txt"),
        ("psid_controls.txt", "psid_controls.txt"),
    ]

    for source, dest in files_to_download:
        url = base_url + source
        download_file(url, dest)

    # Convert to CSV
    print("\nConverting to CSV format...")
    df_treated = load_and_save_csv("nsw_dw_treated.txt", "nsw_treated.csv", treat_value=1)
    df_control = load_and_save_csv("nsw_dw_control.txt", "nsw_control.csv", treat_value=0)
    df_psid = load_and_save_csv("psid_controls.txt", "psid_controls.csv", treat_value=0)

    # Combine NSW experimental data
    if df_treated is not None and df_control is not None:
        df_nsw = pd.concat([df_treated, df_control], ignore_index=True)
        df_nsw.to_csv("nsw_experimental.csv", index=False)
        print(f"[OK] Created nsw_experimental.csv ({len(df_nsw)} rows)")

    # Combine treated with PSID controls (observational setting)
    if df_treated is not None and df_psid is not None:
        df_obs = pd.concat([df_treated, df_psid], ignore_index=True)
        df_obs.to_csv("nsw_psid_observational.csv", index=False)
        print(f"[OK] Created nsw_psid_observational.csv ({len(df_obs)} rows)")

    print("\n" + "="*60)
    print("Dataset download complete!")
    print("="*60)
    print("\nFiles created:")
    print("  - nsw_treated.csv: NSW treated units (185 obs)")
    print("  - nsw_control.csv: NSW control units (260 obs)")
    print("  - nsw_experimental.csv: Combined experimental data (445 obs)")
    print("  - psid_controls.csv: PSID control units (2,490 obs)")
    print("  - nsw_psid_observational.csv: Observational setting (2,675 obs)")
