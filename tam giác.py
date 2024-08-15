# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:08:30 2024

@author: MinhThu
"""

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b > c and a + c > b and b + c > a:
    print("a, b, c là ba canh của một tam giác")
else:
    print("a, b, c không phải là ba cạnh của một tam giác")