import os
import random
import shutil


def list_sort(x: str):
    x = x[21:-4]  # file number
    return int(x)


data_percent = 1.0
xml_file_path = 'data2/train/Annotations'
total_xml = os.listdir(xml_file_path)
total_xml.sort(key=list_sort)
jpg_file_path = 'data2/train/images'
total_jpg = os.listdir(jpg_file_path)
total_jpg.sort(key=list_sort)

num = len(total_xml)
list = range(num)
to_be_spilted_num = int(num * data_percent)
print(f"number of to be spilted: {to_be_spilted_num}")
to_be_spilted = random.sample(list, to_be_spilted_num)

if not os.path.exists('data2/train/' + str(data_percent) + '/images'):
    os.makedirs('data2/train/' + str(data_percent) + '/images')
if not os.path.exists('data2/train/' + str(data_percent) + '/Annotations'):
    os.makedirs('data2/train/' + str(data_percent) + '/Annotations')
if not os.path.exists('data2/train/' + str(data_percent) + '/labels'):
    os.makedirs('data2/train/' + str(data_percent) + '/labels')
if not os.path.exists('data2/train/' + str(data_percent) + '/ImageSets'):
    os.makedirs('data2/train/' + str(data_percent) + '/ImageSets')

for i in list:
    if i in to_be_spilted:
        try:
            shutil.copy('data2/train/Annotations/' + total_xml[i], 'data2/train/' + str(data_percent) + '/Annotations')
            shutil.copy('data2/train/images/' + total_jpg[i], 'data2/train/' + str(data_percent) + '/images')
        except IOError as e:
            print("Unable to copy file. %s" % e)
