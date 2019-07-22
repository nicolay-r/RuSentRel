from reader.common.bound import Bound
from reader.common.entities.collection import EntityCollection
from reader.common.lemmatization.mystem import MystemWrapper
from reader.entities.collection import RuSentRelDocumentEntityCollection
from reader.entities.entity import RuSentRelEntity
from reader.news import RuSentRelNews
from reader.opinions.collection import RuSentRelOpinionCollection
from reader.opinions.opinion import RuSentRelOpinion
from reader.sentence import RuSentRelSentence
from reader.synonyms import RuSentRelSynonymsCollection
import utils


# Initializing stemmer
stemmer = MystemWrapper()

# Reading synonyms collection.
synonyms = RuSentRelSynonymsCollection.from_file('synonyms.txt', stemmer=stemmer)

# Reading 'train' subfolder of collection.
train_root = 'train'
for news_id in utils.get_rusentrel_train_indices():

    # Init filepaths
    entities_filepath = utils.get_rusentrel_entity_filepath(news_id, root=train_root)
    news_filepath = utils.get_rusentrel_news_filepath(news_id, root=train_root)
    opinion_filepath = utils.get_rusentrel_format_sentiment_opin_filepath(news_id, root=train_root, is_etalon=True)

    # Read collections
    entities = RuSentRelDocumentEntityCollection.from_file(entities_filepath, stemmer=stemmer, synonyms=synonyms)
    news = RuSentRelNews.from_file(news_filepath, entities)
    opininons = RuSentRelOpinionCollection.from_file(opinion_filepath, synonyms=synonyms)

    #############
    # Application
    #############

    # Example: Access to the read OPINIONS collection.
    for opinion in opininons.iter_sentiment():
        assert(isinstance(opinion, RuSentRelOpinion))
        print "{}->{} ({}) [synonym groups opinion: {}->{}]".format(
            opinion.SourceValue,
            opinion.TargetValue,
            opinion.Sentiment.to_str(),
            # Considering synonyms.
            synonyms.get_synonym_group_index(opinion.SourceValue),
            synonyms.get_synonym_group_index(opinion.TargetValue))

    # Example: Access to the read NEWS collection.
    for sentence in news.iter_sentences():
        assert(isinstance(sentence, RuSentRelSentence))
        # Access to text.
        print("Text:{}".format(sentence.Text))
        # Access to inner entities.
        for entity, bound in sentence.iter_entity_with_local_bounds():
            assert(isinstance(entity, RuSentRelEntity))
            assert(isinstance(bound, Bound))
            print("Entity: {}, text position: ({}-{}), docId:{}".format(
                entity.Value,
                bound.Position,
                bound.Position + bound.Length,
                entity.IdInDocument))

    # Example: Access to the read ENTITIES collection.
    example = entities.get_entity_by_index(5)
    entities_list = entities.try_get_entities(example.Value, group_key=EntityCollection.KeyType.BY_SYNONYMS)
    print("Synonymous to {}:".format(example))
    print("[{}]".format(", ".join([e.Value for e in entities_list])))
