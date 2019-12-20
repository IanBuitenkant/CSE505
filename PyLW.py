from pyswip import Prolog
import json
import sys
import os
import glob
from BeautifulSoup import BeautifulSoup
import urllib2
import requests
path = './programs/'
files = glob.glob('./programs/*')
file_store = []
prolog = Prolog()



def list_programs():
	for file_name in file_store:
		new_name = file_name.replace("_","/")
		print(new_name + "\n")

def print_help():
	print("Choose one of the following commands:")
	print("load [url] 	\t	loads a file from the internet")
	print("list 		\t	list all loaded programs")
	print("query_u [query]	\t	perform a prolog query on the union of all loaded programs")
	print("query_i [query]	\t	perform a prolog query on the intersection of all loaded programs")
	print("help 		\t	list the possible commands")
	

def quit():
	print("Goodbye")
	for f in files:
		os.remove(f)
	sys.exit()

def load(file_name):
	#get the html from the specified file and parse its LogicWeb code
	page = urllib2.urlopen(file_name)
	soup = BeautifulSoup(page)
	logic = soup.find(attrs={"lw_code":True})
	#print(type(logic))
	print(str(logic.text))
	new_file_name=file_name.replace("/", "_")
	f = open(path+new_file_name, 'w+')
	f.write(logic.text)
	if not new_file_name in file_store:
                file_store.append(new_file_name)
	else:
		print("file already loaded.")	
	
	

def query_union(query):
	union = []
	for file_name in file_store:
		prolog.consult(path+file_name)
		print("consulting "+file_name)
		res = list(prolog.query(query))
		new_res = []
		for result in res:
			new_res.append(json.dumps(result))
		union = list(set().union(new_res, union))
	print(union)
			
	#For each loaded program, run the query and print all responses

def query_inter(query):
	#For each loaded program, run the query and print only the common responses
	inter = []
        for file_name in file_store:
                prolog.consult(path+file_name)
                print("consulting "+file_name)
                res = list(prolog.query(query))
		new_res = []
                for result in res:
	
                        new_res.append(json.dumps(result))
			if inter == []:
				inter = new_res
                inter = list(set().intersection(new_res, inter))
        print(inter)

def parse(line):
	tokens = line.split()
	
	if(tokens[0] == 'quit'):
		quit()
	elif (tokens[0] == 'load'):
		load(tokens[1])
	elif (tokens[0] == 'query_u'):
		query_union(tokens[1])
	elif (tokens[0] == 'query_i'):
		query_inter(tokens[1])
	elif (tokens[0] == 'help'):
		print_help()
	elif (tokens[0] == 'list'):
		list_programs()



def main():
	line = raw_input("Welcome to LogicWeb. Enter 'help' for a list of commands:\n#>")
	while(True):
		parse(line)
		line = raw_input("#>")

if __name__ == '__main__':
	main()
