from argparse import ArgumentParser
from dataclasses import dataclass


def parse_arguments():
	parser = create_argument_parser()
	add_arguments_to_parser(parser)
	arguments = parser.parse_args()
	return arguments
	

def create_argument_parser():
	return ArgumentParser(description='Evaluates the score of a given detailed routing solution.')


@dataclass
class Argument:
	name: str
	type: type
	help: str


def add_arguments_to_parser(parser: ArgumentParser):
	arguments: list[Argument] = [Argument('--routing', str, 'Routing solution in csv format.'),]
	for argument in arguments:
		parser.add_argument(argument.name, type=argument.type, help=argument.help)
