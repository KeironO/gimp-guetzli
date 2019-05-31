# gimp-guetzli

GIMP plugin to enable exporting via Google's Perceptual JPEG encoder.

Taken from the [Googe Guetzli GitHub Page](https://github.com/google/guetzli):

> Guetzli is a JPEG encoder that aims for excellent compression density at high visual quality. Guetzli-generated images are typically 20-30% smaller than images of equivalent quality generated by libjpeg. Guetzli generates only sequential (nonprogressive) JPEGs due to faster decompression speeds they offer.

## Example

Uncompressed 137.3kB:

![Uncompressed Image](https://github.com/KeironO/gimp-guetzli/raw/master/examples/uncompressed.jpg)

Compressed 19.4kB:

![Compressed Image](https://github.com/KeironO/gimp-guetzli/raw/master/examples/compressed.jpeg)


## Installation

First of all, install ```gimp-python``` and ```libpng``` using the following command:

```
sudo dnf/apt install libpng-devel gimp-python
``` 

This plugin requires that you set up Guetzli. The easiest way to do this is to download the newest release from the [following page](https://github.com/google/guetzli/releases) and unzip the binary to your preferred path.

Once you have done that, ensure that the binary is executable by running the following in your terminal:

```bash
chmod +x /path/to/binary/guetzli
```

Now append the path to the Guetzli binary to ```~/.profile```.

```
export GUETZLI="/path/to/binary/guetzli"
``` 

Once complete, clone this project and copy over the plugin to the default local plugins directory and make it executable.

```bash
git clone https://github.com/KeironO/gimp-guetzli/
cp gimp-guetzli/src/guetzli-export.py ~/.config/GIMP/2.10/plug-ins
chmod +x ~/.config/GIMP/2.10/plug-ins/guetzli-export.py
```

## Usage

0. Open the image you want to export in GIMP.
1. File > Export As
2. Select File Type (By Extension) > Google Guetzli (JPEG)
3. Change the filename to whatever you want.
4. Export
5. Drag the slider to whatever compression quality you want and click export.
6. ???
7. PROFIT

## Important Notes

> Note: Guetzli uses a large amount of memory. You should provide 300MB of memory per 1MPix of the input image.

And also:

> Note: Guetzli uses a significant amount of CPU time. You should count on using about 1 minute of CPU per 1 MPix of input image.

Oh, and another thing:

> Note: Guetzli assumes that input is in sRGB profile with a gamma of 2.2. Guetzli will ignore any color-profile metadata in the image.


## License

Code released under [the MIT license](https://github.com/KeironO/gimp-guetzli/blob/master/LICENSE).
