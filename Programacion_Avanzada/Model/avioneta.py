#!/usr/bin/python
# -*- coding: utf-8 -*-
from aeronave import Aeronave

class Avioneta(Aeronave):
    def __init__(self, modelo, capacidad, tamaño, altitudmaxima):
        super().__init__(modelo, capacidad, tamaño)
        self.altitudmaxima = altitudmaxima

    def planear(self, ):
        pass

    def describir(self, ):
        print("Estoy respondiendo desde la clase Avioneta.")

    def getAltitudmaxima(self, ):
        pass

    def setAltitudmaxima(self, value):
        pass
