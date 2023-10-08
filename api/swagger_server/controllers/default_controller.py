import connexion
import six

from swagger_server.models.convertspacevideotosound_body import ConvertspacevideotosoundBody  # noqa: E501
from swagger_server import util


def convert_space_video_to_sound_post(body):  # noqa: E501
    """Represent a video of space with sound

    Takes a video URL and returns an audio file or audio URL. # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """
    if connexion.request.is_json:
        body = ConvertspacevideotosoundBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
