#!/usr/bin/env python

file_name = 'Max_Points_on_a_Line'
func_name = 'maxPoints'

import importlib
module = importlib.import_module('Leetcode.%s' % file_name)
instance = module.Solution()

print getattr(instance, func_name)()
