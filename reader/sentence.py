from reader.common.bound import Bound
from reader.entities.entity import RuSentRelEntity


class RuSentRelSentence(object):
    """ Represent a raw sentence of reader.
        Provides text could be used to parse then.
        Provides API to store entites.
    """

    def __init__(self, text, char_ind_begin, char_ind_end):
        assert(isinstance(text, str) and len(text) > 0)
        assert(isinstance(char_ind_begin, int))
        assert(isinstance(char_ind_end, int))
        self.__text = text
        self.__begin = char_ind_begin
        self.__end = char_ind_end
        self.__entities = []

    @property
    def Text(self):
        return self.__text

    def add_local_entity(self, entity):
        assert(isinstance(entity, RuSentRelEntity))
        self.__entities.append(entity)

    def iter_entity_ids(self):
        for entity in self.__entities:
            yield entity.IdInDocument

    def iter_entities(self):
        for entity in self.__entities:
            yield entity

    def iter_entity_with_local_bounds(self):
        for entity in self.__entities:
            start = entity.CharIndexBegin - self.__begin
            end = entity.CharIndexEnd - self.__begin
            yield entity, Bound(pos=start, length=end - start)

    def is_entity_goes_after(self, entity):
        assert(isinstance(entity, RuSentRelEntity))
        return entity.CharIndexBegin > self.__end

    def __contains__(self, entity):
        assert(isinstance(entity, RuSentRelEntity))
        return entity.CharIndexBegin >= self.__begin and entity.CharIndexEnd <= self.__end
