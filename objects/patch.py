from objects.routing_object import RoutingObject, RoutingObjectType

from objects.geometry.rectangle import Rectangle
from objects.net import Net


class Patch(RoutingObject):
	def __init__(self, net:Net, layer:int, shape:Rectangle):
		super().__init__(RoutingObjectType.PATCH, net, shape, layer)

	@staticmethod
	def make_patch(net, layer:int, lx:int, ly:int, ux:int, uy:int):
		return Patch(net, layer, Rectangle(lx, ly, ux, uy))
