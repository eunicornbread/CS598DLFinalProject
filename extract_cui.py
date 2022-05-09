from pymetamap import MetaMapLite
import pandas as pd
import os
import argparse
from sklearn.utils import shuffle

METAMAP_LITE_DIR = "/mnt/c/Users/eunic/git-repos/cs598dl/public_mm_lite/"

# Run this file to extract CUIs from clinical notes

def extract_cui(text): 
    concepts,error = mm.extract_concepts([text],[1])

    return " ".join([concept[4] for concept in concepts])

def parse_arguments(parser):
    """Read user arguments"""
    parser.add_argument(
	    "--noteevents_file", type=str, default='./NOTEEVENTS.csv', help="File path to MIMIC-III dataset NOTEEVENTS.csv"
	)
    parser.add_argument(
	    "--output_dir", type=str, default='./output/', help="Path to directory to save all the output files"
	)
    parser.add_argument(
        "--metamap_lite_dir", type=str, help="Directory path to metamap lite"
    )
    parser.add_argument(
        "--max_rows", type=int, default=1000, help="Maximum number of rows to extract"
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
		formatter_class=argparse.ArgumentDefaultsHelpFormatter
	)
    ARGS = parse_arguments(PARSER)
    
    df = pd.read_csv(ARGS.noteevents_file)
    df = df[~pd.isnull(df['CHARTTIME'])]
    df = df[:ARGS.max_rows]

    os.chdir(ARGS.metamap_lite_dir)
    mm = MetaMapLite.get_instance(ARGS.metamap_lite_dir)

    # observation is a list of spaced separated UMLS CUIs
    df["observations"] = df['TEXT'].apply(lambda x: extract_cui(x))
    df = df[["SUBJECT_ID", "HADM_ID", "CHARTTIME", "observations"]]
    df = df.rename(columns={
        "SUBJECT_ID": "subject_id", 
        "HADM_ID": "hadm_id", 
        "CHARTTIME": "timestamp"
        })

    df = shuffle(df)
    r, _ = df.shape

    df.to_csv(ARGS.output_dir + "chronologies.csv", index=False)
    df[:int(0.8 * r)].to_csv(ARGS.output_dir + "train.chronologies.csv", index=False)
    df[int(0.8 * r):int(0.9 * r)].to_csv(ARGS.output_dir + "devel.chronologies.csv", index=False)
    df[int(0.9 * r):].to_csv(ARGS.output_dir + "test.chronologies.csv", index=False)