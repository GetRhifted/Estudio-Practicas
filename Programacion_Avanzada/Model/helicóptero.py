#!/usr/bin/python
# -*- coding: utf-8 -*-
from aeronave import Aeronave

class Helicóptero(Aeronave):
    def __init__(self, modelo, capacidad, tamaño, numerohelices):
        super().__init__(modelo, capacidad, tamaño)
        self.numerohelices = numerohelices

    def volar(self, ):
        pass

    def describir(self, ):
        print("Estoy respondiendo desde la clase Helicóptero.")

    def despegarverticalmente(self, ):
        pass

    def getNumerohelices(self, ):
        pass

    def setNumerohelices(self, value):
        pass
