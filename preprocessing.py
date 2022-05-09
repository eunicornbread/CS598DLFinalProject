import pandas as pd
import argparse

METAMAP_LITE_DIR = "/mnt/c/Users/eunic/git-repos/cs598dl/public_mm_lite/"

# Run this file to prepare chronologies, admittimes, and labels

def parse_arguments(parser):
    """Read user arguments"""
    parser.add_argument(
	    "--data_dir", type=str, default='./data/', help="Path to directory that contains all the input data files"
	)
    parser.add_argument(
	    "--output_dir", type=str, default='./output/', help="Path to directory to save all the output files"
	)
    parser.add_argument(
        "--chronology_dir", type=str, default="./", help="Path to directory that contains all the chronology files"
    )
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
		formatter_class=argparse.ArgumentDefaultsHelpFormatter
	)
    ARGS = parse_arguments(PARSER)
    
    # Process ADMISSIONS.csv
    admissions = pd.read_csv(ARGS.data_dir + "./ADMISSIONS.csv")
    admissions = admissions[["SUBJECT_ID", "HADM_ID", "ADMITTIME"]]
    admissions = admissions.rename(columns={
        "SUBJECT_ID": "subject_id", 
        "HADM_ID": "hadm_id", 
        "ADMITTIME": "timestamp"
        })

    
    # Process PATIENTS.csv
    patients = pd.read_csv(ARGS.data_dir + "./PATIENTS.csv")
    patients['label'] = (~pd.isnull(patients.head()['DOD'])).astype(int)
    patients = patients[["SUBJECT_ID", "label"]]
    patients = patients.rename(columns={"SUBJECT_ID": "subject_id"})
    
    # Prepare labels.csv
    labels = pd.merge(patients, admissions, on="subject_id")
    labels = labels[["subject_id","hadm_id","timestamp","label"]]
    labels['label'] = labels['label'].fillna(0)
    labels['label'] = labels['label'].astype(int)

   
    # Read in chronology.csv
    chronologies = pd.read_csv(ARGS.chronology_dir + "chronologies.csv")
    test_chronologies = pd.read_csv(ARGS.chronology_dir + "test.chronologies.csv")
    train_chronologies = pd.read_csv(ARGS.chronology_dir + "train.chronologies.csv")
    devel_chronologies = pd.read_csv(ARGS.chronology_dir + "devel.chronologies.csv")


    # Prepare chronology files
    test_chronologies = test_chronologies.groupby(["hadm_id"]).agg({'subject_id': 'min', 'timestamp': 'max', 'observations': lambda x: " ".join(x)}).reset_index("hadm_id")
    test_chronologies = test_chronologies[['subject_id', 'hadm_id', 'timestamp', 'observations']]
    test_chronologies.to_csv(ARGS.output_dir + "test.chronologies.csv", index=False)

    train_chronologies['observations'] = train_chronologies['observations'].apply(lambda x: str(x))
    train_chronologies = train_chronologies.groupby(["hadm_id"]).agg({'subject_id': 'min', 'timestamp': 'max', 'observations': lambda x: " ".join(x)}).reset_index("hadm_id")
    train_chronologies = train_chronologies[['subject_id', 'hadm_id', 'timestamp', 'observations']]
    train_chronologies.to_csv(ARGS.output_dir + "train.chronologies.csv", index=False)

    devel_chronologies = devel_chronologies.groupby(["hadm_id"]).agg({'subject_id': 'min', 'timestamp': 'max', 'observations': lambda x: " ".join(x)}).reset_index("hadm_id")
    devel_chronologies = devel_chronologies[['subject_id', 'hadm_id', 'timestamp', 'observations']]
    devel_chronologies.to_csv(ARGS.output_dir + "devel.chronologies.csv", index=False)


    # Prepare admittimes files
    test_admittimes = pd.merge(test_chronologies[["subject_id", "hadm_id"]], admissions, on=["subject_id", "hadm_id"])
    test_admittimes.to_csv(ARGS.output_dir + "test.admittimes.csv", index=False)

    train_admittimes = pd.merge(train_chronologies[["subject_id", "hadm_id"]], admissions, on=["subject_id", "hadm_id"])
    train_admittimes.to_csv(ARGS.output_dir + "train.admittimes.csv", index=False)

    devel_admittimes = pd.merge(devel_chronologies[["subject_id", "hadm_id"]], admissions, on=["subject_id", "hadm_id"])
    devel_admittimes.to_csv(ARGS.output_dir + "devel.admittimes.csv", index=False)


    # Prepare labels files
    test_labels = pd.merge(test_chronologies[["subject_id", "hadm_id"]], labels, on=["subject_id", "hadm_id"])
    test_labels.to_csv(ARGS.output_dir + "test.labels.csv", index=False)

    train_labels = pd.merge(train_chronologies[["subject_id", "hadm_id"]], labels, on=["subject_id", "hadm_id"])
    train_labels.to_csv(ARGS.output_dir + "train.labels.csv", index=False)

    devel_labels = pd.merge(devel_chronologies[["subject_id", "hadm_id"]], labels, on=["subject_id", "hadm_id"])
    devel_labels.to_csv(ARGS.output_dir + "devel.labels.csv", index=False)