# Create train.txt and test.txt 
import glob, os
import numpy as np 
# Current directory
data_dir = '../can_cuoc_327/'
# Percentage of images to be used for the test set
# Create and/or truncate train.txt and test.txt
file_train = open('data/train.txt', 'w')  
file_test = open('data/valid.txt', 'w')
# Populate train.txt and test.txt
np.random.seed(0)
txt_path = [path for path in glob.glob(data_dir+'*.txt')]
paths = [path for path in glob.glob(data_dir+'*') if path not in txt_path]
total_samples = len(paths)
percent = 0.9
total_train_samples = int(total_samples * percent)
train = paths[:total_train_samples]
test = paths[total_train_samples:]
print(f'Total train: {len(train)}')
print(f'Total test: {len(test)}')

for pathAndFilename in test:  
            file_test.write(pathAndFilename + "\n")
for pathAndFilename in train:
            file_train.write(pathAndFilename + "\n")
print('Create train.txt and test.txt succesful')
