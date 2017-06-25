class Metric(object):
    """
    Abstract metric class
    """

    def __init__(self, name):
        self.name = name

    def stringify(self, detail):
        return "%s(%s:%s)" % (self.__class__.__name__, self.name, detail)

    def __eq__(self, other):
        return (type(self) == type(other)) and (self.name == other.name)


class NaturalMetric(Metric):
    """
    Metric dealing with ranges of integers
    """

    def __init__(self, name, definition):
        super().__init__(name)
        self.start = definition['range']['start']
        self.end = definition['range']['end']

    def validate(self, val):
        return (val >= self.start and val <= self.end and int(val) == val)

    def __repr__(self):
        return self.stringify("range[%s,%s]" % (self.start, self.end))

    def __eq__(self, other):
        return super().__eq__(other) and (self.start == other.start) and (self.end == other.end)


class BooleanMetric(object):
    pass


METRIC_MAPPING = {
    'natural': NaturalMetric,
    'boolean': BooleanMetric
}


def create(name, defn):
    klazz = METRIC_MAPPING[defn['type']]
    return klazz(name, defn)