from objects.geometry.rectangle import Rectangle

from objects.net import Net


class Guide:
	def __init__(self, shape:Rectangle, net:Net, layer:int):
		self._shape = shape
		self._net = net
		self._layer = layer