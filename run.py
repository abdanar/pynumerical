import numpy as np

from pynumerical import trapezoidal

print(trapezoidal("np.sin(x)", 10, [0, 4], True))
