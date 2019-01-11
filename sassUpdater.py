import sass
import os
import time

sep = os.sep
pathSass, pathCss = "XXX", "XXX"

while True:
	sass.compile(dirname=(pathSass, pathCss), output_style='compressed')
	time.sleep(1)