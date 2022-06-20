import pandas

from keys import Keys
from inout.routing_solution_reader import read_routing_solution_dataframe
from objects.routing_solution import RoutingSolution
from objects.wire import Wire, Direction, get_wire_length
from objects.via import Via
from objects.patch import Patch
from objects.net import Net

from engine.report import *


class Evaluator:
	def __init__(self, routing_direction_reversed:bool = False):
		self._routing_direction_reversed = routing_direction_reversed
		if self._routing_direction_reversed:
			self.layer_direction = {1:Direction.HORIZONTAL, 0:Direction.VERTICAL}
		else:
			self.layer_direction = {0:Direction.HORIZONTAL, 1:Direction.VERTICAL}
	
	def get_layer_direction(self, layer:int):
		return self.layer_direction[layer%2]
		
	def run_flow(self, routing_filename: str):
		data_frame = read_routing_solution_dataframe(routing_filename)
		routing_solution: RoutingSolution = self.build_routing_solution_from_data_frame(data_frame)
		print('Routing solution has {} wires, {} vias an {} patches.'.format(len(routing_solution._wires),
																																				 len(routing_solution._vias),
																																				 len(routing_solution._patches)))
		measurements = dict()
		measurements[WIRE_LENGTH], measurements[WRONG_WAY_WIRE_LENGTH] = self.calculate_wire_lengths(
			routing_solution._wires)
		# The number of vias is divided by 2 because the vias have two objects, the bottom- and top-layer, each with a
		# potentially different shape
		measurements[VIA_COUNT] = len(routing_solution._vias) / 2
		Report().report(measurements)
	
	def print_vias(vias: set[Via]):
		via: Via
		for via in vias:
			print(via)
	
	def calculate_wire_lengths(self, wires: set[Wire]):
		total_wl = 0
		wrong_way_wl = 0
		for wire in wires:
			wl = get_wire_length(wire)
			total_wl += wl
			if wire._direction != self.get_layer_direction(wire._layer):
				wrong_way_wl += wl
		return total_wl, wrong_way_wl
	
	@staticmethod
	def build_routing_solution_from_data_frame(data_frame: pandas.DataFrame):
		routing_solution = RoutingSolution()
		for _, row in data_frame.iterrows():
			routing_solution._nets.add(Net(row[Keys.NET]))
			match row[Keys.TYPE]:
				case Keys.WIRE:
					builder_function, container = Wire.make_wire, routing_solution._wires
				case Keys.VIA:
					builder_function, container = Via.make_via, routing_solution._vias
				case Keys.PATCH:
					builder_function, container = Patch.make_patch, routing_solution._patches
				case _:
					print('[Warning] Skipping unknown routing object type {}.'.format(row['type']))
					continue
			container.add(builder_function(row[Keys.NET],
																		 row[Keys.LAYER],
																		 row[Keys.LOWER_X],
																		 row[Keys.LOWER_Y],
																		 row[Keys.UPPER_X],
																		 row[Keys.UPPER_Y]))
		return routing_solution
