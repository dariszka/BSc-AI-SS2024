from torch.utils.data import Dataset, DataLoader
import torch
from a3_ex1 import ImagesDataset

def stacking(batch_as_list: list): 
    images = [sample[0] for sample in batch_as_list] 
    class_ids = [sample[1] for sample in batch_as_list]
    class_names = [sample[2] for sample in batch_as_list]
    image_filepaths = [sample[3] for sample in batch_as_list]

    # tensor_list_images = [torch.tensor(s) for s in images]
    stacked_images = torch.stack(images, dim=0)

    # tensor_list_ids = [torch.tensor(s) for s in class_ids] 
    # this will by default it will set to int64, 
    # but in the example output we had int32, so im explicitly changing it:
    tensor_list_ids = [torch.tensor(s, dtype=torch.int32) for s in class_ids]
    stacked_class_ids = torch.stack(tensor_list_ids, dim = 0)

    # https://stackoverflow.com/questions/43328632/pytorch-reshape-tensor-dimension
    stacked_class_ids = stacked_class_ids.unsqueeze(1) # to make separate arrays

    return (stacked_images, stacked_class_ids, class_names, image_filepaths)

    
ds = ImagesDataset("./validated_images", 100, 100, int)
dl = DataLoader(ds, batch_size=2, shuffle=False, collate_fn=stacking)
for i, (images, classids, classnames, image_filepaths) in enumerate(dl):
    print(f'mini batch: {i}')
    print(f'images shape: {images.shape}')
    print(f'class ids: {classids}')
    print(f'class names: {classnames}\n')
