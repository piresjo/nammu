'''
Copyright 2015 - 2017 University College London.

This file is part of Nammu.

Nammu is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Nammu is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Nammu.  If not, see <http://www.gnu.org/licenses/>.
'''

from ..view.EditSettingsView import EditSettingsView
from ..utils import save_yaml_config


class EditSettingsController:
    def __init__(self, maincontroller):
        self.controller = maincontroller
        self.config = self.controller.config
        self.load_config()
        self.view = EditSettingsView(self, self.working_dir, self.servers,
                                     self.keystrokes, self.languages,
                                     self.projects)
        self.view.display()

    def load_config(self):
        '''
        The user's config file should containg all necessary information for
        this settings editor.
        '''
        config_keywords = ['working_dir', 'servers', 'keystrokes',
                           'languages', 'projects']
        for keyword in config_keywords:
            try:
                setattr(self, keyword, self.config[keyword])
            except KeyError:
                self.controller.logger.error('%s missing on settings file.',
                                             keyword)
                self.view.display_error(keyword)

    def update_config(self, working_dir, server, keystrokes=None,
                      languages=None, projects=None):
        '''
        Update the settings file with the user input.
        '''
        # TODO: Validate new values introduced by user.
        # TODO: As of v0.6, only working_dir and servers are editable from the
        #       settings window. The other tabs for keystrokes, languages and
        #       projects will be added later.
        self.config['working_dir']['default'] = working_dir
        self.config['servers']['default'] = server
        self.controller.logger.debug("Settings updated.")
        save_yaml_config(self.config)