from dataclasses import dataclass

@dataclass
class Net:
	_name: str
	
	def __hash__(self):
		return hash(self._name)