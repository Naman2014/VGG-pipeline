import os
import random
import shutil
from sklearn.model_selection import train_test_split

# Path to your dataset directory
data_dir =  r"E:\Desktop\Carselona\classifying fake and real image\dataset"
# List all classes in your dataset
classes = os.listdir(data_dir)

# Create directories for train, val, test sets
train_dir = os.path.join(data_dir, 'train')
val_dir = os.path.join(data_dir, 'val')
test_dir = os.path.join(data_dir, 'test')

os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Loop through each class folder
for class_name in classes:
    class_dir = os.path.join(data_dir, class_name)
    if os.path.isdir(class_dir):
        # List all files in the class directory
        files = os.listdir(class_dir)
        # Split the files into train, val, test sets
        train_files, test_files = train_test_split(files, test_size=0.2, random_state=42)
        val_files, test_files = train_test_split(test_files, test_size=0.5, random_state=42)
        
        # Create class directories in train, val, test sets
        os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
        os.makedirs(os.path.join(val_dir, class_name), exist_ok=True)
        os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)
        
        # Copy files to respective directories
        for fname in train_files:
            src = os.path.join(class_dir, fname)
            dst = os.path.join(train_dir, class_name, fname)
            shutil.copyfile(src, dst)
        
        for fname in val_files:
            src = os.path.join(class_dir, fname)
            dst = os.path.join(val_dir, class_name, fname)
            shutil.copyfile(src, dst)
        
        for fname in test_files:
            src = os.path.join(class_dir, fname)
            dst = os.path.join(test_dir, class_name, fname)
            shutil.copyfile(src, dst)

# Create a new directory 'main_dataset' and move train, val, test directories into it
main_dataset_dir = os.path.join(data_dir, 'main_dataset')
os.makedirs(main_dataset_dir, exist_ok=True)

shutil.move(train_dir, os.path.join(main_dataset_dir, 'train'))
shutil.move(val_dir, os.path.join(main_dataset_dir, 'val'))
shutil.move(test_dir, os.path.join(main_dataset_dir, 'test'))

print("Dataset successfully organized into 'main_dataset'.")