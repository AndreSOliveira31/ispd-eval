from pandas import read_csv

def read_routing_solution_dataframe(filename:str):
	return read_csv(filename)