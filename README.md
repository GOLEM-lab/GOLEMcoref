# anonymousCoref: a Multilingual Coreference Dataset of Fiction
This repository hosts the data, models, and evaluation results of the paper *anonymousCoref: a Multilingual Coreference Dataset of Fiction*.

- What is **anonymousCoref**?
    - It is a gold standard benchmark for coreference resolution in **7 langugages**: **Chinese**, **Dutch**, **English**, **Indonesian**, **Italian**, **Korean**, **Spanish** (--> [data/gold_annotations](https://github.com/GOLEM-lab/golemcoref/tree/main/data/gold_annotations)).
    - It contains fictional **short stories** sourced from 3 popular **fanfiction** platforms: [Archive of Our Own (AO3)](https://archiveofourown.org/), [Postype](https://www.postype.com/), and [Wattpad](https://www.wattpad.com/).
    - It is the first of its kind offering **multilingual coverage** for **fictional literature**.
    - It includes **complete works**.
    - It is a **gold standard**: it is fully **annotated** and curated by **humans** following specialised guidelines (--> [guidelines](https://github.com/GOLEM-lab/golemcoref/tree/main/guidelines)).

- We release **neural coreference systems** trained on our dataset:
    - We train separate models for each language and one trained on data across all languages (-->[models](https://github.com/GOLEM-lab/golemcoref/tree/main/models)).
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
│       └── anon_Character Coreference Annotation Guidelines.pdf
|
├── models/
│   ├── chinese/
│   ├── dutch/
│   ├── english/
│   ├── indonesian/
│   ├── italian/
│   ├── korean/
│   ├── spanish/
│   └── multilingual/
│
├── scripts/
│       └── makesplit.py
|
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

- **anonymousCoref** is available in this repository in the [data](https://github.com/GOLEM-lab/golemcoref/tree/main/data/gold_annotations) folder:
    - We release our **gold standard** benchmark in [data/gold_annotations](https://github.com/GOLEM-lab/golemcoref/tree/main/data/gold_annotations):
        - We store annotated data in each **language** in a **dedicated** folder (for example, [data/gold_annotations/chinese](https://github.com/GOLEM-lab/anonymouscoref/tree/main/data/gold_annotations/chinese)) 
        -  For each language, we provide:
            - data in **CoNLL-2012** (stored in the **conll** subfolder - for example, [data/gold_annotations/chinese/conll](https://github.com/GOLEM-lab/anonymouscoref/tree/main/data/gold_annotations/chinese/conll)):
                - They are divided in *train*, *dev* and *test* splits.
                - Zero anaphora are included as <EMPTY> tokens.
            - data in **CorefUD** (stored in the **conllu** subfolder - for example, [data/gold_annotations/chinese/conllu](https://github.com/GOLEM-lab/anonymouscoref/tree/main/data/gold_annotations/chinese/conllu)):
                - They are divided in *train*, *dev* and *test* splits.
                - They come with zero anaphora and split antecedents (inclusion relation), as well as POS tags and dependencies from [Stanza](https://stanfordnlp.github.io/stanza/).
              
    - Stories included in each of the splits (*train*, *dev* and *test*) are listed in [data/splits/splits.csv](https://github.com/GOLEM-lab/anonymouscoref/blob/main/data/splits/splits.csv)
    - the script used to create the *train*, *dev* and *test* splits is available at [scripts/makesplit.py](https://github.com/GOLEM-lab/anonymouscoref/blob/main/scripts/makesplit.py)

# Guidelines

- The guidelines used in the annotation campaign that led to the creation of anonymousCoref are available at [guidelines](https://github.com/GOLEM-lab/golemcoref/tree/main/guidelines/).

# Models

- Due to the size of the monolingual and multilingual models that we trained, and anonymity issues, we will release the trained models with the final and non-anonymous version of the paper.

# Scripts

- We release the scripts we used in our experiments:
    - the script used to create the *train*, *dev* and *test* splits is available at [scripts/makesplit.py](https://github.com/GOLEM-lab/anonymouscoref/blob/main/scripts/makesplit.py)


# Results

We release the output of our models in [results](https://github.com/arianna-graciotti/anonymouscoref/tree/main/results)

