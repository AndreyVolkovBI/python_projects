import sass
import os
import time

sep = os.sep
main = "..."
pathSass = main + "static" + sep + "sass"
pathCss = main + "static" + sep + "css"

while True:
	sass.compile(dirname=(pathSass, pathCss), output_style='compressed')
	time.sleep(1)