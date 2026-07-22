class ImageProcessor:

    def crop(self, image, x, y, width, height):
        return image[y:y + height, x:x + width]