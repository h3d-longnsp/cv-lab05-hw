### Study functions note:
- **`imnoise`**:

  - **`J = imnoise(I, 'gaussian')`** adds zero-mean, Gaussian white noise with variance of 0.01 to grayscale image **`I`**. 
 
  - **`J = imnoise(I, 'gaussian', m)`** adds Gaussian white noise with mean **`m`** and variance of 0.01. 
 
  - **`J = imnoise(I, 'gaussian', m, var_gauss)`** adds Gaussian white noise with mean **`m`** and variance **`var_gauss`**. 
 
  - **`J = imnoise(I, 'localvar', var_local)`** adds zero-mean, Gaussian white noise of local variance **`var_local`**. 
 
  - **`J = imnoise(I, 'localvar', intensity_map, var_local)`** adds zero-mean, Gaussian white noise. The local variance of the noise **`var_local`** is a function of the image intensity values in **`I`**. The mapping of image intensity value to noise variance is specified by the vector **`intensity_map`**. 
 
  - **`J = imnoise(I, 'poisson')`** generates Poisson noise from the data instead of adding artificial noise to the data.

  - **`J = imnoise(I, 'salt & pepper')`** adds salt and pepper noise, with default noise density 0.05. This affects approximately 5% of pixels. 

  - **`J = imnoise(I, 'salt & pepper', d)`** adds salt and pepper noise, where **`d`** is the noise density. This affects approximately **`d*numel(I)`** pixels. 

  - **`J = imnoise(I, 'speckle')`** adds multiplicative noise using the equation **`J = I+n*I`**, where **`n`** is uniformly distributed random noise with mean 0 and variance 0.05. 

  - **`J = imnoise(I, 'speckle', var_speckle)`** adds multiplicative noise with variance **`var_speckle`**.

- **`medfilt2`**:
  - **`J = medfilt2(I)`** performs median filtering of the image **`I`** in two dimensions. Each output pixel contains the median value in a 3-by-3 neighborhood around the corresponding pixel in the input image.

- **`conv2`**:
  - **`C = conv2(A,B)`** returns the two-dimensional convolution of matrices A and B.

- **`filter2`**:
  - **`Y = filter2(H,X)`** applies a finite impulse response filter to a matrix of data **`X`** according to coefficients in a matrix **`H`**.

- **`fspecial`**:
  - **`h = fspecial(type)`** creates a two-dimensional filter **`h`** of the specified type. Some of the filter types have optional additional parameters, shown in the following syntaxes. **`fspecial`** returns **`h`** as a correlation kernel, which is the appropriate form to use with **`imfilter`**.
- **`imfilter`**:
  - **`B = imfilter(A,h)`** filters the multidimensional array **`A`** with the multidimensional filter kernel **`h`** and returns the result in **`B`**.
- **`edge`**:
  - **`E = edge(tree,X,Y)`** returns the classification edge for **`tree`** with data **`X`** and classification **`Y`**.