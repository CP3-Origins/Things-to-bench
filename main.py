import os
import logging
from cp3-bench.bench.evaluate_dataset import evaluate_dataset

PATH = os.path.dirname(os.path.abspath(__file__))

TRAINING_DATASETS = [
    "Koza2_1000.csv",
    "Jin1.csv",
    "Jin4.csv",
    "Keijzer1_1000.csv",
    "Keijzer4_1000.csv",
    "Vladislavleva1.csv",
    "Korns2_N30.csv",
    "Korns8_N30.csv",
]

COSMO_DATASETS= [
    "C1.csv",
    "C2.csv",
    "C3.csv",
    "C4.csv",
    "C5.csv",
    "C6.csv",
    "C7.csv",
    "C8.csv",
    "C9.csv",
    "C10.csv",
    "C11.csv",
    "C12.csv",
    "C13.csv",
    "C14.csv",
    "C15.csv",
    "C16.csv",
    "C17.csv",
    "C18.csv",
    "C19.csv",
]

if __name__ == "__main__":
    for dataset in COSMO_DATASETS:
        if "error" not in dataset:
            logging.info(f"Evaluating {dataset}")
            evaluate_dataset(f"{PATH}/cosmo_data/{dataset}")
