# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 08:59:02 2023

@author: maggi
"""

from collections.abc import Iterable


def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    list2=[]
    i=0
    while i in range(len(donuts)):
        list2.append(donuts[i])
        if donuts[i]==0:
            list2.append(0)
        i+=1
    return list2