# -*- coding: utf-8 -*-

# Copyright 2019 TONAL SYSTEM

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import NXSettingsConfig 
from flask import Flask, Blueprint
from flask import redirect, url_for
# from flask_appbuilder import AppBuilder, SQLA

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    # return redirect(url_for('Airflow.index'))
    return 'Hello, World!'

class NXWebserver:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(routes)
    
    def run(self):

        try:
            logging.info('webserver starting')
            self.app.run()
        except Exception as e:
            logging.critical(e)
        
