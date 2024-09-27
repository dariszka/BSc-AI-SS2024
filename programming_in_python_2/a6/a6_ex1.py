import numpy as np
import torch
import torchvision
import random
from torch.utils.data import Dataset
from torchvision import transforms

from a3_ex1 import ImagesDataset

def augment_image(img_np: np.ndarray, index: int):
    v = index % 7
    trans_img = torch.as_tensor(img_np, dtype=torch.int32)  # not sure if it's a python version problem, but I have to
                                                            # explicitly set the dtype to int32, otherwise it doesn't display correctly 
                                                            # (with keeping old dtype==int64, it would not display at all)
                                                            # in the sample solution for the next task the dtype is int32 anyways

    transformations = [torchvision.transforms.GaussianBlur((3,3)), 
    torchvision.transforms.RandomRotation(360),
    torchvision.transforms.RandomVerticalFlip(),
    torchvision.transforms.RandomHorizontalFlip(),
    torchvision.transforms.ColorJitter((1,2), (1,2), (1,2), (-0.5,0.5))] #making the jitter randomized as well, not that great in the cloud example

    if v == 0:
        trans_name = 'Original'
        
    elif v == 6:
        trans_name = 'Compose'
        random_transformations = random.sample(transformations, 3)
        transform = transforms.Compose(random_transformations)
        trans_img = transform(trans_img)

    else: # v in range [1,5]
        transform = transformations[v-1]
        trans_img = transform(trans_img)
        trans_name = str(transform).split('.')[-1]
        trans_name = str(transform).split('(')[0] 

    return trans_img, trans_name

class TransformedImagesDataset(Dataset):

    def __init__(self, data_set: Dataset):
        super().__init__()
        self.data_set = data_set

    def __getitem__(self, index: int):
        og_ds_i = index // 7 # original dataset index
        image, classid, classname, img_path = self.data_set[og_ds_i]
        trans_img, trans_name = augment_image(image, index)
        index = index
        return trans_img, trans_name, index, classid, classname, img_path

    def __len__(self):
        return len(self.data_set)*7

if __name__ == "__main__":
    from matplotlib import pyplot as plt

    dataset = ImagesDataset("./validated_images", 100, 100, int)
    transformed_ds = TransformedImagesDataset(dataset)

    fig, axes = plt.subplots(2, 4)
    for i in range(0, 8):
        trans_img, trans_name, index, classid, classname, img_path = transformed_ds.__getitem__(i)
        _i = i // 4
        _j = i % 4
        axes[_i, _j].imshow(transforms.functional.to_pil_image(trans_img))
        axes[_i, _j].set_title(f'{trans_name}\n{classname}')
    fig.tight_layout()
    plt.show()




