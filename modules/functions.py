from PIL import Image, ImageFilter
import os
from .widgets import *

work_dir = ''
filenames = []
extensions = ['.png', '.jpg']
def filter(listnames):
    output_list =[]
    for i in listnames:
        for j in extensions:
            if j in i:
                output_list.append(i)
    return output_list
def show_dialog():
    global work_dir
    global filenames
    work_dir = filedialog.getExistingDirectory()
    filenames = filter(os.listdir(work_dir))
    print(filenames)

browse.clicked.connect(show_dialog)