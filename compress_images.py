import os
import sys


# compress the specific directory png files.
def compress_png_files(dir_name):
    files = os.listdir(dir_name)
    for file_name in files:
        if not os.path.isdir(file_name):
            if file_name.endswith(".png"):
                os.system("pngquant --force --output {0} --posterize 4 --skip-if-larger {0}".format(file_name))
        else:
            compress_png_files("{}/{}".format(dir_name, file_name))


arg_len = 0
# make sure there is one argument
for argv in sys.argv:
    arg_len += 1
else:
    if arg_len <= 1:
        print("compress current directory images...")
        compress_png_files(".")
    else:
        compress_path = sys.argv[1]
        if not compress_path:
            compress_png_files(compress_path)
