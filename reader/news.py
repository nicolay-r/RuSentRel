# -*- coding: utf-8 -*-
import io
from .helpers.news import RuSentRelNewsHelper
from .entities.collection import RuSentRelDocumentEntityCollection
from reader.entities.entity import RuSentRelEntity
from reader.sentence import RuSentRelSentence


class RuSentRelNews(object):

    def __init__(self, sentences, entities):
        assert(isinstance(sentences, list))
        assert(isinstance(entities, RuSentRelDocumentEntityCollection))
        self.__sentences = sentences
        self.__entities = entities
        self.__helper = RuSentRelNewsHelper(self)

    @property
    def DocEntities(self):
        return self.__entities

    @property
    def Helper(self):
        return self.__helper

    @classmethod
    def from_file(cls, filepath, entities):
        assert(isinstance(filepath, str))
        assert(isinstance(entities, RuSentRelDocumentEntityCollection))

        sentences = RuSentRelNews.read_sentences(filepath)

        s_ind = 0
        e_ind = 0

        while s_ind < len(sentences) and e_ind < len(entities):
            e = entities.get_entity_by_index(e_ind)
            assert(isinstance(e, RuSentRelEntity))

            s = sentences[s_ind]

            if s.is_entity_goes_after(e):
                s_ind += 1
                continue

            if e in s:
                s.add_local_entity(entity=e)
                e_ind += 1
                continue

            if e.Value in ['author', 'unknown']:
                e_ind += 1
                continue

            raise Exception("e_i:{} e:('{}',{},{}), s_i:{}".format(
                e_ind,
                e.Value.encode('utf-8'), e.CharIndexBegin, e.CharIndexEnd,
                s_ind))

        assert(e_ind == len(entities))

        return cls(sentences, entities)

    @staticmethod
    def read_sentences(filepath):
        assert(isinstance(filepath, str))

        with io.open(filepath, 'rt', newline='\n', encoding='utf-8') as f:

            sentences = []
            line_start = 0
            unknown_entity = "Unknown}"

            for line in f.readlines():

                if unknown_entity in line:
                    offset = line.index(unknown_entity) + len(unknown_entity)
                    line_start += offset
                    line = line[offset:]

                line_end = line_start + len(line) - 1

                if line != str('\r\n'):
                    s = RuSentRelSentence(text=line,
                                          char_ind_begin=line_start,
                                          char_ind_end=line_end)
                    sentences.append(s)

                line_start = line_end + 1

        return sentences

    def sentences_count(self):
        return len(self.__sentences)

    def get_sentence_by_index(self, index):
        return self.__sentences[index]

    def iter_sentences(self):
        for sentence in self.__sentences:
            yield sentence
