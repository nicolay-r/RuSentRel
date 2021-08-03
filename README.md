# RuSentRel 1.0-rc

RuSentRel corpus of version 1.0 consisted of analytical articles from Internet-portal inosmi.ru. 
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
