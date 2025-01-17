import random
import time

import torch
import numpy as np
from scipy.io import loadmat
from sklearn import preprocessing

DATASETS_CONFIG = {
    'PaviaU': {
        'img': 'PaviaU.mat',
        'gt': 'PaviaU_gt.mat'
    },
    'KSC': {
        'img': 'KSC.mat',
        'gt': 'KSC_gt.mat'
    },
    'IndianPines': {
        'img': 'indian_pines.mat',
        'gt': 'indian_pines_gt.mat'
    },
    'Salinas': {
        'img': 'salinas.mat',
        'gt': 'salinas_gt.mat'
    },
    'Houston': {
        'img': 'Houston.mat',
        'gt': 'Houston_gt.mat'
    },
    'Botswana': {
        'img': 'Botswana.mat',
        'gt': 'Botswana_gt.mat'
    },
    'WHU-Hi-LongKou': {
        'img': 'WHU_Hi_LongKou.mat',
        'gt': 'WHU_Hi_LongKou_gt.mat'
    },
    'WHU-Hi-HanChuan': {
        'img': 'WHU_Hi_HanChuan.mat',
        'gt': 'WHU_Hi_HanChuan_gt.mat'
    }
}


def get_dataset(logger, dataset_name, target_folder="./dataset/", datasets=DATASETS_CONFIG):
    """ Gets the dataset specified by name and return the related components.
    Args:
        dataset_name: string with the name of the dataset
        target_folder (optional): folder to store the datasets, defaults to ./
        datasets (optional): dataset configuration dictionary, defaults to prebuilt one
    Returns:
        img: 3D hyperspectral image (WxHxB)
        gt: 2D int array of labels
        label_values: list of class names
        ignored_labels: list of int classes to ignore
        rgb_bands: int tuple that correspond to red, green and blue bands
    """
    if dataset_name not in datasets.keys():
        raise ValueError("{} dataset is unknown.".format(dataset_name))

    img_file = target_folder + dataset_name + '/' + datasets[dataset_name].get('img')
    gt_file = target_folder + dataset_name + '/' + datasets[dataset_name].get('gt')
    if dataset_name == 'Houston':
        # Load the image
        img = loadmat(img_file)['Houston']

        gt = loadmat(gt_file)['Houston_gt']

        label_values = ["Undefined", "Healthy grass", "Stressed grass", " Synthetic grass",
                        "Trees", "Soil", "Water", "Residential", "Commercial", "Road",
                        "Highway", "Railway", "Parking Lot 1", "Parking Lot 2",
                        "Tennis Court", "Running Track"]

        ignored_labels = [0]

    elif dataset_name == 'PaviaU':
        # Load the image
        img = loadmat(img_file)['paviaU']

        gt = loadmat(gt_file)['Data_gt']

        label_values = ['Undefined', 'Asphalt', 'Meadows', 'Gravel', 'Trees',
                        'Painted metal sheets', 'Bare Soil', 'Bitumen',
                        'Self-Blocking Bricks', 'Shadows']

        ignored_labels = [0]

    elif dataset_name == 'IndianPines':
        # Load the image
        
        img = loadmat(img_file)
        img = img['HSI_original']

        gt = loadmat(gt_file)['Data_gt']
        label_values = ["Undefined", "Alfalfa", "Corn-notill", "Corn-mintill",
                        "Corn", "Grass-pasture", "Grass-trees",
                        "Grass-pasture-mowed", "Hay-windrowed", "Oats",
                        "Soybean-notill", "Soybean-mintill", "Soybean-clean",
                        "Wheat", "Woods", "Buildings-Grass-Trees-Drives",
                        "Stone-Steel-Towers"]

        ignored_labels = [0]

    elif dataset_name == 'Botswana':
        # Load the image
        img = loadmat(img_file)['Botswana']

        gt = loadmat(gt_file)['Botswana_gt']
        label_values = ["Undefined", "Water", "Hippo grass",
                        "Floodplain grasses 1", "Floodplain grasses 2",
                        "Reeds", "Riparian", "Firescar", "Island interior",
                        "Acacia woodlands", "Acacia shrublands",
                        "Acacia grasslands", "Short mopane", "Mixed mopane",
                        "Exposed soils"]

        ignored_labels = [0]

    elif dataset_name == 'KSC':
        # Load the image
        img = loadmat(img_file)['KSC']

        gt = loadmat(gt_file)['KSC_gt']
        label_values = ["Undefined", "Scrub", "Willow swamp",
                        "Cabbage palm hammock", "Cabbage palm/oak hammock",
                        "Slash pine", "Oak/broadleaf hammock",
                        "Hardwood swamp", "Graminoid marsh", "Spartina marsh",
                        "Cattail marsh", "Salt marsh", "Mud flats", "Wate"]

        ignored_labels = [0]

    elif dataset_name == 'Salinas':
        # Load the image
        img = loadmat(img_file)['HSI_original']

        gt = loadmat(gt_file)['Data_gt']
        label_values = ["Undefined", "Brocoli green weeds 1", "Brocoli_green_weeds_2",
                        "Fallow", "Fallow rough plow", "Fallow smooth", "Stubble",
                        "Celery", "Grapes untrained", "Soil vinyard develop",
                        "Corn senesced green weeds", "Lettuce romaine 4wk",
                        "Lettuce romaine 5wk", "Lettuce romaine 6wk", "Lettuce romaine 7wk",
                        "Vinyard untrained", "Vinyard vertical trellis"]

        ignored_labels = [0]


    elif dataset_name == 'WHU-Hi-LongKou':
        # Load the image

        img = loadmat(img_file)['WHU_Hi_LongKou']

        gt = loadmat(gt_file)['WHU_Hi_LongKou_gt']
        
        label_values = ["Corn", "Cotton", "Sesame",
                        "Broad-leaf soybean", "Narrow-leaf soybean", "Rice", "Water",
                        "Roads and houses", "Mixed weed"]

        ignored_labels = [0]

    elif dataset_name == 'WHU-Hi-HanChuan':
        # Load the image

        img = loadmat(img_file)['WHU_Hi_HanChuan']

        gt = loadmat(gt_file)['WHU_Hi_HanChuan_gt']
        
        label_values = ["Undefined", "Alfalfa", "Corn-notill", "Corn-mintill",
                        "Corn", "Grass-pasture", "Grass-trees",
                        "Grass-pasture-mowed", "Hay-windrowed", "Oats",
                        "Soybean-notill", "Soybean-mintill", "Soybean-clean",
                        "Wheat", "Woods", "Buildings-Grass-Trees-Drives",
                        "Stone-Steel-Towers"]

        ignored_labels = [0]

    # 检查像元是否为空
    nan_mask = np.isnan(img.sum(axis=-1))
    if np.count_nonzero(nan_mask) > 0:
        logger.info("Warning: NaN have been found in the data. It is preferable to remove them beforehand. Learning on NaN "
              "data is disabled.")
    img[nan_mask] = 0
    gt[nan_mask] = 0
    ignored_labels.append(0)
    ignored_labels = list(set(ignored_labels))
    # # Normalization
    # img = np.asarray(img, dtype='float32')#（145*145*200）
    # data = img.reshape(np.prod(img.shape[:2]), np.prod(img.shape[2:]))#(21025,200)
    # data = preprocessing.minmax_scale(data, axis=1)#对像素进行缩放，将数据在缩放在固定区间，默认缩放到区间 [0, 1]
    # # data = preprocessing.scale(data, axis=1)#对像素进行缩放，将数据在缩放在固定区间，默认缩放到区间 [0, 1]
    # scaler = preprocessing.StandardScaler().fit(data)#这一步可以得到scaler，里面存的有计算出来的均值和方差
    # data = scaler.fit_transform(data)#这一步再用scaler中的均值和方差来转换data，使data标准化
    # img = data.reshape(img.shape) 
    return img, gt, label_values, ignored_labels


class HyperX(torch.utils.data.Dataset):
    """ Generic class for a hyperspectral scene """

    def __init__(self, data, gt, **hyperparams):
        """
        Args:
            data: 3D hyperspectral image
            gt: 2D array of labels
            patch_size: int, size of the spatial neighbourhood
            center_pixel: bool, set to True to consider only the label of the
                          center pixel
            data_augmentation: bool, set to True to perform random flips
            supervision: 'full' or 'semi' supervised algorithms
        """
        super(HyperX, self).__init__()
        self.data = data
        self.label = gt
        self.dataset_name = hyperparams['dataset']
        self.patch_size = hyperparams['patch_size']
        self.ignored_labels = set(hyperparams['ignored_labels'])
        self.center_pixel = True
        supervision = 'full'
        if supervision == 'full':#设置所有类别参与训练
            mask = np.ones_like(gt)
            for l in self.ignored_labels:
                mask[gt == l] = 0                #gt=0的话，mask这个像素为0
        elif supervision == 'semi':    #若该patch大小覆盖了图像边缘之外的部分，该像素丢弃   
            mask = np.ones_like(gt)
        x_pos, y_pos = np.nonzero(mask)#获取每个点的位置 
        # p = self.patch_size // 2+2#!!!!!!!!!!!错位裁剪注意这里+2
        p = self.patch_size // 2

        self.indices = np.array([(x, y) for x, y in zip(x_pos, y_pos) if
                                 x > p and x < data.shape[0] - p and y > p and y < data.shape[1] - p])
        self.labels = [self.label[x, y] for x, y in self.indices]
        np.random.shuffle(self.indices) #打乱数组或列表里面元素的顺序
    
    
    
    @staticmethod
    def get_data(data, x, y, patch_size, data_3D=False):
        x1, y1 = x - patch_size // 2, y - patch_size // 2
        x2, y2 = x1 + patch_size, y1 + patch_size  #注意：并不等同于x2, y2 = x + patch_size // 2, y + patch_size // 2
        data = data[x1:x2, y1:y2] #15*15*200

        # Copy the data into numpy arrays (PyTorch doesn't like numpy views)
        data = np.asarray(np.copy(data).transpose((2, 0, 1)), dtype='float32')
        # Load the data into PyTorch tensors
        data = torch.from_numpy(data)
        return data
        

    def __len__(self):
        return len(self.indices)

    def __getitem__(self, i):
        x, y = self.indices[i]
        data1 = self.get_data(self.data, x, y, self.patch_size, data_3D=False)
        # data2 = self.get_data(self.data, x-2, y+2, self.patch_size, data_3D=False)
        data2 = data1#使用错位裁剪时这里注意要注释掉
        x1, y1 = x - self.patch_size // 2, y - self.patch_size // 2
        x2, y2 = x1 + self.patch_size, y1 + self.patch_size
        label = self.label[x1:x2, y1:y2]
        label = np.asarray(np.copy(label), dtype='int64')
        label = torch.from_numpy(label)

        label = np.asarray(np.copy(label), dtype='int64')
        
        if self.center_pixel and self.patch_size > 1:
            label = label[self.patch_size // 2, self.patch_size // 2]
        # Remove unused dimensions when we work with invidual spectrums
        elif self.patch_size == 1:
            data = data[:, 0, 0]
            label = label[0, 0]

        # # Add a fourth dimension for 3D CNN
        # if self.patch_size > 1:
        #     data = data.unsqueeze(0)# Make 4D data ((Batch x) Planes x Channels x Width x Height)

        
        return data1,data2,label