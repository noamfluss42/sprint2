import numpy as np
import cv2
import create_mask


def main():
    # Load an color image in grayscale
    img1 = cv2.imread('img1.png')
    img2 = cv2.imread('img2.png')
