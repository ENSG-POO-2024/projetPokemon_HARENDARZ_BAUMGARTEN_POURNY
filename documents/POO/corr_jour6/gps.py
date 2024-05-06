# -*- coding: utf-8 -*-
import csv
from datetime import datetime
from shapely.geometry import Point

class Observation:
    def __init__(self, x, y, z, txtdate):
      self.p = Point(x, y, z)
      self.t = datetime.strptime(txtdate, '%Y-%m-%d %H:%M:%S')
        
class TraceGPS:
    def __init__(self, nomfichier):
        self.OBS = []
        with open(nomfichier, mode ='r') as file:
            csvFile = csv.reader(file)
            next(csvFile)
            for row in csvFile:
                t = row[1]
                x, y, z = (float(row[2]), float(row[3]), float(row[4]))
                o = Observation(x,y,z,t)
                self.OBS.append(o)
  
    def __str__(self):
        return str(len(self.OBS))
    
    
t = TraceGPS('../abbaye-de-valcroissant.dat')
print (t)
#t.plot()