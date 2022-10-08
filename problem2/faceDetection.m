% read the image
R = imread('friends.jpg');

A = double(R);
% get the R,G,B channels of the image
Ar = A(:,:,1);
Ag = A(:,:,2);
Ab = A(:,:,3);
% normalization
Arc = Ar./(Ar+Ag+Ab+1e-10); %1e-10 to avoid 0/0
Agc = Ag./(Ar+Ag+Ab+1e-10);
Abc = Ab./(Ar+Ag+Ab+1e-10);
% Decision function
idx1 = double(Agc>=(-6.70*Arc+2.99));
idx2 = double(Agc>=(-1.31*Arc+0.84));
% create mask
mask = idx1.*idx2;

% apply mask to image to show skin regions
B = zeros(size(A));
B(:,:,1) = mask.*Ar;
B(:,:,2) = mask.*Ag;
B(:,:,3) = mask.*Ab;
B = uint8(B);
% display outputs
figure ('Name','Segmented Skin - RGB'); imshow(B);
figure('Name','Mask - RGB'); imshow (mask);
