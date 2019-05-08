#!/usr/bin/env python
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
import argparse
from NXWebserver.NXWebserver import NXWebserver

class Application:
    def __init__(self, name):
        self.name = name
        self.args = None
    
    def get_arguments(self):
        commandParser = CommandParser()
        self.args = commandParser.parse()
        return(self.args.command, self.args.target)

    def run(self, args):
        print(f'Command: {args!r}')
        if self.args.target == 'webserver':
            # logging.info('webserver')
            webserver = NXWebserver()
            webserver.run() 
            
        else:
            pass

class CommandParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('command', help='Command to execute (start, stop)')
        self.parser.add_argument('target', help='Target for the command (webserver, dataserver, appserver)')
        self.parser.add_argument("--verbosity", help="increase output verbosity")
        # logging.info(self.parser)
    
    def parse(self):
        args = self.parser.parse_args()
        return args
        

if __name__ == '__main__':
    app = Application('NXHello')
    args = app.get_arguments()
    app.run(args)
