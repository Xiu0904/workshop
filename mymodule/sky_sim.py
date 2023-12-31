#! /usr/local/envs/myenv python
"""Determine Andromeda location in ra/dec degrees"""

from math import cos, pi
from random import uniform

NSRC = 1_000_000
# from wikipedia
RA = '00:42:44.3'
DEC = '41:16:09'

def make_positions():
  # convert to decimal degrees
  d, m, s = DEC.split(':')
  DEC0 = int(d)+int(m)/60+float(s)/3600

  h, m, s = RA.split(':')
  RA0 = 15*(int(h)+int(m)/60+float(s)/3600)
  RA0 = RA0/cos(DEC0*pi/180)

  # make 1000 stars within 1 degree of Andromeda

  ras = []
  decs = []
  for i in range(NSRC):
    ras.append(RA0 + uniform(-1,1))
    decs.append(DEC0 + uniform(-1,1))
  return ras, decs

def save_positions(ras, decs):
  # now write these to a csv file for use by my other program
  with open('/content/drive/My Drive/ADACSECRPythonWorkshop/catalog.csv','w', encoding='utf8') as f:
    print("id,ra,dec", file=f)
    for i in range(len(ras)):
      print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)

def main():
  ras, decs = make_positions()
  save_positions(ras, decs)

if __name__ == "__main__":
  main()