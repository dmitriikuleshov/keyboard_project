from PyQt5.Qt import *


class AnimatedButton(QPushButton):
    def __init__(self, *args, **kwargs):
        QPushButton.__init__(self, *args, **kwargs)

        # GEOMETRY
        self.anim = QPropertyAnimation(self, b'geometry')
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.OutElastic)

        # COLORIZING
        self.colorEffect = QGraphicsColorizeEffect(self)
        self.colorEffect.setStrength(0)
        self.colorEffect.setColor(QColor(20, 20, 20))
        self.setGraphicsEffect(self.colorEffect)
        self.colorAnim = QPropertyAnimation(self.colorEffect, b'strength')
        self.colorAnim.setDuration(200)

        '''
        # COLOR
        self.colorEffect1 = QGraphicsColorizeEffect(self)
        #self.colorEffect1.setColor(QColor(0, 255, 0, 255))
        self.setGraphicsEffect(self.colorEffect1)
        self.colorAnim1 = QPropertyAnimation(self.colorEffect1, b'color')
        self.colorAnim1.setDuration(100)
        '''

    def color_clicked(self):
        # COLORIZING
        self.colorAnim.setDirection(self.colorAnim.Forward)
        if self.colorAnim.state() == self.colorAnim.State.Stopped:
            self.colorAnim.setStartValue(0)
            self.colorAnim.setKeyValueAt(0.1, 1)
            self.colorAnim.setKeyValueAt(0.9, 1)
            self.colorAnim.setEndValue(0)
            self.colorAnim.start()

        self.anim.setDirection(self.anim.Forward)
        if self.anim.state() == self.anim.State.Stopped:
            rect = self.geometry()
            self.anim.setStartValue(rect)
            self.anim.setEndValue(rect)
            rect += QMargins(4, 4, 4, 4)
            self.anim.setKeyValueAt(0.5, rect)
            self.anim.start()
