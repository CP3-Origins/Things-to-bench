import os
import logging
from cp3bench.bench.evaluate_dataset import evaluate_dataset

PATH = os.path.dirname(os.path.abspath(__file__))

TRAINING_DATASETS = [
    "F1.csv",
    "F2.csv",
    "F3.csv",
    "F4.csv",
    "F5.csv",
    "F6.csv",
    "F7.csv",
    "F8.csv",
]

COSMO_DATASETS= [
    "C1a.csv",
    "C1b.csv",
    "C1c.csv",
    "C1d.csv",
    "C2a.csv",
    "C5f.csv",
    "C2b.csv",
    "C3a.csv",
    "C3b.csv",
    "C3c.csv",
    "C3d.csv",
    "C3e.csv",
    "C3f.csv",
    "C3g.csv",
    "C3h.csv",
    "C4a.csv",
    "C4b.csv",
    "C4c.csv",
    "C4d.csv",
    "C4e.csv",
    "C5a.csv",
    "C5b.csv",
    "C5c.csv",
    "C5d.csv",
    "C5e.csv",
    "C6a.csv",
    "C6b.csv",
    "C6c.csv",
]

if __name__ == "__main__":
    for dataset in COSMO_DATASETS:
        if "error" not in dataset:
            logging.info(f"Evaluating {dataset}")
            evaluate_dataset(f"{PATH}/cosmo_data/{dataset}")
