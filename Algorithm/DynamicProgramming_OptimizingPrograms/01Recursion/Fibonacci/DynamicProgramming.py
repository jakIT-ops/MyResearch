#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 02:06:26 2022

@author: jakitcs
"""

calculated = {}

def fib(n):
  if n == 0:
    return 0
  if n == 1: 
    return 1
  elif n in calculated:
    return calculated[n]
  else: # recursive step
    calculated[n] = fib(n-1) + fib(n-2)
    return calculated[n]

numbers = 20
print(fib(numbers))