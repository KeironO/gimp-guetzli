#!/usr/bin/env python

from gimpfu import *
import os
from tempfile import NamedTemporaryFile as ntf
import subprocess

try:
    guetzli = os.environ['GUETZLI']
except KeyError:
    gimp.message('Unable to find GUETZLI in your environment path, have you set it up correctly?')


def create_tmpfile_fp():
    tmpfile = ntf(suffix='.png')
    tmpfile_fp = tmpfile.name
    tmpfile.close()
    return tmpfile_fp, os.path.basename(tmpfile_fp)


def do_export(image, drawable, fp, raw_filename, _, quality):
    
    image_copy = pdb.gimp_image_duplicate(image)

    gimp.progress_init('Exporting %s' % raw_filename)

    tmpfile_fp, tmpfile_name = create_tmpfile_fp()
    
    pdb.file_png_save(image_copy, image_copy.flatten(), tmpfile_fp, tmpfile_name,  0, 0, 0, 0, 0, 0, 0)

    args = [guetzli]
    args.append('--quality')
    args.append(str(int(quality)))

    args.append(tmpfile_fp)
    args.append(fp)

    gimp.progress_init('Exporting: %s' % (fp))

    output = subprocess.check_output(args)

    pdb.gimp_progress_end()
    pdb.gimp_displays_flush()

    os.remove(tmpfile_fp)


def register_save():
    gimp.register_save_handler('file-google-guetzli-save', 'jpeg,jpg', '')

register (
    proc_name='file-google-guetzli-save',
    blurb='Export via Googles Perceptual JPEG encoder',
    help='Export via Googles Perceptual JPEG encoder',
    author='Keiron OShea',
    copyright='MIT',
    date='2019',
    label='<Save>/Google Guetzli (JPEG)',
    imagetypes='RGB*, GRAY*',
    params=[
        (PF_STRING, 'none', 'None', None),
        (PF_SLIDER, 'quality', 'Compression Quality', 90, (0, 100, 1))
    ],
    results=[],
    function=do_export,
    on_query=register_save
)


main()
