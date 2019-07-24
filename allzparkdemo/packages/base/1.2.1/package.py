# -*- coding: utf-8 -*-

name = 'base'

version = '1.2.1'

requires = [
    'ftrack-1',
    'gitlab-1'
]

def commands():
    global env
    global this
    global system
    global expandvars
    
    # Base handles all differences between OSes
    # No reference to `system.platform` is made elsewhere
    if system.platform == "windows":
        this.projects_path = r"\\server\nas\projects"
    else:
        this.projects_path = "/mnt/projects"
    
    for key, value in this._environ.items():
        if isinstance(value, (tuple, list)):
    
            # `expandvars` is called, even though it currently
            # isn't necessary, so as to enable edits to the above
            # `_environ` that reference system environment variables,
            # without changing the logic of the below.
            [env[key].append(expandvars(v)) for v in value]
        else:
            env[key] = expandvars(value)

with scope('config') as config:
    config.release_packages_path = 'C:\\Users\\manima\\Dropbox\\dev\\anima\\github\\mottosso\\rez-for-projects\\packages\\ext'

timestamp = 1563997382

_environ = \
    {'GITLAB_URI': 'https://gitlab.mycompany.co.jp',
     'PROJECTS_PATH': '{this.projects_path}'}

format_version = 2
