import os


# compress the specific directory png files.
def compress_png_files(dirName):
	files = os.listdir(dirName)
	for fileName in files:
		if not os.path.isdir(fileName):
			# start to compress the png file
			if fileName.endswith('.png'):
				os.system("pngquant --force --output {0} --posterize 4 --skip-if-larger {0}".format(fileName))
		else:
			compress_png_files("{}/{}".format(dirName, fileName))


compress_png_files('.')
