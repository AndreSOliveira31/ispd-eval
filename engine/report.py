from tabulate import tabulate

WIRE_LENGTH = 'Total Wire Length'
VIA_COUNT = 'Total Via Count'
WRONG_WAY_WIRE_LENGTH = 'Wrong-Way Wire Length'


class Feature:
	def __init__(self, metric_multiplier: float, weight: float):
		self._metric_multiplier = metric_multiplier
		self._weight = weight


class Report:
	def __init__(self):
		self.features: dict[Feature] = {WIRE_LENGTH: Feature(1 / 400, 0.5),
																		VIA_COUNT: Feature(1, 2.0),
																		WRONG_WAY_WIRE_LENGTH: Feature(1 / 400, 1)}
	
	def calculate_row(self, feature_name, value):
		feature = self.features[feature_name]
		metric = value * feature._metric_multiplier
		weight = feature._weight
		score = metric * weight
		return [feature_name, value, metric, weight, score]
	
	def report(self, measurements: dict):
		total_score = 0
		table = [['', 'Value', 'Metric', 'Weight', 'Score'],
						 self.calculate_row(WIRE_LENGTH, measurements[WIRE_LENGTH]),
						 self.calculate_row(VIA_COUNT, measurements[VIA_COUNT]),
						 self.calculate_row(WRONG_WAY_WIRE_LENGTH, measurements[WRONG_WAY_WIRE_LENGTH])]
		for i in range(1, len(table)):
			total_score += table[i][4]
		
		table.append(['Total Score', '-', '-', '-', total_score])
		print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
