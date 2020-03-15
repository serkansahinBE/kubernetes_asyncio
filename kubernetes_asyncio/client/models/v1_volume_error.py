# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.15.11
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1VolumeError(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'message': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'message': 'message',
        'time': 'time'
    }

    def __init__(self, message=None, time=None, local_vars_configuration=None):  # noqa: E501
        """V1VolumeError - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message = None
        self._time = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if time is not None:
            self.time = time

    @property
    def message(self):
        """Gets the message of this V1VolumeError.  # noqa: E501

        String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.  # noqa: E501

        :return: The message of this V1VolumeError.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this V1VolumeError.

        String detailing the error encountered during Attach or Detach operation. This string may be logged, so it should not contain sensitive information.  # noqa: E501

        :param message: The message of this V1VolumeError.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def time(self):
        """Gets the time of this V1VolumeError.  # noqa: E501

        Time the error was encountered.  # noqa: E501

        :return: The time of this V1VolumeError.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this V1VolumeError.

        Time the error was encountered.  # noqa: E501

        :param time: The time of this V1VolumeError.  # noqa: E501
        :type: datetime
        """

        self._time = time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1VolumeError):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1VolumeError):
            return True

        return self.to_dict() != other.to_dict()
