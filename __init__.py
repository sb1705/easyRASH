from flask import Flask, render_template
import json

app = Flask(__name__)

from easyRASH import views

