#!/usr/bin/python
# -*- coding: utf-8 -*-
from aeronave import Aeronave

class Jet(Aeronave):
    def __init__(self, modelo, capacidad, tamaño, velocidadmaxima, cantidadcabinas):
        super().__init__(modelo, capacidad, tamaño)
        self.velocidadmaxima = velocidadmaxima
        self.cantidadcabinas = cantidadcabinas

    def presurizar(self, ):
        pass

    def describir(self, ):
        print("Estoy respondiendo desde la clase Jet.")

    def getVelocidadmaxima(self, ):
        pass

    def setVelocidadmaxima(self, value):
        pass

    def getCantidadcabinas(self, ):
        pass

    def setCantidadcabinas(self, value):
        pass
