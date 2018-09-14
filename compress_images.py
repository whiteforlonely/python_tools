import os
import sys


# compress the specific directory png files.
def compress_png_files(dir_name):
    files = os.listdir(dir_name)
    for file_name in files:
        # here should direct the file path
        file_name = "{}/{}".format(dir_name, file_name)
        if not os.path.isdir(file_name):
            # print("come to file is not dir")
            if file_name.endswith(".png"):
                # print("{} is png file".format(file_name))
                os.system("pngquant --force --output {0} --posterize 4 --skip-if-larger {0}".format(file_name))
                print("compress png: {} ok.".format(file_name))
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
        print("the argument is {}. start to compress path".format(compress_path))
        if compress_path:
            compress_png_files(compress_path)
