"""
    Spectre Information Center API

    Spectre Information Center API to access MySQL and Influx Databases.   # noqa: E501

    The version of the OpenAPI document: 0.4.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import spectre_api_client
from spectre_api_client.model.data_point import DataPoint
globals()['DataPoint'] = DataPoint
from spectre_api_client.model.data_series import DataSeries


class TestDataSeries(unittest.TestCase):
    """DataSeries unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDataSeries(self):
        """Test DataSeries"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DataSeries()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
