import numpy as np
import torch
import torchvision
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms

from a3_ex1 import ImagesDataset
from a6_ex1 import TransformedImagesDataset

def stacking(batch_as_list: list):
    trans_imgs = [sample[0] for sample in batch_as_list] 
    trans_names = [sample[1] for sample in batch_as_list] 
    indices = [sample[2] for sample in batch_as_list] 
    class_ids = [sample[3] for sample in batch_as_list]
    class_names = [sample[4] for sample in batch_as_list]
    img_paths = [sample[5] for sample in batch_as_list]

    stacked_images = torch.stack(trans_imgs, dim=0)

    tensor_list_indices = [torch.tensor(s, dtype=torch.int32) for s in indices]
    stacked_indices = torch.stack(tensor_list_indices, dim = 0)
    stacked_indices = stacked_indices.unsqueeze(1)  # to make separate arrays

    tensor_list_ids = [torch.tensor(s, dtype=torch.int32) for s in class_ids]
    stacked_class_ids = torch.stack(tensor_list_ids, dim = 0)
    stacked_class_ids = stacked_class_ids.unsqueeze(1)

    return (stacked_images, trans_names, stacked_indices, stacked_class_ids, class_names, img_paths)

if __name__ == "__main__":
    dataset = ImagesDataset("./validated_images", 100, 100, int)
    transformed_ds = TransformedImagesDataset(dataset)
    dl = DataLoader(transformed_ds, batch_size=7, shuffle=False, collate_fn=stacking)
    for i, (images, trans_names, indices, classids, classnames, img_paths) in enumerate(dl):
        print(f'mini batch: {i}')
        print(f'images shape: {images.shape}')
        print(f'trans_names: {trans_names}')
        print(f'indices: {indices}')
        print(f'class ids: {classids}')
        print(f'class names: {classnames}\n')