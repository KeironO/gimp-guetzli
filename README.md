# gimp-guetzli

GIMP plugin to enable exporting via Google's Perceptual JPEG encoder

## Installation

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
5. Drag the slider to whatever compression quality you want.
6. ???
7. PROFIT

## License

Code released under [the MIT license](https://github.com/KeironO/gimp-guetzli/blob/master/LICENSE).
