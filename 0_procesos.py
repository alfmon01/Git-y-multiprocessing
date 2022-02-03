# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 18:20:56 2022

@author: Alfonso
"""

from time import sleep
from random import random
from multiprocessing import Process

def f():
 for i in range(5):
     print ("hola", i)
     sleep(random())
 
if __name__ == "__main__":
 p = Process(target=f)
 q = Process(target=f)
 p.start()
 q.start()
 print ("fin")
