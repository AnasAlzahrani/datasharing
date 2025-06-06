import pandas as pd

RAW_PATH = "data/raw_sample.csv"
TIDY_PATH = "data/tidy_sample.csv"
CODEBOOK_PATH = "data/codebook.md"


def main():
    # Read raw data
    raw = pd.read_csv(RAW_PATH)

    # Convert to tidy format
    tidy = pd.melt(raw, id_vars=["ID", "Gender"], var_name="Day", value_name="Weight")
    tidy["Day"] = tidy["Day"].str.extract("Day(\d+)").astype(int)
    tidy.sort_values(["ID", "Day"], inplace=True)

    # Save tidy dataset
    tidy.to_csv(TIDY_PATH, index=False)

    # Write a simple codebook
    codebook_lines = [
        "# Codebook",
        "",
        "## Variables",
        "- `ID`: unique patient identifier (integer)",
        "- `Gender`: patient gender (`M` or `F`)",
        "- `Day`: day of measurement (integer)",
        "- `Weight`: weight measured in kg (numeric)"
    ]
    with open(CODEBOOK_PATH, "w") as f:
        f.write("\n".join(codebook_lines))

    # Reproducibility check
    tidy_again = pd.melt(raw, id_vars=["ID", "Gender"], var_name="Day", value_name="Weight")
    tidy_again["Day"] = tidy_again["Day"].str.extract("Day(\d+)").astype(int)
    tidy_again.sort_values(["ID", "Day"], inplace=True)

    if tidy.equals(tidy_again):
        print("Reproducibility check passed.")
    else:
        print("Reproducibility check failed.")


if __name__ == "__main__":
    main()
