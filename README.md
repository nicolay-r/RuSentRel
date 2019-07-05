# RuSentRel 1.1

> Comparing with v1.0, in v1.1 list of synonyms has been expanded. It covers all 
extracted named entities in *.ann files.

RuSentRel corpus [[paper](https://arxiv.org/pdf/1808.08932.pdf)] of version 1.1 consisted of analytical articles from Internet-portal inosmi.ru. 
These are translated into Russian texts in the domain of international politics
obtained from foreign authoritative sources.
The collected articles contain both the author's opinion on the subject matter of the 
article and a large number of references mentioned between the participants of the 
described situations. In total, 73 large analytical texts were labeled with about 2000
relations.

The texts were processed by the automatic name entity (NE) recognizer, based on CRF method [[paper]](https://pdfs.semanticscholar.org/5eb6/6e658a9c306b846c84da8b5cbd0e150ab64a.pdf).
NE were categorized into four classes: Persons, Organizations, Places and Geopolitical Entities 
(states and capitals as states). 
Automatic labeling contains a few errors that have not yet been corrected. Preliminary analysis 
showed that the F-measure of determining the correct entity boundaries exceeds 95%.
Recognized NE were composed in `*.ann` files.

For verbose description, please see [References](#references) section.

For model application, please refer to the following repositores: 
* Scikit-learn classifiers [application](https://github.com/nicolay-r/sentiment-relation-classifiers)
* Piecewise CNN [application](https://github.com/nicolay-r/sentiment-pcnn)

# Parameters

| Parameter                                         |  Training collection |  Test collection |
|---------------------------------------------------|:--------------------:|:----------------:|
| Number of documents                               | 44                   | 29               |
| Sentences (avg./doc.)                             | 74.5                 | 137              |
| NE (avg./doc.)                                    | 194                  | 300              |
| unique NE (avg./doc.)                             | 33.3                 | 59.9             |
| positive pairs of NE (avg./doc.)                  | 6.23                 | 14.7             |
| negative pairs of NE (avg./doc.)                  | 9.33                 | 15.6             |
| Share of attitudes expressed in a single sentence | 76.5\%               | 73\%             |

Statistics for the whole Collection:

| Parameter                                        | Collection |
|--------------------------------------------------|:----------:|
| Avg. dist. between NE within a sentence in words | 10.2       |
| Human labeling agreement (F1(P, N))              | 0.55       |
| Contradiction (Acc.)                             | 0.01       |

Separately for train and test collections, we compose and group these sets by sizes and the resulted statistics for the
first eight groups is presented in table below.

We decide a context **sentiment** with a pair of entities, when related sentiment attitude could be found.


|train-sent | Total | 1     | 2      | 3     | 4       | 5       | 6      | 7      | 8    |
|-----------|:------|:------|:-------|:------|:--------|:--------|:-------|:-------|------|
|train-sent | 467   | 47\%  | 15\%   | 4.4\% | 4.3\%   | 2.2\%   | 0.9\%  | 0.8\%  | 1.0\%|
|test-sent  | 669   | 47\%  | 13\%   | 5.0\% | 4.2\%   | 2.4\%   | 1.0\%  | 1.1\%  | 1.3\%|

In most cases we deal with single-context attitudes in train and test collections. However, the distribution of the
sentiment single-context attitudes represent 47%
is about a half of all occured attitudes.
Considering such a distinctive factor for attitudes labeling, it is important to take into account the labels of several contexts

# References
<a name="references"></a>
```
@article{loukachevitch2018extracting,
    Author = {Loukachevitch, N. and Rusnachenko, N.},
    Title = {Extracting Sentiment Attitudes from Analytical Texts},
    Journal = {In Proceedings of International conference Dialog-2018},
    Year = {2018}
}
```
