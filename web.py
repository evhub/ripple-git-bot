#!/usr/bin/python

# Imported Modules:

from __future__ import print_function
import os
from flask import Flask
from gitbot import main

app = Flask(__name__)

@app.route("/")
def web(*args, **kwargs):
    print("Initializing...")
    out = main(*args, **kwargs)
    print("Complete.")
    return out
