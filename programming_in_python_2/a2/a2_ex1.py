import numpy as np
from PIL import Image

def to_grayscale(pil_image: np.ndarray) -> np.ndarray:

    image = pil_image.copy() #copying to make sure sth doesn't go wrong
    if image.ndim == 2:
        # https://stackoverflow.com/questions/49237117/python-add-one-more-channel-to-image
        img = np.expand_dims(image, axis=0)
        return img
    elif image.ndim == 3:
        if image.shape[2] != 3:
            raise ValueError
        else:
            c = image/255 # normalized 
            c_linear = np.where(c <= 0.04045, c/12.92, (((c+0.055)/1.055)**2.4))
            
            y_linear = (c_linear[..., 0] * 0.2126 +
                    c_linear[..., 1] * 0.7152 +
                    c_linear[..., 2] * 0.0722)
            
            y = np.where(y_linear <= 0.0031308, 12.92*y_linear, 1.055*(y_linear**(1/2.4))-0.055)

            if np.issubdtype(image.dtype, np.integer): # denormalized
                y_denormalized = np.round(y * 255)
            else:
                y_denormalized = y * 255
                
            y_denormalized = y_denormalized.astype(image.dtype)
            img = np.expand_dims(y_denormalized, axis=0)

            return img        
    else:
        raise ValueError
    

# I ran it like this:

# image_path = "image.jpg"
# with Image.open(image_path) as im:
#     image_arr = np.array(im)
#     greyscale_image = to_grayscale(image_arr)
