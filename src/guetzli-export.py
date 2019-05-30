#!/usr/bin/env python


from gimpfu import *
import os

print(os.environ)

def do_export(image, drawable, filename, raw_filename,quality, smoothing, ringing_reduction):
    gimp.progress_init("Exporting %s" % raw_filename)



def register_save():
    gimp.register_save_handler("guetzli-save", "jpeg", "jpg")

register (
    "save-guetzli",
    "Export via Google's Perceptual JPEG encoder",
    "Export via Google's Perceptual JPEG encoder",
    "Keiron O'Shea",
    "Keiron O'Shea",
    "2019"
)


main()

