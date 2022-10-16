"""Generate a WIDTH x HEIGHT sequence of 1-bit-per-pixel images, from black to white,
passing through all possible apparent shades of grey (ordered dithering). Source:
https://bisqwit.iki.fi/story/howto/dither/jy/
"""

import math
import os


WIDTH = 1
HEIGHT = 128

m_ = math.log2(WIDTH)
l_ = math.log2(HEIGHT)
m = int(m_)
l = int(l_)
if m_ != m or l_ != l:
    raise RuntimeError("WIDTH or HEIGHT aren't powers of 2")

thresh = []
for y in range(HEIGHT):
    t = []
    for x in range(WIDTH):
        v = 0
        offset = 0
        xmask = m
        ymask = l
        if m == 0 or (m > l and l != 0):
            xc = x ^ ((y << m) >> l)
            yc = y
            bit = 0
            while bit < m + l:
                ymask -= 1
                v |= ((yc >> ymask) & 1) << bit
                bit += 1
                offset += m
                while offset >= l:
                    xmask -= 1
                    v |= ((xc >> xmask) & 1) << bit
                    bit += 1
                    offset -= l
        else:
            xc = x
            yc = y ^ ((x << l) >> m)
            bit = 0
            while bit < m + l:
                xmask -= 1
                v |= ((xc >> xmask) & 1) << bit
                bit += 1
                offset += l
                while offset >= m:
                    ymask -= 1
                    v |= ((yc >> ymask) & 1) << bit
                    bit += 1
                    offset -= m
        t.append(v)
    thresh.append(t)

total = WIDTH * HEIGHT + 1
pad = len(str(total))
for i in range(total):
    with open('{}_{:0{}}.pbm'.format(os.path.splitext(__file__)[0], i, pad), 'w') as f:
        f.write('P1\n{} {}\n'.format(WIDTH, HEIGHT))
        for t in thresh:
            f.write(''.join(str(int(x >= i)) for x in t) + '\n')
