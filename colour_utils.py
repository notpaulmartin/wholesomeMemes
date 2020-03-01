'''
File:          colour_utils.py
Project:       htb2020-memebot
File Created:  Sunday, 1st March 2020 1:21:18 am
Author(s):     Paul Martin

Last Modified: Sunday, 1st March 2020 2:20:34 am
Modified By:   Paul Martin
'''

from __future__ import print_function
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

IMG_DIR = 'memes'
NUM_CLUSTERS = 5

def get_main_colour(filename):
    print('reading image')
    im = Image.open(f'{IMG_DIR}/{filename}')
    im = im.resize((100, 100))      # optional, to reduce time
    ar = np.asarray(im)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    print('finding clusters')
    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
    print('cluster centres:\n', codes)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent
    peak = codes[index_max] # colour in rgb
    colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii') # hex colour
    
    return tuple(map(int, peak))

def square(file, background_colour=(255,255,255)):
    old_im = Image.open(f'{IMG_DIR}/{file}')
    old_size = old_im.size

    new_size = (max(old_size), max(old_size))
    new_im = Image.new("RGB", new_size, background_colour)   ## luckily, this is already black!

    placement_x = (new_size[0]-old_size[0])/2
    placement_y = (new_size[1]-old_size[1])/2

    new_im.paste(
        old_im,
        (
            int(placement_x),
            int(placement_y)
        )
    )

    return new_im
    