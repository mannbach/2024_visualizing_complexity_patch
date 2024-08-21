import pandas as pd
import argparse

from netin.utils.constants import ERPATCH_MODEL_NAME
from patch_workshop.constants import MAP_MODEL_NAME_TO_GLOBAL

FILE_IN = "data/aggregate_statistics.csv"
FILE_OUT = "data/aggregate_statistics_vis.csv"

def parse_args():
    parser = argparse.ArgumentParser(description="Transform aggregate statistics")
    parser.add_argument("--file-in", type=str, default=FILE_IN)
    parser.add_argument("--file-out", type=str, default=FILE_OUT)
    return parser.parse_args()

def map_model_name_and_tcu_to_local(row: pd.Series) -> str:
    model_name = row["model_name"]
    tcu = row["tcu"]
    if tcu:
        return "random"
    return MAP_MODEL_NAME_TO_GLOBAL[model_name]

def main():
    args = parse_args()
    data = pd.read_csv(args.file_in)

    print(f"Read {len(data)} elements from {args.file_in}")
    print(data.head())

    data["global"] = data["model_name"]\
        .map(MAP_MODEL_NAME_TO_GLOBAL)
    data["local"] = data\
        .apply(map_model_name_and_tcu_to_local, axis=1)
    data = data[(data["model_name"] != ERPATCH_MODEL_NAME) | data["tcu"]]
    data = data.filter(
        ["global", "local", "h", "tc", "r", "gini", "ei", "stoch_dom"])

    data.to_csv(args.file_out, index=False)
    print(f"Wrote {len(data)} elements to {args.file_out}")

if __name__ == "__main__":
    main()
