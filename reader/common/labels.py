

class Label:

    @staticmethod
    def from_str(value):
        for l in Label._get_supported_labels():
            if l.to_str() == value:
                return l
        raise Exception("Label by value '{}' doesn't supported".format(value))

    @staticmethod
    def from_int(value):
        assert(isinstance(value, int))
        for l in Label._get_supported_labels():
            if l.to_int() == value:
                return l
        raise Exception("Label by value '{}' doesn't supported".format(value))

    @staticmethod
    def from_uint(value):
        assert(isinstance(value, int) and value >= 0)
        for l in Label._get_supported_labels():
            if l.to_uint() == value:
                return l
        raise Exception("Label by unsigned value '{}' doesn't supported".format(value))

    @staticmethod
    def _get_supported_labels():
        supported_labels = [
            PositiveLabel(),
            NegativeLabel()
        ]
        return supported_labels

    def to_str(self):
        raise NotImplementedError()

    def to_int(self):
        raise NotImplementedError()

    def to_uint(self):
        raise Exception("Not implemented exception")

    def __eq__(self, other):
        assert(isinstance(other, Label))
        return self.to_int() == other.to_int()

    def __ne__(self, other):
        assert(isinstance(other, Label))
        return self.to_int() != other.to_int()


class PositiveLabel(Label):

    def to_str(self):
        return 'pos'

    def to_int(self):
        return int(1)

    def to_uint(self):
        return int(1)


class NegativeLabel(Label):

    def to_str(self):
        return 'neg'

    def to_int(self):
        return int(-1)

    def to_uint(self):
        return int(2)

