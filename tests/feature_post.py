import json

from tests.base import BaseTestCase


class FeaturePostTestCase(BaseTestCase):

    def test_feature_post_successful(self):
        """
        Ensure that a valid POST request to /feature_request
        will create a new Feature Request record.
        """
        post_data = {
            "title": "chat app",
            "description": "realtime chat app",
            "client": "client b",
            "priority": 2,
            "product_area": "Policies",
            "target_date": "2018-04-01",
        }

        headers = {'Content-Type': 'application/json'}
        resp = self.test_client.post('/feature_request', data=json.dumps(post_data), headers=headers)
        resp_dict = json.loads(resp.data.decode())
        assert(resp.status_code == 201)
        assert(post_data['title'], resp_dict['title'])
        assert(post_data['description'], resp_dict['description'])
        assert(post_data['client'], resp_dict['client'])
        assert(post_data['priority'], resp_dict['priority'])
        assert(post_data['product_area'], resp_dict['product_area'])
        assert(post_data['target_date'], resp_dict['target_date'])

    def test_feature_post_invalid(self):
        """
        Ensure that invalid POST requests to /feature_request
        will get a 400 error code response.
        """
        post_data = {
            "title": "",
            "description": "realtime chat app",
            "client": "client b",
            "priority": 2,
            "product_area": "Policies"
        }

        headers = {'Content-Type': 'application/json'}
        resp = self.test_client.post('/feature_request', data=json.dumps(post_data), headers=headers)
        resp_dict = json.loads(resp.data.decode())
        assert(resp.status_code == 400)
