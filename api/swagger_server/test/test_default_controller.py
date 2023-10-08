# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.convertspacevideotosound_body import ConvertspacevideotosoundBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_convert_space_video_to_sound_post(self):
        """Test case for convert_space_video_to_sound_post

        Represent a video of space with sound
        """
        body = ConvertspacevideotosoundBody()
        response = self.client.open(
            '/wl504797/NASA-Space-Apps-2023-Sonograph/1.0.0/convert-space-video-to-sound',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
