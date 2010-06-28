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

#readme = "".join((l for l in open("README", "r")))

setup(  
    name         = 'logtools',
    version      = '0.4',
    description  = 'Log analysis and filtering tools',
    author       = 'Adam Ever-Hadani',
    author_email = 'adamhadani@gmail.com',
    url          = 'http://github.com/adamhadani/logtools',
    keywords     = ['logging', 'sampling', 'geoip', 'filterbots', 
                    'logparse', 'logmerge', 'logplot', 'filter'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",        
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Topic :: Internet :: Log Analysis",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Filters",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators"        
        ],
    long_description = """\
A log files analysis / filtering framework.

logtools encompasses of a few easy-to-use, easy to configure command-line
tools, typically used in conjunction with Apache logs.

The idea is to standardize log parsing and filtering using a coherent
configuration methodology and UNIX command-line interface (STDIN input streaming, command-line piping etc.)
so as to create a consistent environment for creating reports, charts and other such
log mining artifacts that are typically employed in a Website context.

This software is distributed under the Apache 2.0 license.
""",
    
    packages = find_packages(),

    scripts = ['scripts/aggregate'],

    include_package_data = False,    
    
    install_requires = [
        "pygooglechart>=0.2.1"
    ],

    entry_points = {
        'console_scripts': [
            'filterbots = logtools:filterbots_main',
            'geoip = logtools:geoip_main',
            'logparse = logtools:logparse_main',
            'logmerge = logtools:logmerge_main',
            'logplot = logtools:logplot_main',
            'logsample = logtools:logsample_main',            
        ]
    },

    test_requires = [
        "Nose>=0.11.3"
    ],
    test_suite = "nose.collector",

    zip_safe = True
)

