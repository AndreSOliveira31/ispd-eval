from dataclasses import dataclass
from enum import Enum

from objects.net import Net

from objects.geometry.rectangle import Rectangle


class RoutingObjectType(Enum):
	WIRE = 1
	VIA = 2
	PATCH = 3


class RoutingObject:
	
	def __init__(self, type: RoutingObjectType, net: Net, shape: Rectangle, layer: int):
		self._type = type
		self._net = net
		self._shape = shape
		self._layer = layer
		
	def as_tuple(self):
		return (self._net, self._layer, self._type, self._shape)
	
	def __hash__(self):
		return hash(self.as_tuple())
