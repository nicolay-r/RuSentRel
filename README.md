# RuSentRel

Corpus consisted of analytical articles from Internet-portal inosmi.ru. These
are translated into Russian texts in the domain of international politics
obtained from foreign authoritative sources. The collected articles contain
both the author's opinion on the subject matter of the article and a large
number of references mentioned between the participants of the described
situations. In total, 73 large analytical texts were labeled with about 2000
relations.

| Parameter                                         |  Training collection |  Test collection |
|---------------------------------------------------|:--------------------:|:----------------:|
| Number of documents                               | 44                   | 29               |
| Avg. number of sentences per doc.                 | 74.5                 | 137              |
| Avg. number of mentioned NE per doc.              | 194                  | 300              |
| Avg. number of unique NE per doc.                 | 33.3                 | 59.9             |
| Avg. number of positive pairs of NE per doc.      | 6.23                 | 14.7             |
| Avg. number of negative pairs of NE per doc.      | 9.33                 | 15.6             |
| Share of attitudes expressed in a single sentence | 76.5\%               | 73\%             |
| Avg. number of neutral pairs of NE per doc.       | 120                  | 276              |

Statistics for the whole Collection:

| Parameter                                        | Collection |
|--------------------------------------------------|:----------:|
| Avg. dist. between NE within a sentence in words | 10.2       |
| Human labeling agreement ($F_1(N, P)$)           | 0.55       |
| Contradiction (Accuracy measure)                 | 0.01       |
