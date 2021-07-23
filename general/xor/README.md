##  XOR

#### lemur xor
1. Using python
For this read both images assign color values and xor each pixel of both images in python and might need to recolor the result image to get the flag 
2.  Using Imagemagick cli
    ```bash
    convert flag.png lemur.png -fx "(((255*u)&(255*(1-v)))|((255*(1-u))&(255*v)))/255" result.png
    #the u and v is first and second image
    ```
    im not 100% sure how this works but checkout more about the '-fx' operator here https://imagemagick.org/script/fx.php

