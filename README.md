# GOLEMcoref: a Multilingual Coreference Dataset of Fiction
This repository hosts the data, models, and evaluation results of the paper *GOLEMcoref: a Multilingual Coreference Dataset of Fiction*.

- What is **GOLEMcoref**?
    - It is a gold standard benchmark for coreference resolution in **7 langugages**: **Bahasa Indonesia**, **Chinese**, **Dutch**, **English**, **Italian**, **Korean**, **Spanish** (--> [data/gold_annotations](https://github.com/GOLEM-lab/golemcoref/tree/main/data/gold_annotations)).
    - It contains fictional **short stories** sourced from 3 popular **fanfiction** platforms: [Archive of Our Own (AO3)](https://archiveofourown.org/), [Postype](https://www.postype.com/), and [Wattpad](https://www.wattpad.com/).
    - It is the first of its kind offering **multilingual coverage** for **fictional literature**.
    - It includes **complete works**.
    - It is a **gold standard**: it is fully **annotated** and curated by **humans** following specialised guidelines (--> [guidelines](https://github.com/GOLEM-lab/golemcoref/tree/main/guidelines)) and accompanied by a report discussing annotation challenges (--> [report](https://github.com/GOLEM-lab/golemcoref/tree/main/report)).

- We trained **neural coreference systems** on our dataset:
    - We train separate models for each language and crosslingual models trained on data across all languages.
    - Consistent with previous work, we observe improvements of the model trained multilingually over the monolingually trained models (-->[results](https://github.com/GOLEM-lab/golemcoref/tree/main/results)).

## Repository Structure

The schema below provides a map of this repository:

```
├── README.md
│
├── data/
│   ├── gold_annotations/
│   │   ├── chinese/
│   │   │   ├── conll/
│   │   │   └── conllu/
│   │   ├── dutch/
│   │   │   ├── conll/
│   │   │   └── conllu/
│   │   ├── english/
│   │   │   ├── conll/
│   │   │   └── conllu/
│   │   ├── indonesian/
│   │   │   ├── conll/
│   │   │   └── conllu/
│   │   ├── italian/
│   │   │   ├── conll/
│   │   │   └── conllu/
│   │   ├── korean/
│   │   │   ├── conll/
│   │   │   └── conllu/
│   │   └── spanish/
│   │       ├── conll/
│   │       └── conllu/
│   └── splits/
│       └── splits.csv
│
├── guidelines/
│       └── GOLEMcoref_Character Coreference Annotation Guidelines.pdf
│
├── report/
│       └── Coref_Annotation_Challenges.pdf
│
├── scripts/
│       └── makesplit.py
│
└── results/
    ├── evalreport.txt
    └── monolingual_models/
            ├── chinese/
            ├── dutch/
            ├── dutch_openboek/
            ├── english/
            ├── english_litbankp/
            ├── indonesian/
            ├── italian/
            ├── korean/
            └── spanish/
    └── single_crosslingual_model/
            ├── chinese/
            ├── dutch/
            ├── dutch_openboek/
            ├── english/
            ├── english_litbankp/
            ├── indonesian/
            ├── italian/
            ├── korean/
            └── spanish/
```
# Data

- **GOLEMcoref** is available in this repository in the [data](https://github.com/GOLEM-lab/golemcoref/tree/main/data/gold_annotations) folder:
    - We release our **gold standard** benchmark in [data/gold_annotations](https://github.com/GOLEM-lab/golemcoref/tree/main/data/gold_annotations):
        - We store annotated data in each **language** in a **dedicated** folder (for example, [data/gold_annotations/chinese](https://github.com/GOLEM-lab/GOLEMcoref/tree/main/data/gold_annotations/chinese)) 
        -  For each language, we provide:
            - data in **CoNLL-2012** (stored in the **conll** subfolder - for example, [data/gold_annotations/chinese/conll](https://github.com/GOLEM-lab/GOLEMcoref/tree/main/data/gold_annotations/chinese/conll)):
                - They are divided in *train*, *dev* and *test* splits.
                - Zero anaphora are included as <EMPTY> tokens.
            - data in **CorefUD** (stored in the **conllu** subfolder - for example, [data/gold_annotations/chinese/conllu](https://github.com/GOLEM-lab/GOLEMcoref/tree/main/data/gold_annotations/chinese/conllu)):
                - They are divided in *train*, *dev* and *test* splits.
                - They come with zero anaphora and split antecedents (inclusion relation), as well as POS tags and dependencies from [Stanza](https://stanfordnlp.github.io/stanza/).
              
    - Stories included in each of the splits (*train*, *dev* and *test*) are listed in [data/splits/splits.csv](https://github.com/GOLEM-lab/GOLEMcoref/blob/main/data/splits/splits.csv)
    - the script used to create the *train*, *dev* and *test* splits is available at [scripts/makesplit.py](https://github.com/GOLEM-lab/GOLEMcoref/blob/main/scripts/makesplit.py)

# Guidelines

- The guidelines used in the annotation campaign that led to the creation of GOLEMcoref are available at [guidelines](https://github.com/GOLEM-lab/golemcoref/tree/main/guidelines/).

# Models

The best performing model, the crosslingual fast-coref model, is made available as [a release in this Github repository](https://github.com/GOLEM-lab/GOLEMcoref/releases/tag/v1.0).
To see how to apply the model on your own texts, refer to [the notebook on Google Colab](https://colab.research.google.com/drive/1X7CwX8qrhHeAZ-J0e9LSfDo_tuF7s858?usp=sharing); or [the copy of the notebook in this repository](https://github.com/GOLEM-lab/GOLEMcoref/blob/main/scripts/GOLEMcoref_using_the_crosslingual_fast_coref_model.ipynb).

# Report

- The [report](https://github.com/GOLEM-lab/golemcoref/tree/main/report) discusses the challenges encountered by the annotators and curators, both in relation to fiction and to language specificities.

# Scripts

- We release the scripts we used in our experiments:
    - the script used to create the *train*, *dev* and *test* splits is available at [scripts/makesplit.py](https://github.com/GOLEM-lab/GOLEMcoref/blob/main/scripts/makesplit.py)
- Some modifications were made to the coreference systems. These are availabel at https://github.com/andreasvc/fast-coref and https://github.com/andreasvc/xcore

# Results

We release the output of our models in [results](https://github.com/GOLEM-lab/GOLEMcoref/tree/main/results)

