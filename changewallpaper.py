import os
import sys
import time
import random

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gio, Gtk, Notify

import schedule

def set_gsetting(schema, key, value):
    gsettings = Gio.Settings.new(schema)
    gsettings.set_string(key, value)
    gsettings.apply()

def get_image_path():
    path = os.path.join(os.path.abspath(os.getcwd()), "images")
    return path

def get_random_image():
    image_list = os.listdir(get_image_path())
    rand_num = random.randint(0, len(image_list)-1)
    image = os.path.join(get_image_path(), image_list[rand_num])
    return image 

def set_random_image():
    try:
        set_gsetting('org.gnome.desktop.background', 'picture-uri', get_random_image())
    except:
        set_gsetting('org.cinnamon.desktop.background', 'picture-uri', get_random_image())

schedule.every(2).minutes.do(set_random_image)

while True:
    schedule.run_pending()