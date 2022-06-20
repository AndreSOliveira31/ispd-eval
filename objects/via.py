from objects.routing_object import RoutingObject, RoutingObjectType
from objects.geometry.rectangle import Rectangle
from objects.net import Net


class Via(RoutingObject):
	def __init__(self, net: Net, lower_layer: int, upper_layer: int, shape: Rectangle):
		super().__init__(RoutingObjectType.VIA, net, shape, lower_layer)
		self._lower_layer = lower_layer
		self._upper_layer = upper_layer
		
	def __str__(self):
		return "Via from Metal{} to Metal{} at {} with hash {}".format(self._lower_layer + 1, self._upper_layer + 1,
																															 self._shape, self.__hash__())
	
	@staticmethod
	def make_via(net, layer:int, lx:int, ly:int, ux:int, uy:int):
		return Via(net, layer, layer + 1, Rectangle(lx, ly, ux, uy))


