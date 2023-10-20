# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 09:30:56 2023

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
def test_answer():
    assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
        1,
        0,
        0,
        2,
        3,
        0,
        0,
        4,
        5,
        0,
        0,
    ]
    assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]