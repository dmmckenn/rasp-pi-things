#!/usr/bin/env python
import random
from time import sleep
square_length=15
points=55
xy_crds=[(random.randint(1,square_length-2),random.randint(1,square_length-2)) for i in range(points)]
max_obs=0
while True:
  for i in range(square_length):
    for j in range(square_length):
      if i==0 or j==0 or i==square_length-1 or j==square_length-1:
        print '*',
      elif (i,j) in xy_crds: 
        num=xy_crds.count((i,j))
        if num > max_obs: max_obs=num
        print num,
      else:
        print " ",
    print ""
  for i in range(len(xy_crds)):
    (x,y)=xy_crds[i]
    if random.uniform(0,1)>.5:
      x_move=random.randint(-1,1) 
      if 1 <= x+x_move<= square_length-2:
        x=x+x_move
      y_move=random.randint(-1,1) 
      if 1 <= y+y_move<= square_length-2:
        y=y+y_move
    xy_crds[i]=(x,y)
  print max_obs
  sleep(.5)
