## Persephone
>Application to generate a visual representation of a hash/checksum

Persephone makes use of the [Hades](https://github.com/thisisjustinm/hades) hashing algorithm to generate a unique image, based on the input supplied. If the input supplied is
a hex string, it will display the hex string as an image, otherwise, the hash is calculated. i.e If you enter anything except the hexadecimal characters ```0123456789abcdef```, the application will return a 128-bit hash generated using hades.

## How it works
The application visually represents hexadecimal code as used within hashes in the form of stacked square blocks. Each single vertical line represents a number from 0 to 255, 
i.e. 00 to ff. A completely white vertical line of blocks would represent ```00```, while a completely black line of blocks would represent ```ff```.

The hash value for the input **```persephone-and-hades```** is ```449637206349395ffdc51e98bbc8c05a``` and the associated image is : 

![Image for the input persephone-and-hades](https://persephone-vmh.herokuapp.com/api/persephone-and-hades)

The first column visually represents the hexadecimal number 44, or decimal 68. The white squares denote 0 and black squares denote 1. The square at the bottom denotes 1 and 
the one at the top denotes 128. Here, the black squares are at 64 and 4, which sums upto decimal 68.

## Extra
The application  can be accessed here at [persephone-vmh](https://persephone-vmh.herokuapp.com/).  **No copyrights**, use as you wish. Do let me know if you have an interesting use.
Persephone is named after the goddess queen of the underworld, wife of the god Hades.

