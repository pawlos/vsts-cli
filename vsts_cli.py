#!/usr/bin/python
# -*- coding: utf-8 -*- 
from vsts_query import *
import sys

if __name__=='__main__':
	vsts = VSTSQuery('DEBUG' in sys.argv)
	vsts.cmdloop()

