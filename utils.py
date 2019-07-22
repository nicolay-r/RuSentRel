from os import path


def get_rusentrel_format_sentiment_opin_filepath(index, root, is_etalon, prefix=u'art'):
    assert(isinstance(is_etalon, bool))
    return path.join(root, u"{}{}.opin{}.txt".format(prefix, index, '' if is_etalon else u'.result'))


def get_rusentrel_entity_filepath(index, root):
    assert(isinstance(index, int))
    assert(isinstance(root, unicode))
    return path.join(root, u"art{}.ann".format(index))


def get_rusentrel_news_filepath(index, root):
    assert(isinstance(index, int))
    assert(isinstance(root, unicode))
    return path.join(root, u"art{}.txt".format(index))


def get_rusentrel_test_indices():
    indices = range(46, 76)
    for i in [70]:
        if i in indices:
            indices.remove(i)
    return indices


def get_rusentrel_train_indices():
    indices = range(1, 46)
    for i in [9, 22, 26]:
        if i in indices:
            indices.remove(i)
    return indices


def get_rusentrel_collection_indices():
    return get_rusentrel_train_indices() + get_rusentrel_test_indices()


def get_rusentrel_synonyms_filepath():
    return path.join(u"synonyms.txt")