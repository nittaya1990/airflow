# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE OVERWRITTEN!
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-apache-pig",
        "name": "Apache Pig",
        "description": "`Apache Pig <https://pig.apache.org/>`__\n",
        "state": "ready",
        "source-date-epoch": 1734528476,
        "versions": [
            "4.6.0",
            "4.5.0",
            "4.4.1",
            "4.4.0",
            "4.3.0",
            "4.2.0",
            "4.1.2",
            "4.1.1",
            "4.1.0",
            "4.0.0",
            "3.0.0",
            "2.0.4",
            "2.0.3",
            "2.0.2",
            "2.0.1",
            "2.0.0",
            "1.0.1",
            "1.0.0",
        ],
        "integrations": [
            {
                "integration-name": "Apache Pig",
                "external-doc-url": "https://pig.apache.org/",
                "how-to-guide": ["/docs/apache-airflow-providers-apache-pig/operators.rst"],
                "logo": "/docs/integration-logos/pig.png",
                "tags": ["apache"],
            }
        ],
        "operators": [
            {
                "integration-name": "Apache Pig",
                "python-modules": ["airflow.providers.apache.pig.operators.pig"],
            }
        ],
        "hooks": [
            {"integration-name": "Apache Pig", "python-modules": ["airflow.providers.apache.pig.hooks.pig"]}
        ],
        "connection-types": [
            {
                "connection-type": "pig_cli",
                "hook-class-name": "airflow.providers.apache.pig.hooks.pig.PigCliHook",
            }
        ],
        "dependencies": ["apache-airflow>=2.9.0"],
    }
