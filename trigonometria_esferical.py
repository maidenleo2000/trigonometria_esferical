#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math as m

# Este es  el módulo que permite calcular cuanto debería esconderse el horizonte
# bajo la curvatura de la Tierra si esta fuera una bola

L = input('Introduce la distancia (en Kms): ')
response = 6373-(6373*(m.cos(m.asin(float(L)/6373))))
response *= 1000
print (f'El horizonte se esconde  {str(response)} metros en una esfera')
