# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta

class NiveauRandonneur(metaclass=ABCMeta):
	
    @abstractmethod
    def tempsMoyen(self, distance, pente):
        pass

class NiveauConfirme(NiveauRandonneur):

	def tempsMoyen(self, distance, pente):
		if pente > 0:
			# 3 km/h
			return distance / 3;
		elif pente == 0:
			# 6 km/h
			return distance / 6;
		else: 
			# 30 km/heure
			return distance / 10;


class NiveauDebutant(NiveauRandonneur):

	def tempsMoyen(self, distance, pente):
		if pente > 0:
			# 3 km/h
			return distance / 1;
		elif pente == 0:
			# 6 km/h
			return distance / 12;
		else: 
			# 30 km/heure
			return distance / 5;











