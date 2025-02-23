#!/usr/bin/env python
from setuptools import setup
import versioneer


with open("README.md", "r") as fh:
    long_description = fh.read()

configuration = {
    'name': 'sotb-wrapper',
    'packages': ["sotb-wrapper"],
    'package_dir': {'sotb-wrapper': 'sotb_wrapper'},
    'package_data': {'sotb-wrapper': ['lib/libOPTIM.so']},
    'version': versioneer.get_version(),
    'cmdclass': versioneer.get_cmdclass(),
    'description': "wrapper to call fortran routines from SEISCOPE optimization toolbox",
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'url': 'https://github.com/ofmla/seiscope_opt_toolbox_w_ctypes',
    'author': "Oscar Mojica",
    'author_email': 'o_mojical@hotmail.com',
    'license': 'MIT',
    'zip_safe': False
}

setup(**configuration)
