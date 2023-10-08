# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ConvertspacevideotosoundBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, video_url: str=None):  # noqa: E501
        """ConvertspacevideotosoundBody - a model defined in Swagger

        :param video_url: The video_url of this ConvertspacevideotosoundBody.  # noqa: E501
        :type video_url: str
        """
        self.swagger_types = {
            'video_url': str
        }

        self.attribute_map = {
            'video_url': 'video_url'
        }
        self._video_url = video_url

    @classmethod
    def from_dict(cls, dikt) -> 'ConvertspacevideotosoundBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The convertspacevideotosound_body of this ConvertspacevideotosoundBody.  # noqa: E501
        :rtype: ConvertspacevideotosoundBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def video_url(self) -> str:
        """Gets the video_url of this ConvertspacevideotosoundBody.

        URL of the video to be converted.  # noqa: E501

        :return: The video_url of this ConvertspacevideotosoundBody.
        :rtype: str
        """
        return self._video_url

    @video_url.setter
    def video_url(self, video_url: str):
        """Sets the video_url of this ConvertspacevideotosoundBody.

        URL of the video to be converted.  # noqa: E501

        :param video_url: The video_url of this ConvertspacevideotosoundBody.
        :type video_url: str
        """
        if video_url is None:
            raise ValueError("Invalid value for `video_url`, must not be `None`")  # noqa: E501

        self._video_url = video_url
