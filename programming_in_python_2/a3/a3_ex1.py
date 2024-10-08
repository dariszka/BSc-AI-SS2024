from torch.utils.data import Dataset
from typing import Optional
from PIL import Image
import numpy as np
import os


from a2_ex1 import to_grayscale
from a2_ex2 import prepare_image

class ImagesDataset(Dataset):
    def __init__(
        self,
        image_dir,
        width: int = 100,
        height: int = 100,
        dtype: Optional[type] = None
        ):

        if width < 100 or height < 100:
            raise ValueError
        
        self.image_dir = image_dir
        self.width = width
        self.height = height
        self.dtype = dtype

        found_files = []
        for path in os.listdir(image_dir):
            if os.path.splitext(path)[-1]=='.jpg':
                found_files.append(os.path.abspath(os.path.join(image_dir, path)))
            elif os.path.splitext(path)[-1]=='.csv':
                csv_file = os.path.abspath(os.path.join(image_dir, path)) 

        found_files.sort()
        self.found_files = found_files
    
        csv_contents = np.genfromtxt(csv_file, delimiter=';', dtype=str, skip_header=1)
        # https://stackoverflow.com/questions/2828059/sorting-arrays-in-numpy-by-column
        csv_contents = csv_contents[csv_contents[:, 1].argsort()]

        classids = []
        classnames = []

        for i, name in enumerate(csv_contents):
            classids.append(i)
            classnames.append(name[1])

        self.classnames = classnames
        self.classids = classids        

    def __getitem__(self, index):
        image_path = self.found_files[index]
        with Image.open(image_path) as im:
            image_arr = np.array(im, dtype=self.dtype)
            greyscale_image = to_grayscale(image_arr)
            resized_image = prepare_image(greyscale_image, self.width, self.height, x=0, y=0, size=32)

            return (resized_image[0], self.classids[index], self.classnames[index], image_path)

    def __len__(self):
        return len(self.found_files)
        

# dataset = ImagesDataset("./validated_images", 100, 100, int)

# for resized_image, classid, classname, _ in dataset:
#     print(f'image shape: {resized_image.shape}, dtype: {resized_image.dtype}, '
#     f'classid: {classid}, classname: {classname}\n')