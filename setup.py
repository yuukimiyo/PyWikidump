# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='pywikidump',
    version='0.1.0',
    description='Functions for wikidump.',
    long_description='Functions for wikidump.',
    author='yuuki miyoshi',
    author_email='yuuki.miyo@gmail.com',
    url='https://github.com/yuukimiyo/PyWikidump',
    license="MIT",
    keywords="wiki wikidump infobox",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
