# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 11:50:41 2024

@author: kamoliddin
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][1] > arr[j + 1][1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Respublikamizdagi viloyatlar va ularning maydonlari
viloyatlar = [("Andijon", 4200), ("Buxoro", 39400), ("Farg'ona", 6100), 
              ("Jizzax", 20500), ("Namangan", 7600), ("Navoiy", 110800),
              ("Qashqadaryo", 28400), ("Qoraqalpog'iston", 160000), 
              ("Samarqand", 16400), ("Sirdaryo", 5100), ("Surxondaryo", 20000),
              ("Toshkent", 1500), ("Toshkent viloyati", 15000)]

# Bubble sort algoritmini ishga tushiramiz
bubble_sort(viloyatlar)

# Natijalarni chop etamiz
print("Respublikamizdagi viloyatlar maydonini o’sish tartibida:")
for viloyat in viloyatlar:
    print(f"{viloyat[0]}: {viloyat[1]} kv.km")
