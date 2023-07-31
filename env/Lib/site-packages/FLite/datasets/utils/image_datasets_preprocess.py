from PIL import Image
from torch.utils.data import Dataset

"""
This code defines two PyTorch Dataset classes for loading image datasets and performing data preprocessing.

First, a class called ImageDataset is defined, which inherits from the Dataset class. The initialization function of this class requires the following parameters:

images: a list containing the file paths of the images
labels: a list containing the labels of each image
transform_x: a function or transformation operation for preprocessing the image data, can be None
transform_y: a function or transformation operation for preprocessing the label data, can be None
The len method of this class returns the number of images in the dataset, and the getitem method takes an index value and returns the corresponding image data and label at that index. Before returning, if transform_x is specified, the function is used to preprocess the image, and if transform_y is specified, the function is used to preprocess the label.

Next, another class called TransformDataset is defined, which also inherits from the Dataset class. The initialization function of this class is similar to that of the ImageDataset class and requires the following parameters:

images: a list containing the file paths of the images
labels: a list containing the labels of each image
transform_x: a function or transformation operation for preprocessing the image data, can be None
transform_y: a function or transformation operation for preprocessing the label data, can be None
The len method of this class returns the number of images in the dataset, and the getitem method takes an index value and returns the corresponding image data and label at that index. Before returning, if transform_x is specified, the function is used to preprocess the image, and if transform_y is specified, the function is used to preprocess the label. The difference between this class and the ImageDataset class is that the image data and label data in the dataset are saved in self.data and self.targets respectively.
"""


class ImageDataset(Dataset):
    def __init__(self, images, labels, transform_x=None, transform_y=None):
        self.images = images
        self.labels = labels
        self.transform_x = transform_x
        self.transform_y = transform_y

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, index):
        data, label = self.images[index], self.labels[index]
        if self.transform_x is not None:
            data = self.transform_x(Image.open(data))
        else:
            data = Image.open(data)
        if self.transform_y is not None:
            label = self.transform_y(label)
        return data, label


class TransformDataset(Dataset):
    def __init__(self, images, labels, transform_x=None, transform_y=None):
        self.data = images
        self.targets = labels
        self.transform_x = transform_x
        self.transform_y = transform_y

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = self.data[idx]
        target = self.targets[idx]

        if self.transform_x:
            sample = self.transform_x(sample)
        if self.transform_y:
            target = self.transform_y(target)

        return sample, target
