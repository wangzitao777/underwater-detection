import os
import random

data_percent = 1.0
trainval_percent = 0.8
train_percent = 0.8
xmlfilepath = 'data2/train/' + str(data_percent) + '/Annotations'
txtsavepath = 'data2/train/' + str(data_percent) + '/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('data2/train/' + str(data_percent) + '/ImageSets/trainval.txt', 'w')
ftest = open('data2/train/' + str(data_percent) + '/ImageSets/test.txt', 'w')
ftrain = open('data2/train/' + str(data_percent) + '/ImageSets/train.txt', 'w')
fval = open('data2/train/' + str(data_percent) + '/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
