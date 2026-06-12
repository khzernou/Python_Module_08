import sys
import importlib.metadata as metadata


REQUIRED = {
    "numpy": "Numerical computation ready",
    "pandas": "Data manipulation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> bool:
    """check req package and print status/version"""
    print("Checking dependencies:")
    ok = True
    for name, desc in REQUIRED.items():
        try:
            version = metadata.version(name)
            print(f"[OK] {name} ({version}) - {desc}")
        except metadata.PackageNotFoundError:
            print(f"[MISSING] {name} - {desc}")
            ok = False
    return ok


def run_analysis() -> None:
    """generate matrix data with numpy, analyse w pandas, and plot it"""
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")
    raw_data = np.random.default_rng().normal(50, 15, size=1000)
    print(f"Processing {len(raw_data)} data points...")

    df = pd.DataFrame({"signal": raw_data})
    df["trend"] = df["signal"].rolling(window=10).mean()

    print("Generating visualization...")
    df.plot(title="Matrix Data Stream", figsize=(8, 4))
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def show_pip_vs_poetry() -> None:
    """briefly contrast pip and Poetry dependency managment"""
    print("\npip:    reads requirements.txt, "
          "no lock file, versions can drift.")
    print("Poetry: reads pyproject.toml + poetry.lock, reproducible installs.")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    if not check_dependencies():
        print("\n[ERROR] Missing required dependencies.")
        print("Install with pip:    pip install -r requirements.txt")
        print("Install with Poetry: poetry install")
        sys.exit(1)

    run_analysis()
    show_pip_vs_poetry()


if __name__ == "__main__":
    main()
