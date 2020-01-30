# coding: utf-8

import os
from web import create_app

app = create_app(os.path.abspath('conf/dev.config.py'))

if __name__ == "__main__":
    app.run()
