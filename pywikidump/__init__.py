#!/usr/bin/env python
# coding: utf-8
from .WikiText import WikiText
from .pywikidump import getArticlesMultistreamIndexArray

def init(programDescription=[]):
    return WikiText(programDescription)
