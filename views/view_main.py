# -*- coding: utf-8 -*-


from PySide6.QtCore import QObject, Qt

from views import LoginWindow, MainWindow
from views.ui_components import create_animation_group, create_opacity_animation


class ViewMain(QObject):
    login_window: LoginWindow
    main_window: MainWindow

    def __init__(self, animate_on_startup):
        super().__init__()
        self.setup_ui(animate_on_startup)

    def setup_ui(self, animate_on_startup):
        self.main_window = MainWindow()

        # 判断是否以动画的形式启动
        if animate_on_startup:
            self.login_window = LoginWindow()
            # 设置窗口不显示任务栏
            self.login_window.setWindowFlag(Qt.WindowType.Tool)
            # 连接Signal信号，login动画加载完成再运行
            self.login_window.login_successful.connect(self.start_animation)
            #
            self.login_window.show()
        else:
            self.main_window.show()
            # 主窗口淡入，看个人喜好
            # self.fade_in = create_opacity_animation(self.main_window, 0, 1, 2500)
            # self.fade_in.start()

    def start_animation(self):
        # 确保第二个窗口的透明度初始为0
        self.main_window.setWindowOpacity(0)
        self.main_window.show()

        # 创建淡出淡入动画
        fade_out = create_opacity_animation(self.login_window, 1, 0, 1800)
        fade_in = create_opacity_animation(self.main_window, 0, 1, 2500)
        fade_out.finished.connect(self.login_window.close)  # 淡出完成后隐藏窗口

        # 使用并行动画组合，同时执行淡入和淡出
        self.animation_group = create_animation_group((fade_out, fade_in))
        self.animation_group.start()
