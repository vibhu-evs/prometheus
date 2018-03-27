import json

from tests.base import BaseTestCase


class FeatureGetTestCase(BaseTestCase):


    def test_feaure_successful(self):
        """
        Ensure that GET request to /feature_request
        list will return an 200 response.
        """
        resp = self.test_client.get("/feature_request")
        assert(resp.status_code == 200)
