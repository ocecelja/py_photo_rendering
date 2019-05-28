#!/usr/bin/env python

import os
import click
import shutil
import glob
import sys
import requests
from PIL import Image, ImageFilter

# FILENAME_ORIGINAL_PHOTOS = 'original'
# FILENAME_FULL_SIZE_PHOTOS = 'full_size'
# FILENAME_SMALL_SIZE_PHOTOS = 'small_size'
folder_names = {'FILENAME_ORIGINAL_PHOTOS': 'original', 'FILENAME_FULL_SIZE_PHOTOS': 'full_size', 'FILENAME_SMALL_SIZE_PHOTOS': 'small_size'}

# Set your photo size for FULL and SMALL size
full_size = 1200, 800
small_size = 200, 150

def check_original_folders():
    if not (os.path.exists(folder_names['FILENAME_ORIGINAL_PHOTOS'])):
        print("Missing original directory %s " % folder_names['FILENAME_ORIGINAL_PHOTOS'])
        exit()

    if os.path.exists(folder_names['FILENAME_SMALL_SIZE_PHOTOS']):
        try:
            shutil.rmtree(folder_names['FILENAME_SMALL_SIZE_PHOTOS'])
        except OSError:
            print("Removing of the directory %s failed" % folder_names['FILENAME_SMALL_SIZE_PHOTOS'])
            exit()
        else:
            print("Successfully deleted the directory %s " % folder_names['FILENAME_SMALL_SIZE_PHOTOS'])
        try:
            os.mkdir(folder_names['FILENAME_SMALL_SIZE_PHOTOS'])
        except OSError:
            print("Creation of the directory %s failed" % folder_names['FILENAME_SMALL_SIZE_PHOTOS'])
            exit()
        else:
            print("Successfully created the directory %s " % folder_names['FILENAME_SMALL_SIZE_PHOTOS'])
    else:
        try:
            os.mkdir(folder_names['FILENAME_SMALL_SIZE_PHOTOS'])
        except OSError:
            print("Creation of the directory %s failed" % folder_names['FILENAME_SMALL_SIZE_PHOTOS'])
            exit()
        else:
            print("Successfully created the directory %s " % folder_names['FILENAME_SMALL_SIZE_PHOTOS'])

    if os.path.exists(folder_names['FILENAME_FULL_SIZE_PHOTOS']):
        try:
            shutil.rmtree(folder_names['FILENAME_FULL_SIZE_PHOTOS'])
        except OSError:
            print("Removing of the directory %s failed" % folder_names['FILENAME_FULL_SIZE_PHOTOS'])
            exit()
        else:
            print("Successfully deleted the directory %s " % folder_names['FILENAME_FULL_SIZE_PHOTOS'])
        try:
            os.mkdir(folder_names['FILENAME_FULL_SIZE_PHOTOS'])
        except OSError:
            print("Creation of the directory %s failed" % folder_names['FILENAME_FULL_SIZE_PHOTOS'])
            exit()
        else:
            print("Successfully created the directory %s " % folder_names['FILENAME_FULL_SIZE_PHOTOS'])
    else:
        try:
            os.mkdir(folder_names['FILENAME_FULL_SIZE_PHOTOS'])
        except OSError:
            print("Creation of the directory %s failed" % folder_names['FILENAME_FULL_SIZE_PHOTOS'])
            exit()
        else:
            print("Successfully created the directory %s " % folder_names['FILENAME_FULL_SIZE_PHOTOS'])

def generate():
    for filename in os.listdir(folder_names['FILENAME_ORIGINAL_PHOTOS']):
        # ADD whatever format you like supported by PILLOW
        if filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            photo_name = filename.split('.')
            # print(photo_name)
            im = Image.open(folder_names['FILENAME_ORIGINAL_PHOTOS'] + "/" + filename)
            im.thumbnail(full_size)
            im.save(folder_names['FILENAME_FULL_SIZE_PHOTOS'] + '/' + str(photo_name[0]) + "_full." + str(photo_name[len(photo_name) - 1]))
            im.thumbnail(small_size)
            im.save(folder_names['FILENAME_SMALL_SIZE_PHOTOS'] + '/' + str(photo_name[0]) + "_small." + str(photo_name[len(photo_name) - 1]))

@click.command()
@click.option("-n", "--none", help='Use predefined full_size and small_size folder', is_flag=True)
@click.option("-o", "--original", help='Original sized photos folder name inside " "', is_flag=False)
@click.option("-f", "--full", help='Full sized photos folder name inside " "', is_flag=False)
@click.option("-s", "--small", help='Small sized photos folder name inside " "', is_flag=False)

def render(none, original, full, small):
    if not (none or full or small):
                print("No option set!")
                sys.exit(0)
    if none:
        check_original_folders()
        generate()
    elif original:
        if full:
            if small:
                folder_names['FILENAME_ORIGINAL_PHOTOS'] = str(original)
                folder_names['FILENAME_FULL_SIZE_PHOTOS'] = str(full)
                folder_names['FILENAME_SMALL_SIZE_PHOTOS'] = str(small)
                check_original_folders()
                generate()
            else:
                print("Missing small size photos folder name!")
        else:
                print("Missing full size photos folder name!")
    else:
        print("Missing original size photos folder name!")

@click.group()
def main():
    pass

main.add_command(render)

if __name__ == "__main__":
    main()
