"""
Utility functions for loading LaLonde dataset.

Usage:
    from datasets.lalonde.load_lalonde import load_lalonde_experimental, load_lalonde_observational

    df_exp = load_lalonde_experimental()
    df_obs = load_lalonde_observational()
"""

import pandas as pd
import numpy as np
from pathlib import Path

def get_lalonde_path():
    """Get the path to the lalonde dataset directory."""
    # Try to find the datasets directory
    current = Path.cwd()

    # Check common locations
    candidates = [
        current / 'datasets' / 'lalonde',
        current.parent / 'datasets' / 'lalonde',
        current.parent.parent / 'datasets' / 'lalonde',
    ]

    for path in candidates:
        if path.exists():
            return path

    # Default to relative path
    return Path('datasets/lalonde')

def load_lalonde_experimental():
    """
    Load the LaLonde experimental dataset (NSW randomized experiment).

    Returns
    -------
    pd.DataFrame
        Dataset with 445 observations (185 treated, 260 control)
    """
    base_path = get_lalonde_path()
    file_path = base_path / 'nsw_experimental.csv'

    if not file_path.exists():
        raise FileNotFoundError(
            f"LaLonde experimental data not found at {file_path}\n"
            f"Please run: python datasets/lalonde/download_data.py"
        )

    return pd.read_csv(file_path)

def load_lalonde_observational():
    """
    Load the LaLonde observational dataset (NSW treated + PSID controls).

    This dataset has confounding because PSID controls differ systematically
    from NSW participants in demographics and prior earnings.

    Returns
    -------
    pd.DataFrame
        Dataset with 2,675 observations (185 treated, 2,490 PSID controls)
    """
    base_path = get_lalonde_path()
    file_path = base_path / 'nsw_psid_observational.csv'

    if not file_path.exists():
        raise FileNotFoundError(
            f"LaLonde observational data not found at {file_path}\n"
            f"Please run: python datasets/lalonde/download_data.py"
        )

    return pd.read_csv(file_path)

def describe_lalonde():
    """Print information about the LaLonde dataset."""
    print("="*70)
    print("LaLonde Job Training Dataset")
    print("="*70)
    print("\nVariables:")
    print("  - treat: Treatment indicator (1=NSW program, 0=control)")
    print("  - age: Age in years")
    print("  - education: Years of schooling")
    print("  - black: 1 if Black, 0 otherwise")
    print("  - hispanic: 1 if Hispanic, 0 otherwise")
    print("  - married: 1 if married, 0 otherwise")
    print("  - nodegree: 1 if no high school degree, 0 otherwise")
    print("  - re74: Real earnings in 1974 (pre-treatment)")
    print("  - re75: Real earnings in 1975 (pre-treatment)")
    print("  - re78: Real earnings in 1978 (outcome)")
    print("\nKnown Results:")
    print("  - Experimental ATE ≈ $1,794 (Lalonde 1986)")
    print("  - This is the 'true' causal effect from randomization")
    print("\nFor more info: See datasets/lalonde/README.md")
    print("="*70)

if __name__ == "__main__":
    describe_lalonde()

    try:
        df_exp = load_lalonde_experimental()
        print(f"\n✓ Experimental data loaded: {len(df_exp)} observations")
        print(f"  - Treated: {df_exp['treat'].sum()}")
        print(f"  - Control: {len(df_exp) - df_exp['treat'].sum()}")
    except FileNotFoundError as e:
        print(f"\n✗ {e}")

    try:
        df_obs = load_lalonde_observational()
        print(f"\n✓ Observational data loaded: {len(df_obs)} observations")
        print(f"  - Treated: {df_obs['treat'].sum()}")
        print(f"  - Control: {len(df_obs) - df_obs['treat'].sum()}")
    except FileNotFoundError as e:
        print(f"\n✗ {e}")
