# This repository contains all Python API Projects
import webbrowser

helloString = "Here you can find lots of Python Projects!"
chooseString = "Choose one of them by typing the number of the project:"
sep = "----------"*5
error = "Something went wrong, please, try again!"
projects = [{"Vk Connections API":"https://github.com/AndreyVolkovBI/python_projects/tree/vk_connections_api"},
			{"Raccoonn.ru Flask Application":"https://github.com/AndreyVolkovBI/python_projects/tree/flask_raccoonn_ru"}]   # {name_of_project: url}


while True:
	print(sep)
	print(helloString)
	print(chooseString)
	count = 1
	for project in projects:
		name = list(project.keys())[0]
		print(count, name, sep=". ")
		count += 1
	n = input()
	try:
		n = int(n.strip())
		item = list(projects[n - 1].values())[0]
		webbrowser.open(item, new=2)
	except:
		print(sep)
		print(error)
