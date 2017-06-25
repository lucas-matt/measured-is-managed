import yaml
import logging
import models.metrics


logger = logging.getLogger(__name__)


def __parse_config(defns):
    metrics = defns['metrics']
    names = metrics.keys()
    defns = [(name, metrics[name]) for name in names]
    return { name: models.metrics.create(name, defn) for (name, defn) in defns}


def load(file):
    with open(file, 'r') as stream:
        config = yaml.load(stream)
        return __parse_config(config)


