import unittest
import models.metrics
import config.metric_config as mconfig

class TestMetricConfig(unittest.TestCase):

    def test_load_config(self):
        mood = mconfig.load('sample_metrics.yml')['mood']
        self.assertEqual(models.metrics.NaturalMetric('mood', {
            'range': {
                'start': 0,
                'end': 9
            }
        }), mood)