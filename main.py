from inout.argument_parser import parse_arguments
from engine.evaluator import Evaluator
		
def main():
	arguments = parse_arguments()
	eval = Evaluator()
	eval.run_flow(arguments.routing)
	

if __name__ == '__main__':
	main()

