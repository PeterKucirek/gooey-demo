from pathlib import Path
from balsa import read_mdf
import pandas as pd
from argparse import ArgumentParser


def run(parent_folder: Path):
    tiprs_folder = parent_folder / "Trip Matrices"
    results = {}
    for p in tiprs_folder.iterdir():
        if p.suffix != '.mdf': continue
        print(p.stem)

        matrix = read_mdf(p)
        matrix_total = matrix.sum().sum()
        results[p.stem] = matrix_total
    results = pd.Series(results)

    results.index.name = 'matrix_name'
    results.name = 'total_trips'
    results.to_csv(parent_folder / "demo_matrix_summaries.csv", index=True, header=True)


def main():
    parser = ArgumentParser()
    parser.add_argument("output_folder", type=Path, help="The output folder to analyze", widget='DirChooser')
    args = parser.parse_args()

    run(args.output_folder)


if __name__ == '__main__':
    main()

