

def make_label_image(label_image, masks):
    '''
    Creates a label image by adding one mask at a time onto an empty image.

    Inputs:
    - A label image of zeros, in the same size and shape of your original image.
    - A list of masks from an ultralytics segmentation
    Outputs:
    - A label-image of all masks
    '''
    for enum, mask in enumerate(masks):
        curr_label = mask.data.cpu().numpy() # Converting from tensors to a numpy compatible array on the CPU
        mnarray = curr_label.squeeze() # reduce each mask into 2D array
        label_image[mnarray] = enum + 1 # set each mask to a unique ID (enum)

    return(label_image)

if __name__ == "__main__":
    masks = results[0].masks # Ultralytics masks are a component of the results (predictions)
    array_shape = [masks.shape[1], masks.shape[2]] # Getting the 2D shape
    label_image = np.zeros(array_shape, dtype=np.int32) # Creates a label image
    make_label_image(label_image, masks)
