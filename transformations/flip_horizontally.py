import sys
from PIL import Image


def apply_filter():
    img_input = Image.open(sys.argv[1])
    img_output = img_input.transpose(Image.FLIP_LEFT_RIGHT)
    img_output.save(sys.argv[2])


if __name__ == '__main__':
    apply_filter()