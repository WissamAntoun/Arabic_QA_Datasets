# Arabic Question Answering Datasets

This repository conatains copies of the major repositories that contain Arabic QA dataset that follows the SQuAD format.

```
file.json
├── "data"
│   └── [i]
│       ├── "paragraphs"
│       │   └── [j]
│       │       ├── "context": "paragraph text"
│       │       └── "qas"
│       │           └── [k]
│       │               ├── "answers"
│       │               │   └── [l]
│       │               │       ├── "answer_start": N
│       │               │       └── "text": "answer"
│       │               ├── "id": "<uuid>"
│       │               └── "question": "paragraph question?"
│       └── "title": "document id"
└── "version": XXX
```

If you use any dataset please cite their original source.  (I don't own any of the data available here)

#ARCD and Arabic-SQuAD

**Files:**
`Arabic-SQuAD.json` , `arcd-test.json`, `arcd-train.json`

**Statistics**:
ARCD: 1,395 questions based on 465 paragraphs from 155 articles. split 50/50 for train/test
Arabic-SQuAD: 48,344 questions on 10,364 paragraphs. Note that Arabic-SQuAD is translated from English SQuAD

**Owner:** [Hussein Mozannar](https://github.com/husseinmozannar/SOQAL)

**Cites as:**
```
@inproceedings{mozannar-etal-2019-neural,
    title = "Neural {A}rabic Question Answering",
    author = "Mozannar, Hussein  and
      Maamary, Elie  and
      El Hajal, Karl  and
      Hajj, Hazem",
    booktitle = "Proceedings of the Fourth Arabic Natural Language Processing Workshop",
    month = aug,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-4612",
    doi = "10.18653/v1/W19-4612",
    pages = "108--118",
    abstract = "This paper tackles the problem of open domain factual Arabic question answering (QA) using Wikipedia as our knowledge source. This constrains the answer of any question to be a span of text in Wikipedia. Open domain QA for Arabic entails three challenges: annotated QA datasets in Arabic, large scale efficient information retrieval and machine reading comprehension. To deal with the lack of Arabic QA datasets we present the Arabic Reading Comprehension Dataset (ARCD) composed of 1,395 questions posed by crowdworkers on Wikipedia articles, and a machine translation of the Stanford Question Answering Dataset (Arabic-SQuAD). Our system for open domain question answering in Arabic (SOQAL) is based on two components: (1) a document retriever using a hierarchical TF-IDF approach and (2) a neural reading comprehension model using the pre-trained bi-directional transformer BERT. Our experiments on ARCD indicate the effectiveness of our approach with our BERT-based reader achieving a 61.3 F1 score, and our open domain system SOQAL achieving a 27.6 F1 score.",
}
```

#TyDiQA (TyDiQA-GoldP)

TyDi QA is a question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs.

We filter the trainning set to get Arabic only QA pairs using `extract_arabic_qa_from_tydiqa.py`

**Files:**
`extract_arabic_qa_from_tydiqa.py`, `tydiqa-goldp-dev-arabic.json`

**Statistics**:
Train: 14508 QA pairs
Dev: 921 QA pairs

**Cite as**:
```
@article{tydiqa,
title   = {TyDi QA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages},
author  = {Jonathan H. Clark and Eunsol Choi and Michael Collins and Dan Garrette and Tom Kwiatkowski and Vitaly Nikolaev and Jennimaria Palomaki}
year    = {2020},
journal = {Transactions of the Association for Computational Linguistics}
}
```

#MLQA 

[MLQA](https://github.com/facebookresearch/MLQA) (MultiLingual Question Answering) is a benchmark dataset for evaluating cross-lingual question answering performance.

Statement from MLQA's GitHUB:

*MLQA is intended to be an evaluation corpus. Please limit evaluations on the test set to an absolute minimum to prevent overfitting. There is a development dataset split which can be used for running intermediate evaluations during model development.*
*If you are running experiments on MLQA, it is important that you clearly state your experimental settings. If you are performing zero-shot experiments, you should only use the development data in the language you are training on. Using MLQA dev data for particular target language to tune performance in that target language is a valid research direction, but is not strictly zero-shot and you should make sure that you explicitly state how you use the development data to ensure fair comparison in the future.*

**Files**:
`MLQA-test-context-ar-question-ar.json`, `MLQA-dev-context-ar-question-ar.json`

**Statistics**:
Dev: 517 paragraph and question pairs
Test: 5225 paragraph and question pairs

**Cite as**:
```
@article{lewis2019mlqa,
  title={MLQA: Evaluating Cross-lingual Extractive Question Answering},
  author={Lewis, Patrick and O\u{g}uz, Barlas and Rinott, Ruty and Riedel, Sebastian and Schwenk, Holger},
  journal={arXiv preprint arXiv:1910.07475},
  year={2019}
}
```


