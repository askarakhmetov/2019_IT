import matplotlib.pyplot as plt
import numpy as np

def gauss_kernel(size = 5, sigma = 3):
    center = (int)(size / 2)
    kernel = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            diff = np.sqrt((i - center) ** 2 + (j - center) ** 2)
            kernel[i, j] = np.exp(-(diff ** 2) / (2 * sigma ** 2))
    return kernel / np.sum(kernel)


def filter(img, window_size=3):
    img2 = np.zeros_like(img)
    kernel = gauss_kernel(window_size)
    p = window_size//2
    for k in range(img.shape[2]): # foreach color channel
        for i in range(p, img.shape[0]-p): # foreach row
            for j in range(p, img.shape[1]-p): # foreach column
                window = img[i-p:i+p+1, j-p:j+p+1, k]
                img2[i,j,k] = (kernel*window).sum()
    return img2

def main():
    img = plt.imread("H:\\git\\2019_IT\\Snail.png")[:, :, :3] #file
    img2 = filter(img)

    fig, axs = plt.subplots(1,2)
    axs[0].imshow(img)
    axs[1].imshow(img2)
    plt.show()


if __name__ == "__main__":
    main()