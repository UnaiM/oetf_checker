[OETF Checker]
==============

**[Opto-Electrical Transfer Fuction] checker for video cameras**

Please go to [unaim.github.io/oetf_checker] to use it— further instructions are available there.


Technical questions
-------------------

### Why horizontal stripes instead of a 2D dithering pattern?

Because displays are more prone to be horizontally soft— there’s a higher chance of non-white pixels when using vertically-changing patterns.

### Why stop at alternating stripes instead of filling up all pixels with white?

Because some displays might apply a “sharpness” filter whereby flat images are duller than very contrasty patterns, so we stop filling up the screen at the last possible pattern without two consecutive white stripes just in case.


[OETF Checker]: https://unaim.github.io/oetf_checker
[Opto-Electrical Transfer Fuction]: https://en.wikipedia.org/wiki/Transfer_functions_in_imaging
[unaim.github.io/oetf_checker]: https://unaim.github.io/oetf_checker
