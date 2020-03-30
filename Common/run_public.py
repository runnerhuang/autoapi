# -*- coding: utf-8 -*-

import importlib


def exe_module(module, method, args=''):
    cls = module.split(".")[-1]
    if len(module.split(".")) > 2:
        module = module[0:-(len(module.split(".")[-1]) + 1)]
        m = importlib.import_module(module, )
        mod = getattr(m, cls)
        obj = mod()
        function = getattr(obj, method)
    else:
        module = module
        m = importlib.import_module(module, )
        function = getattr(m, method)

    if type(args) == tuple or type(args) == list:
        va = function(*args)
    elif args == '':
        va = function()
    else:
        va = function(args)
    return va


class Context(object):
    """
    Define the Context to store the return value.
    """

    def __init__(self):
        self.key_value = {}
