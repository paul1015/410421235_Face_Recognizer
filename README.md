

# Specifications of the Face Recognizer System
* Train a facial recognition system using deep learning.


## Related Tool
* Langue- Python
* Tool - Keras , PIL
* Neural Network - CNN 
* Model - Sequential
* Batch size - 16
* Optimizer - Adadelta 


## Related Technique
* Conv2D
* Dropout
* MaxPooling2D
* activation - Relu , Softmax
* Valid Padding
* Crossentropy

## test recognizer to evaluate its recognition rate
* Test all the photos, record the total number of identification errors, and fewer errors indicate higher training accuracy.
 
 
## the problems suffered in our development
If the batch size is too large, the GPU won't handle it, so it shouldn't be set too high.
 
## any bonus features or functionalities included in your recognizer
We trained the model using datasets consisting of 20 images each from three different individuals. However, due to the limited amount of data and significant variations in facial appearances among the individuals, achieving complete and accurate recognition of all three individuals might not be possible.


## Sharing
* The resizing process might result in distortion due to incorrect proportions between the original and resized images. In the future, it might be beneficial to convert all images into squares before scaling them, which could potentially yield better results.

