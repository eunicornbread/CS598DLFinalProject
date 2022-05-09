# CS598 DL4H Paper Reproducibility Project

This is the codebase for my Paper Reproducibility Project for my CS598 DL4H class. The objective of this project is reproduce a research paper of our choice. The paper I choose is [A customizable deep learning model for nosocomial risk prediction from critical care notes with indirect supervision](https://www.researchgate.net/publication/339351290_A_customizable_deep_learning_model_for_nosocomial_risk_prediction_from_critical_care_notes_with_indirect_supervision) by Travis Goodwin and Dina Demner-Fushman. 

Although I was not able to reproduce the results from the paper, I would still like to provide the code to the progress I have made, so that it can provide helpful information for anyone else who may also want to reproduce this paper. This repo will focus on any intermediate results that I got, along with any challenge and roadblock I ran into, hopefully providing useful insights to the reproducibility of this paper. 

This page will be broken down into the following sections:

1. [Overview](#Overview)
2. [Datasets](#Datasets)
3. [Installation](#Installation)
3. [Data Preprocessing](#data-preprocessing)
4. Running the Model
5. [References](#References)


## Overview


The implementation CANTRIP, which is the novel model proposed by the paper, is publicly available at [https://github.com/h4ste/cantrip](https://github.com/h4ste/cantrip). However, the existing implementation does not include data preprocessing steps. Therefore, this repo focuses on providing instructions on how to preprocess the data in the specific format that will be accepted by the CANTRIP model. 


## Datasets


The datasets used by the experiments are from MIMIC-III, which can be acquired from [PhysioNet](https://physionet.org/). First download the whole dataset, then extract the files in the zipped folders. 


## Installation

The project is built using Python version 3.10.1. To install the Python programming interface, see [https://www.python.org/](https://www.python.org/). 

First clone this repo and nagivated inside the directory
```
git clone https://github.com/eunicornbread/CS598DLFinalProject.git
cd CS598DLFinalProject
```

Then install all necessary packages required for the project
```
pip install -r requirements.txt
```

In addition, you need to download `MetaMap Lite` for this project. For more isntructions, see [https://lhncbc.nlm.nih.gov/ii/tools/MetaMap/run-locally/MetaMapLite.html](https://lhncbc.nlm.nih.gov/ii/tools/MetaMap/run-locally/MetaMapLite.html). It is recommended to use MetaMapLite 3.6.2rc6 and 2020AA dataset, since other versions of `MetaMap` or `MetaMap Lite` may not work with `pymetamap`.




## Data Preprocessing

The files required by CANTRIP are `chronologies.csv`, `admittimes.csv`, and `labels.csv` for each of the `training`, `testing`, and `development` set. 

### Extracting chronologies from clinical notes

To extract chronologies from `NOTEEVENTS.csv`, run the following command
```
python extract_cui.py --metamap_lite_dir [metamap_lite_dir]
```

#### Required flags

```
--metamap_lite_dir: Directory path to metamap lite
```

#### Optional flags

```
--noteevents_file: File path to MIMIC-III dataset NOTEEVENTS.csv
  (default: './NOTEEVENTS.csv')
--output_dir: Path to directory to save all the output files
  (default: './output/')
--max_rows: Maximum number of rows to extract
  (default: 1000)
  (a positive integer)
```

#### Preparing processed data files

To prepare `chronologies`, `admittimes`, and `labels`, run the following command
```
python preprocessing.py
```

#### Optional flags

```
--data_dir: Path to directory that contains all the input data files
  (default: './data/')
--output_dir: Path to directory to save all the output files
  (default: './output/')
--chronology_dir: Path to directory that contains all the chronology files
  (default: './')
```

The repo also includes a IPython notebook if one wants to explore the data preprocessing steps in an interactive way. See `preprocessing.ipynb`. 

## References


Goodwin, Travis & Demner-Fushman, Dina. (2020). A customizable deep learning model for nosocomial risk prediction from critical care notes with indirect supervision. Journal of the American Medical Informatics Association : JAMIA. 27. 10.1093/jamia/ocaa004. 

Johnson, A., Pollard, T., Shen, L. et al. MIMIC-III, a freely accessible critical care database. Sci Data 3, 160035 (2016). https://doi.org/10.1038/sdata.2016.35

<!-- docker build -t spark_docker . 
navigate to folder mimic-on-spark
(in cmd, in other terminals, need to replace %cd% with the absolute path) docker run -it -v %cd%:/my_repo spark_docker bin/bash


in the docker container
cd my_repo/
install gradle in container
follow this link: https://linuxize.com/post/how-to-install-gradle-on-ubuntu-18-04/

wget https://services.gradle.org/distributions/gradle-5.0-bin.zip -P /tmp
sudo unzip -d /opt/gradle /tmp/gradle-*.zip
ls /opt/gradle/gradle-5.0

vim /etc/profile.d/gradle.sh

paste the following code:
export GRADLE_HOME=/opt/gradle/gradle-5.0
export PATH=${GRADLE_HOME}/bin:${PATH}

sudo chmod +x /etc/profile.d/gradle.sh
source /etc/profile.d/gradle.sh

<!-- verify Gradle is installed properly -->
<!-- gradle -v -->
<!-- output -->
<!-- Welcome to Gradle 5.0!

Here are the highlights of this release:
 - Kotlin DSL 1.0
 - Task timeouts
 - Dependency alignment aka BOM support
 - Interactive `gradle init`

For more details see https://docs.gradle.org/5.0/release-notes.html


------------------------------------------------------------
Gradle 5.0
------------------------------------------------------------

Build time:   2018-11-26 11:48:43 UTC
Revision:     7fc6e5abf2fc5fe0824aec8a0f5462664dbcd987

Kotlin DSL:   1.0.4
Kotlin:       1.3.10
Groovy:       2.5.4
Ant:          Apache Ant(TM) version 1.9.13 compiled on July 10 2018
JVM:          1.8.0_312 (Private Build 25.312-b07)
OS:           Linux 5.4.72-microsoft-standard-WSL2 amd64
 -->


<!-- add the gradle wrapper -->
<!-- gradle wrapper -->
<!-- output -->
<!-- Starting a Gradle Daemon (subsequent builds will be faster)

BUILD SUCCESSFUL in 4s
1 actionable task: 1 executed -->

<!-- now we can compile following the repo instruction -->
<!-- ./gradlew jar

put csv files in a data folder

replace build.gradle file and gradle-wreapper.properties file since the original ones are outdated and will prevent compiling --> 