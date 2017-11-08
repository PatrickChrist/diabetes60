"""
Package of helpers for reading Food3D data. The data itself is stored
in binary form using compressed numpy arrays. Appropriate files for loading
are provided below. Please note that we already did the registration on-the-fly
before dumping the frames; accelerometer data has not been captured as
we did not have access to the sensor via our API at the point of recording.

--------------------------------------------------------------------

The MIT License (MIT)

Copyright (c) 2016 Patrick Christ, Sebastian Schlecht

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import os
import numpy as np

np.random.seed(42)

def load(filename):
    """
    Load a record file from disk into memory
    """
    if not os.path.isfile(filename):
        raise ValueError("File %s does not exist." % filename)
    try:
        if filename.endswith("_depth.npz"):
            return np.load(filename)["arr_0"].astype(np.float32)
        elif filename.endswith("_bgr.npz"):
            array = np.load(filename)["arr_0"]

            # Arrays are BGRA, we ommit alpha values
            array = array[:,:,0:3]

            # We barrel roll to RGB and transpose channels to first axis
            return array[:,:,::-1].transpose((2, 0, 1)).astype(np.uint8)
        else:
            raise ValueError("File doesn't seem to be food3d data.")
    except Exception as e:
        print "Could not read file: %s with error: %s" % (filename, str(e))


def transform_depth(depth):
    """
    Transform the depth into the space of meters and clean invalid values
    """
    depth[depth == np.inf] = 0
    depth[depth == np.nan] = 0

    # Convert to meters
    return depth / 1000.
