# golemcoref
Dataset and code for the GolemCoref paper 

# Repository Structure

```
golemcoref/
├── README.md
├── LICENSE
├── requirements.txt
│
├── data/
│   ├── README.md
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
│   │   └── create_splits.py
│   ├── training/
│   │   └── train_model.py
│   ├── evaluation/
│   │   └── evaluate.py
│   └── utils/
│       └── helpers.py
│
└── results/
    ├── evaluation_metrics.csv
    └── predictions/
```
