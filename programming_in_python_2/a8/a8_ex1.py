import torch

def compute_confusion_matrix(logits: torch.Tensor, targets: torch.Tensor, num_classes: int ) -> tuple[torch.Tensor, float, float]:
    
    ## handle errors ##

    if not torch.is_tensor(logits) or not torch.is_floating_point(logits):
        raise TypeError('logits is not a torch.Tensor of floating point data type')

    int_dtypes = [torch.uint8, torch.int8, torch.int16, torch.int32, torch.int64]
    if not torch.is_tensor(targets) or not targets.dtype in int_dtypes:
        raise TypeError('targets is not a torch.Tensor of integer data type')
    
    if len(logits.shape) != 2:
        raise ValueError('the shape of logits is not 2D')
    
    if len(targets.shape) != 1:
        raise ValueError('the shape of targets is not 1D')
    
    if logits.shape[0] != len(targets):
        raise ValueError('the first dimension of logits does not have the same size as targets')

    x = torch.where(targets < num_classes, targets, -1)
    if -1 in x:
        raise ValueError('targets is not an integer tensor that contains values smaller than num_classes')

    ###################

    # predictions is the index with the highest value
    # https://stackoverflow.com/questions/53212507/how-to-efficiently-retrieve-the-indices-of-maximum-values-in-a-torch-tensor
    # https://pytorch.org/docs/stable/generated/torch.topk.html#torch.topk
    outputs = torch.sigmoid(logits)
    predictions = torch.topk(outputs, k=1, sorted=False)[1]
    predictions = predictions.flatten()
    
    confusion_matrix = torch.zeros(num_classes, num_classes, dtype=torch.uint8)
    for i,j in zip(targets,predictions):
        confusion_matrix[i][j]+=1

    tp = 0
    fn = 0
    fp = 0
    tn = 0
   
    p=0
    bacc_sum =0

    #https://stats.stackexchange.com/questions/179835/how-to-build-a-confusion-matrix-for-a-multiclass-classifier
    for i in range(num_classes):
        tpi = confusion_matrix[i][i]
        fni = sum(confusion_matrix[i,:]) - tpi
        fpi = sum(confusion_matrix[:, i]) - tpi
        tni = sum(confusion_matrix) - tpi - fni - fpi

        tp += tpi
        fn += fni
        fp += fpi
        tn += tni

        pi=tpi+fni
        p+=pi

        bacc_sum += tpi/pi

    accuracy = tp/p
    balanced_accuracy = bacc_sum/num_classes

    return confusion_matrix, accuracy, balanced_accuracy

if __name__ == "__main__":
    torch.manual_seed(125)
    logits = torch.rand(size=(100,10)) * 10 - 5
    targets = torch.randint(low=0, high=10, size=(100,))
    num_classes = 10
    confusion_matrix, accuracy, balanced_accuracy = compute_confusion_matrix(logits, targets, num_classes)
    print(confusion_matrix)
    print(f'Accuracy: {accuracy:.2f}')
    print(f'Balanced accuracy: {balanced_accuracy:.2f}')