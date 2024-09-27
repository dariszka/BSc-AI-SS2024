**Disclaimer: Some of the assignments from this course are also uploaded to my GitHub in the image-dataset-prep and cnn repos, where some development progress can be seen. 'Some' is really stressed here, since GitHub management was not a priority at the time.**

### **Assignment 1:**  
Creating a system to validate images based on specific criteria like format, size, and variance.

1. **Image validation pipeline**: Implemented a system to validate images in a directory based on specific criteria like file format, size, dimensions, and variance. Invalid images were logged and excluded from further processing.

---

### **Assignment 2:**  
Conversion of images to grayscale and resizing them to meet specified dimensions.

1. **Grayscale conversion**: Implemented a function to convert images to grayscale using a specific formula for luminance, ensuring correct processing for 2D and 3D image arrays.
   
2. **Image preparation**: Created a function to resize and crop images, ensuring they meet predefined width and height while handling padding and subarea extraction.

---

### **Assignment 3:**  
Custom PyTorch dataset class for loading and preprocessing images for training.

1. **Custom dataset class**: Implemented a PyTorch dataset class to load and preprocess images, converting them to grayscale and resizing them to fixed dimensions. The dataset class also associates each image with its class label based on a CSV file.

2. **Batch stacking**: Created a custom collate function to stack images, class IDs, and names into batches for efficient training using PyTorch’s DataLoader.

---

### **Assignment 4:**  
Simple neural networks for image classification, including both fully connected and convolutional layers.

1. **Simple Feedforward Network**: Designed and implemented a fully connected neural network in PyTorch with multiple layers and ReLU activation, including control over bias usage and customizable hidden layer sizes.

2. **Convolutional Neural Network**: Developed a simple convolutional neural network (CNN) with variable kernel sizes, batch normalization, and ReLU/ELU activation for image classification tasks.

---

### **Assignment 5:**  
Training loop for neural networks, including tracking losses and integrating early stopping for efficient training.

1. **Training loop**: Built a training loop for a neural network, including forward passes, backpropagation, and evaluation on validation data. Losses for both training and validation sets were tracked across epochs.

2. **Early stopping and loss plotting**: Enhanced the training loop with early stopping based on the validation loss and implemented a plotting function to visualize training and evaluation losses over time.

---

### **Assignment 6:**  
Augmenting images and stacking them into batches for efficient training.

1. **Image Augmentation**: Created a function that applies a variety of transformations (e.g., Gaussian blur, rotation, flips, color jitter) to images, enhancing the diversity of the training data.
   
2. **Batch Stacking**: Implemented a stacking function to group images and associated metadata into batches for training using PyTorch’s DataLoader.

---

### **Assignment 7:**  
Building, training, and evaluating a custom CNN using PyTorch, designed to classify images from a custom dataset.

1. **CNN Architecture**: Designed and implemented a multi-layer CNN using **convolutional layers**, **batch normalization**, and **ReLU activations**, with dropout for regularization and max-pooling for downsampling.
   
2. **Custom Dataset Class**: Created a custom PyTorch dataset class to load images from the filesystem, preprocess them by converting to grayscale, resizing, and extracting subareas for consistent input dimensions.

3. **Data Splitting**: Implemented a function to split the dataset into training, validation, and test sets, ensuring balanced distribution using a predefined seed for reproducibility.

4. **Training Loop**: Built a training loop with progress tracking, backpropagation, and optimizer management. Losses for both training and validation sets were tracked across epochs.

5. **Model Evaluation**: Evaluated the model’s performance on unseen test data, calculating accuracy using the accuracy score from the predictions.

---

### **Assignment 8:**  
Calculating a confusion matrix and evaluating model accuracy for multi-class classification tasks.

1. **Confusion Matrix and Model Accuracy**: Implemented a function from scratch using torch to compute the confusion matrix from model predictions and targets, tracking true positives, false negatives, false positives, and true negatives Calculated both overall accuracy and balanced accuracy, offering insights into the model's performance across all classes.