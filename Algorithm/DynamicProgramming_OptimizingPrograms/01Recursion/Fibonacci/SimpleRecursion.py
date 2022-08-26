#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 00:51:06 2022

@author: jakitcs
"""

def fib(n):
  if n == 0: # base case 1
    return 0
  if n == 1: # base case 2
    return 1
  else: # recursive step
    return fib(n-1) + fib(n-2)

print (fib(20))