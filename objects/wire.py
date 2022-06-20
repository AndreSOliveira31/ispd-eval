from enum import Enum, unique

from objects.routing_object import RoutingObject, RoutingObjectType

from objects.geometry.rectangle import Rectangle
from objects.net import Net

from keys import *

@unique
class Direction(Enum):
	HORIZONTAL = 1
	VERTICAL = 2
	

def get_direction(rectangle:Rectangle):
	x = abs(rectangle.upper_x - rectangle.lower_x)
	y = abs(rectangle.upper_y - rectangle.lower_y)
	if x > y:
		return Direction.HORIZONTAL
	else:
		return Direction.VERTICAL
	


class Wire(RoutingObject):
	def __init__(self, net:Net, layer:int, shape:Rectangle):
		super().__init__(RoutingObjectType.WIRE, net, shape, layer)
		self._direction = get_direction(shape)
	
	@staticmethod
	def make_wire(net, layer: int, lx: int, ly: int, ux: int, uy: int):
		return Wire(net, layer, Rectangle(lx, ly, ux, uy))


def get_wire_length(wire: Wire):
	if wire._direction == Direction.HORIZONTAL:
		return abs(wire._shape.upper_x - wire._shape.lower_x)
	else:
		return abs(wire._shape.upper_y - wire._shape.lower_y)