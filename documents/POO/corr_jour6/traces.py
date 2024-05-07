# -*- coding: utf-8 -*-

import csv
from datetime import datetime
import math
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString


class Observation:
    
    def __init__(self, x, y, z, tms):
        self.geom = Point(x, y, z)
        self.tms = tms
        self.abscurv = 0
        self.pente = 0
    
    def getGeom(self):
        return self.geom
    def getTms(self):
        return self.tms.timestamp()
    def getAbsCurv(self):
        return self.absCurv
    def getPente(self):
        return self.pente
    
    def setPente(self, pente):
        self.pente = pente
    def setAbsCurv(self, absCurv):
        self.absCurv = absCurv
    

class TraceGPS:
    
    #private Itineraire itineraire;
    #private List<Observation> OBS;
    #private Activite activite;
    
    def __init__ (self, filename):
        
        COORDS = []
        self.OBS = []
        with open(filename, mode ='r')as file:
            csvFile = csv.reader(file)
            next(csvFile)
            for line in csvFile:
                stDate = line[1]
                ts = datetime.strptime(stDate, '%Y-%m-%d %H:%M:%S')
                x = line[2]
                y = line[3]
                z = line[4]
                p = Observation(float(x), float(y), float(z), ts)
                COORDS.append([float(x), float(y)])
                self.OBS.append(p)
                
        self.geom = LineString(COORDS)
        self.__compute()
    

    def __compute(self):
        
        self.OBS[0].setAbsCurv(0)
        self.OBS[0].setPente(0)
        
        absCurv = 0
        for i in range(1, len(self.OBS)):
            obs1 = self.OBS[i-1]
            obs2 = self.OBS[i]
            
            d = obs1.geom.distance(obs2.geom)
            
            deniv = obs2.geom.z - obs1.geom.z
            pente = math.atan( deniv / d) * 180 / math.pi
            obs2.setPente(pente)
            
            absCurv += d
            obs2.setAbsCurv(absCurv)
            
    def getLastObs(self):
        return self.OBS[len(self.OBS)-1]
            
    def __str__(self):
        t1 = self.OBS[0].getTms()
        t2 = self.getLastObs().getTms()
        delta = t2-t1
        
        txt = '-------------------------------------\n'
        txt += 'Nb of pt(s):  ' + str(len(self.OBS)) + '\n'
        txt += 'Starting at:  ' + str(t1) + '\n'
        txt += 'Ending at:    ' + str(t2) + '\n'
        txt += 'Duration:     ' + str(delta) + ' s \n'
        txt += 'Length:       ' + str(round(self.getLastObs().getAbsCurv())) + ' m \n'
        txt += 'Boucle:       ' + str(self.isBoucle(50)) + ' \n'
        txt += '-------------------------------------'
        return txt
    
    
    def plot(self):
        X = []
        Y = []
        for i in range(0, len(self.OBS)):
            obs = self.OBS[i]
            X.append(obs.geom.x)
            Y.append(obs.geom.y)
        
        plt.figure(figsize=(8, 8))
        plt.plot(X, Y, 'r-', markersize=4)


    def isBoucle(self, seuil):
        p0 = self.OBS[0].geom
        print (p0.distance(self.OBS[-1].geom))
        return self.OBS[-1].geom.buffer(seuil).intersects(p0)
    


    def vitesseReelParcours(self):
        d = self.OBS[-1].getAbsCurv()
        t = self.OBS[-1].getTms() - self.OBS[0].getTms()

        return d / t * 3.6
        
    
    def vitesseTheoriqueParcours(self, niveau):
        d = 0.0
        t = 0.0
        
        for i in range(1, len(self.OBS)):
            obs1 = self.OBS[i-1]
            obs2 = self.OBS[i]
            di = obs1.geom.distance(obs2.geom)
            d += di
            
            pi = self.OBS[i].pente
            t = t + niveau.tempsMoyen(di, pi);

        return d / t;

        
