#!/usr/bin/env python

from gimpfu import *
import os
from tempfile import NamedTemporaryFile as ntf

try:
    guetzli = os.environ["GUETZLI"]
except KeyError:
    gimp.message("Unable to find GUETZLI in your environment path, have you set it up correctly?")


def create_tmpfile_fp():
    tmpfile = ntf(suffix=".png")
    tmpfile_fp = tmpfile.name
    tmpfile.close()
    return tmpfile_fp
 

def do_export(image, drawable, filename, raw_filename, quality):

    gimp.progress_init("Exporting %s" % raw_filename)

    args = [guetzli]

    args.append("--quality %" % str(quality))


def register_save():
    gimp.register_save_handler("guetzli-save", "jpeg", "jpg", "")

register (
    proc_name="save-guetzli",
    blurb="Export via Google's Perceptual JPEG encoder",
    help="Export via Google's Perceptual JPEG encoder",
    author="Keiron O'Shea",
    copyright="MIT",
    date="2019",
    label="<Save>/JPEG (Guetzli)",
    imagetypes="RGB*, GRAY*",
    params=[
        (PF_SLIDER, "quality", "Quality", 90, (80, 100, 1))    
    ],
    results=[],
    function=do_export,
    on_query=register_save
)


main()

