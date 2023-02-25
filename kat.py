#!/usr/bin/env python
from time import sleep
import random
kat ="""
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_) Felix Lee
"""
dino='''
           boing         boing         boing
 e-e           . - .         . - .         . - .
(\_/)\       '       `.   ,'       `.   ,'       .
 `-'\ `--.___,         . .           . .          .
    '\( ,_.-'
       \\               "             "            a:f
       ^'
'''
words="    Sophia is smarter than Albert Einstien! >:D"

def draw (s,t=0.1):
    lines=s.splitlines()
    for l in lines:
        for c in l:
            print (c, end="", flush=True)
            sleep(t)
        print()

pic=random.choice([dino,kat])
draw(pic)
draw (words,0.3)
