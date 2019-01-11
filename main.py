# This repository contains all Python API Projects
import webbrowser

helloString = "Here you can find lots of Python Projects!"
chooseString = "Choose one of them by typing the number of the project:"
sep = "----------"*5
error = "Something went wrong, please, try again!"
projects = [{"":""}]   # {name_of_project: url}


while True:
	print(sep)
	print(helloString)
	print(chooseString)
	n = input()
	try:
		n = int(n.strip())
		item = list(projects[n].values())[0]
		webbrowser.open(item, new=2)
	except:
		print(sep)
		print(error)
