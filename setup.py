#!/usr/bin/env python
#
#  Licensed under the Apache License, Version 2.0 (the "License"); 
#  you may not use this file except in compliance with the License. 
#  You may obtain a copy of the License at 
#  
#      http://www.apache.org/licenses/LICENSE-2.0 
#     
#  Unless required by applicable law or agreed to in writing, software 
#  distributed under the License is distributed on an "AS IS" BASIS, 
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
#  See the License for the specific language governing permissions and 
#  limitations under the License. 

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys
import os

setup(  
    name         = 'logtools',
    version      = '0.1',
    description  = 'Log analysis and filtering tools',
    author       = 'Adam Ever-Hadani',
    author_email = 'adamhadani@gmail.com',

    packages = find_packages(),

    entry_points = {
        'console_scripts': [
            'filterbots = logtools:filterbots_main',
            'geoip = logtools:geoip_main',
        ]
    },

    zip_safe = True
)

