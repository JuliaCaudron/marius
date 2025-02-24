# -*- coding: utf-8 -*-
from MCP3008 import MCP3008

adc = MCP3008()
value = adc.read( channel = 0 ) # Vous pouvez bien entendu adapter le canal à lire
print("Tension appliquée : %.2f" % (value / 1023.0 * 3.3) )