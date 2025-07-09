# -*- coding: utf-8 -*-

from views import ViewMain


class ControllerMain:
    def __init__(self, animate_on_startup=True):
        self.view = ViewMain(animate_on_startup)
