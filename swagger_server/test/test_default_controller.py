# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.video_sonograph_body import VideoSonographBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_video_sonograph_post(self):
        """Test case for video_sonograph_post

        Represent a video of space with sound
        """
        body = VideoSonographBody()
        response = self.client.open(
            '/wl504797/NASA-Space-Apps-2023-Sonograph/1.0.0/videoSonograph',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
