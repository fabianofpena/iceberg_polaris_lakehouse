
# coding: utf-8
#
# Copyright (c) 2024 Snowflake Computing Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
    Polaris Management Service

    Defines the management APIs for using Polaris to create and manage Iceberg catalogs and their principals

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from polaris.management.models.update_principal_role_request import UpdatePrincipalRoleRequest

class TestUpdatePrincipalRoleRequest(unittest.TestCase):
    """UpdatePrincipalRoleRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdatePrincipalRoleRequest:
        """Test UpdatePrincipalRoleRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdatePrincipalRoleRequest`
        """
        model = UpdatePrincipalRoleRequest()
        if include_optional:
            return UpdatePrincipalRoleRequest(
                current_entity_version = 56,
                properties = {
                    'key' : ''
                    }
            )
        else:
            return UpdatePrincipalRoleRequest(
        )
        """

    def testUpdatePrincipalRoleRequest(self):
        """Test UpdatePrincipalRoleRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
