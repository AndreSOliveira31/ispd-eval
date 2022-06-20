from objects.wire import Wire
from objects.via import Via
from objects.patch import Patch
from objects.net import Net

class RoutingSolution:
	def __init__(self):
		self._nets:set[Net] = set()
		self._wires:set[Wire] = set()
		self._vias:set[Via] = set()
		self._patches:set[Patch] = set()

