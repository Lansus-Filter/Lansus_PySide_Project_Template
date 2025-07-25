# -*- coding: utf-8 -*-

from typing import Iterable

from PySide6.QtCore import (
    QByteArray,
    QEasingCurve,
    QParallelAnimationGroup,
    QPropertyAnimation,
)
from PySide6.QtWidgets import QWidget


def create_width_animation(widget: QWidget, target_width: int, duration=500):
    """在指定的持续时间内，将侧边面板控件的宽度动画化到目标宽度。

    Args:
        widget(QWidget): 要动画化的QWidget对象。
        target_width(int): 动画化到的目标宽度，以像素为单位。
        duration(int): 动画持续时间，以毫秒为单位，默认值500

    Returns:
        返回配置好的动画对象(QPropertyAnimation)

    """
    animation = QPropertyAnimation(widget, QByteArray(b"minimumWidth"))
    animation.setDuration(duration)
    animation.setStartValue(widget.width())
    animation.setEndValue(target_width)
    animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
    return animation


def create_opacity_animation(widget: QWidget, target_start, target_end, duration=2000):
    """在指定的持续时间内，将侧边面板控件的宽度动画化到目标宽度。

    Args:

        widget(QWidget): 要动画化的QWidget对象。
        target_start(int): 动画的起始透明度值。0 表示完全透明，1 表示完全不透明。
        target_end(int): 动画的结束透明度值。取值范围同上。
        duration(int): 动画持续时间，以毫秒为单位，默认值500

    Returns:
        返回配置好的动画对象(QPropertyAnimation)

    """
    animation = QPropertyAnimation(widget, QByteArray(b"windowOpacity"))
    animation.setDuration(duration)
    animation.setStartValue(target_start)
    animation.setEndValue(target_end)
    animation.setEasingCurve(QEasingCurve.Type.InOutQuad)
    return animation


def create_animation_group(animations: Iterable):
    """创建动画组
    Args:
        animations(Iterable): 动画组成员

    Returns:
        动画组对象(QParallelAnimationGroup)

    """
    animation_group = QParallelAnimationGroup()
    for anim in animations:
        animation_group.addAnimation(anim)
    return animation_group
