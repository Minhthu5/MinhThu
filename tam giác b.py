# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:29:45 2024

@author:MinhThu
"""
a=float(input("nhập cạnh a: "))
b=float(input("nhập cạnh b: "))
c=float(input("nhập canh c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("đây là tam giác đều")
    elif a == b or b == c or a == c:
        print("đây là tam giác cân")
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2-b**2:
        print("đây là tam giác vuông")
    else:
        print("a, b, c không phải là ba cạnh của một tam giác")
else:
    print("đây là tam giác thường")