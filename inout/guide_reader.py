from objects.guide import Guide
from objects.geometry.rectangle import Rectangle


def get_layer_index_from_name(layer_name:str):
	assert layer_name.startswith('Metal')
	layer_name = layer_name.removeprefix('Metal')
	assert layer_name.isnumeric()
	return int(layer_name)


def read_guides(filename:str):
	with open(filename) as file:
		guides:list[Guide] = []
		while True:
			line = file.readline()
			if not line:
				break
			net_name:str = line
			assert file.readline() == '('
			while line != ')':
				line = file.readline()
				tokens = line.split(' ')
				layer = tokens[4]
				tokens = tokens[:-1]
				tokens = list(map(lambda x:int(x), tokens))
				shape = Rectangle(tokens[0], tokens[1], tokens[2], tokens[3])
				guides.append(Guide(shape, net_name, get_layer_index_from_name(layer)))
				continue
			