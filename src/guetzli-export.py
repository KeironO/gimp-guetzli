from gimpfu import *
import os


def do_export(image, drawable, filename, raw_filename,quality, smoothing, ringing_reduction):
    gimp.progress_init("Exporting %s" % raw_filename)



def register_save():
    gimp.register_save_handler("guetzli-save", "jpeg", "jpg")

register (
    proc_name="save-guetzli",
    blurb="Export via Google's Perceptual JPEG encoder",
    help="Export via Google's Perceptual JPEG encoder",
    date="2019",
    author="Keiron O'Shea"
)


main()

