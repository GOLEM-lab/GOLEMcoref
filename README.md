# anonymousCoref: a Multilingual Coreference Dataset of Fiction
This repository hosts the data, models, and evaluation results of the paper *anonymousCoref: a Multilingual Coreference Dataset of Fiction*.

- Our main contribution is **anonymousCoref**, a gold standard benchmark for coreference resolution in **7 langugages**: **Chinese**, **Dutch**, **English**, **Indonesian**, **Italian**, **Korean**, **Spanish** (--> [data/gold_annotations](https://github.com/GOLEM-lab/golemcoref/tree/main/data/gold_annotations)).
    - Unlike most popular established coreference resolution benchmarks, anonymousCoref focuses on **fiction genre**. It contains fictional **short stories** sourced from 3 popular **fanfiction** platforms: Archive of Our Own (AO3), Postype, and Wattpad.
    - anonymousCoref is the first of its kind offering **multilingual coverage** for the **fiction** genre and including **complete works**.
    - anonymousCoref is fully annotated and curated by humans following specialised guidelines (--> [guidelines](https://github.com/GOLEM-lab/golemcoref/tree/main/guidelines).

- We release **neural coreference systems** trained on our dataset: we train separate models for each language and one trained on data across all languages (-->[models](https://github.com/GOLEM-lab/golemcoref/tree/main/models)).
- Consistent with previous work, we observe strong improvements of the model trained multilingually over the monolingually trained models (-->[results](https://github.com/GOLEM-lab/golemcoref/tree/main/models)).

## Repository Structure

```
golemcoef/
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│   ├── gold_annotations/
│   │   ├── chinese/
│   │   │   ├── conll/
│   │   │   └── tsv/
│   │   ├── dutch/
│   │   │   ├── conll/
│   │   │   └── tsv/
│   │   ├── english/
│   │   │   ├── conll/
│   │   │   └── tsv/
│   │   ├── indonesian/
│   │   │   ├── conll/
│   │   │   └── tsv/
│   │   ├── italian/
│   │   │   ├── conll/
│   │   │   └── tsv/
│   │   ├── korean/
│   │   │   ├── conll/
│   │   │   └── tsv/
│   │   └── spanish/
│   │       ├── conll/
│   │       └── tsv/
│   └── splits/
│       └── splits.csv
│
├── guidelines/
|
|
├── models/
│   ├── README.md
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
│   ├── preprocessing/
│       └── makesplit.py
│   ├── evaluation/
|
└── results/
    ├── evaluation_metrics.csv
    └── predictions/
            ├── chinese/
            ├── dutch/
            ├── english/
            ├── indonesian/
            ├── italian/
            ├── korean/
            └── spanish/
```
