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


class V1alpha1AuditSinkSpec(object):
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
        'policy': 'V1alpha1Policy',
        'webhook': 'V1alpha1Webhook'
    }

    attribute_map = {
        'policy': 'policy',
        'webhook': 'webhook'
    }

    def __init__(self, policy=None, webhook=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1AuditSinkSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._policy = None
        self._webhook = None
        self.discriminator = None

        self.policy = policy
        self.webhook = webhook

    @property
    def policy(self):
        """Gets the policy of this V1alpha1AuditSinkSpec.  # noqa: E501


        :return: The policy of this V1alpha1AuditSinkSpec.  # noqa: E501
        :rtype: V1alpha1Policy
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this V1alpha1AuditSinkSpec.


        :param policy: The policy of this V1alpha1AuditSinkSpec.  # noqa: E501
        :type: V1alpha1Policy
        """
        if self.local_vars_configuration.client_side_validation and policy is None:  # noqa: E501
            raise ValueError("Invalid value for `policy`, must not be `None`")  # noqa: E501

        self._policy = policy

    @property
    def webhook(self):
        """Gets the webhook of this V1alpha1AuditSinkSpec.  # noqa: E501


        :return: The webhook of this V1alpha1AuditSinkSpec.  # noqa: E501
        :rtype: V1alpha1Webhook
        """
        return self._webhook

    @webhook.setter
    def webhook(self, webhook):
        """Sets the webhook of this V1alpha1AuditSinkSpec.


        :param webhook: The webhook of this V1alpha1AuditSinkSpec.  # noqa: E501
        :type: V1alpha1Webhook
        """
        if self.local_vars_configuration.client_side_validation and webhook is None:  # noqa: E501
            raise ValueError("Invalid value for `webhook`, must not be `None`")  # noqa: E501

        self._webhook = webhook

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
        if not isinstance(other, V1alpha1AuditSinkSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1AuditSinkSpec):
            return True

        return self.to_dict() != other.to_dict()
