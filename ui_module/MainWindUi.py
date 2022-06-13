# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win_ui1.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)

class QLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        filePathList = e.mimeData().text()
        filePath = filePathList.split('\n')[0]  # 拖拽多文件只取第一个地址
        filePath = filePath.replace('file:///', '', 1)  # 去除文件地址前缀的特定字符
        self.setText(filePath)



class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(930, 771)
        MainWindow.setAcceptDrops(False)
        MainWindow.setStyleSheet(u"/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left"
                        "-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-rad"
                        "ius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-righ"
                        "t-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargrad"
                        "ient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-style: solid;\n"
"	"
                        "border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qli"
                        "neargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QLabel {\n"
"	color: #000000;\n"
"}\n"
"QLCDNumber {\n"
"	color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(230, 230, 230);\n"
"	border-style: solid;\n"
"	background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient(spread:pad, "
                        "x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"	color: #000000;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
" \n"
"QMenuBar::item:selected {\n"
"  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	border-bo"
                        "ttom-color: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #000000;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	color: #000000;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(223,223,223);\n"
"		background-color:rgb(226,226,226);\n"
"		border-style: solid;\n"
"		border-width: 2px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	border-style: solid;\n"
"	border-left-width:1px;\n"
"	border-right-width:0px;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlinea"
                        "rgradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"	border-style: solid;\n"
"	border-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-l"
                        "eft:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-left-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y"
                        "2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
" \n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"  	border-bottom-width:1px;\n"
"  	border-top-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
" \n"
"QChec"
                        "kBox {\n"
"	color: #000000;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
" \n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
" \n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
" \n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, "
                        "255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"}\n"
"QRadioButton {\n"
"	color: 000000;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	border-style: solid;\n"
""
                        "	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
" \n"
""
                        "QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;"
                        "\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	max-width: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1"
                        "px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;"
                        "\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-ra"
                        "dius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::le"
                        "ft-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub"
                        "-page:vertical {\n"
"   background: none;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(MainWindow)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.groupBox = QGroupBox(MainWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAcceptDrops(False)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_path_py = QLineEdit(self.groupBox)
        self.lineEdit_path_py.setObjectName(u"lineEdit_path_py")
        self.lineEdit_path_py.setAcceptDrops(True)
        self.lineEdit_path_py.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_path_py)

        self.btn_select_path_py = QPushButton(self.groupBox)
        self.btn_select_path_py.setObjectName(u"btn_select_path_py")
        self.btn_select_path_py.setAcceptDrops(False)

        self.horizontalLayout.addWidget(self.btn_select_path_py)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_path_save_dir = QLineEdit(self.groupBox)
        self.lineEdit_path_save_dir.setObjectName(u"lineEdit_path_save_dir")
        self.lineEdit_path_save_dir.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_path_save_dir)

        self.btn_select_path_save_dir = QPushButton(self.groupBox)
        self.btn_select_path_save_dir.setObjectName(u"btn_select_path_save_dir")

        self.horizontalLayout_2.addWidget(self.btn_select_path_save_dir)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lineEdit_path_temp = QLineEdit(self.groupBox)
        self.lineEdit_path_temp.setObjectName(u"lineEdit_path_temp")
        self.lineEdit_path_temp.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.lineEdit_path_temp)

        self.btn_select_path_temp = QPushButton(self.groupBox)
        self.btn_select_path_temp.setObjectName(u"btn_select_path_temp")

        self.horizontalLayout_3.addWidget(self.btn_select_path_temp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_11.addWidget(self.label_3)

        self.lineEdit_path_icon = QLineEdit(self.groupBox)
        self.lineEdit_path_icon.setObjectName(u"lineEdit_path_icon")
        self.lineEdit_path_icon.setDragEnabled(False)
        self.lineEdit_path_icon.setReadOnly(False)

        self.horizontalLayout_11.addWidget(self.lineEdit_path_icon)

        self.btn_select_path_icon = QPushButton(self.groupBox)
        self.btn_select_path_icon.setObjectName(u"btn_select_path_icon")

        self.horizontalLayout_11.addWidget(self.btn_select_path_icon)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_9.addWidget(self.groupBox)

        self.groupBox_basis_config = QGroupBox(MainWindow)
        self.groupBox_basis_config.setObjectName(u"groupBox_basis_config")
        self.groupBox_basis_config.setAlignment(Qt.AlignCenter)
        self.groupBox_basis_config.setFlat(False)
        self.groupBox_basis_config.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_basis_config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.checkBox_single_file = QCheckBox(self.groupBox_basis_config)
        self.checkBox_single_file.setObjectName(u"checkBox_single_file")

        self.horizontalLayout_17.addWidget(self.checkBox_single_file)

        self.checkBox_UPX = QCheckBox(self.groupBox_basis_config)
        self.checkBox_UPX.setObjectName(u"checkBox_UPX")

        self.horizontalLayout_17.addWidget(self.checkBox_UPX)

        self.checkBox_del_cmd = QCheckBox(self.groupBox_basis_config)
        self.checkBox_del_cmd.setObjectName(u"checkBox_del_cmd")

        self.horizontalLayout_17.addWidget(self.checkBox_del_cmd)

        self.checkBox_clear = QCheckBox(self.groupBox_basis_config)
        self.checkBox_clear.setObjectName(u"checkBox_clear")

        self.horizontalLayout_17.addWidget(self.checkBox_clear)

        self.checkBox_del_temp = QCheckBox(self.groupBox_basis_config)
        self.checkBox_del_temp.setObjectName(u"checkBox_del_temp")

        self.horizontalLayout_17.addWidget(self.checkBox_del_temp)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.groupBox_basis_config)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_path_UPX = QLineEdit(self.groupBox_basis_config)
        self.lineEdit_path_UPX.setObjectName(u"lineEdit_path_UPX")
        self.lineEdit_path_UPX.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_path_UPX)

        self.btn_select_path_UPX = QPushButton(self.groupBox_basis_config)
        self.btn_select_path_UPX.setObjectName(u"btn_select_path_UPX")

        self.horizontalLayout_4.addWidget(self.btn_select_path_UPX)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_7 = QLabel(self.groupBox_basis_config)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_6.addWidget(self.label_7)

        self.lineEdit_exe_name = QLineEdit(self.groupBox_basis_config)
        self.lineEdit_exe_name.setObjectName(u"lineEdit_exe_name")

        self.horizontalLayout_6.addWidget(self.lineEdit_exe_name)

        self.label_6 = QLabel(self.groupBox_basis_config)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_pwd = QLineEdit(self.groupBox_basis_config)
        self.lineEdit_pwd.setObjectName(u"lineEdit_pwd")

        self.horizontalLayout_6.addWidget(self.lineEdit_pwd)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.groupBox_basis_config)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_7.addWidget(self.label_8)

        self.lineEdit_path_pyinstaller = QLineEdit(self.groupBox_basis_config)
        self.lineEdit_path_pyinstaller.setObjectName(u"lineEdit_path_pyinstaller")
        self.lineEdit_path_pyinstaller.setReadOnly(False)

        self.horizontalLayout_7.addWidget(self.lineEdit_path_pyinstaller)

        self.btn_select_path_pyinstaller = QPushButton(self.groupBox_basis_config)
        self.btn_select_path_pyinstaller.setObjectName(u"btn_select_path_pyinstaller")

        self.horizontalLayout_7.addWidget(self.btn_select_path_pyinstaller)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_9.addWidget(self.groupBox_basis_config)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.groupBox_senior_config = QGroupBox(MainWindow)
        self.groupBox_senior_config.setObjectName(u"groupBox_senior_config")
        self.groupBox_senior_config.setEnabled(True)
        self.groupBox_senior_config.setAcceptDrops(False)
        self.groupBox_senior_config.setAlignment(Qt.AlignCenter)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_senior_config)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.groupBox_senior_config)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_8.addWidget(self.label_9)

        self.tableWidget_add_data_file = QTableWidget(self.tab)
        if (self.tableWidget_add_data_file.columnCount() < 2):
            self.tableWidget_add_data_file.setColumnCount(2)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget_add_data_file.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget_add_data_file.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget_add_data_file.rowCount() < 6):
            self.tableWidget_add_data_file.setRowCount(6)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_add_data_file.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_add_data_file.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_add_data_file.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_add_data_file.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_add_data_file.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_add_data_file.setVerticalHeaderItem(5, __qtablewidgetitem7)
        self.tableWidget_add_data_file.setObjectName(u"tableWidget_add_data_file")
        self.tableWidget_add_data_file.setEnabled(True)
        self.tableWidget_add_data_file.setFrameShadow(QFrame.Sunken)
        self.tableWidget_add_data_file.setLineWidth(1)
        self.tableWidget_add_data_file.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_add_data_file.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_add_data_file.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget_add_data_file.horizontalHeader().setVisible(True)
        self.tableWidget_add_data_file.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_add_data_file.horizontalHeader().setHighlightSections(True)
        self.tableWidget_add_data_file.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_add_data_file.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_add_data_file.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_add_data_file.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_add_data_file.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.tableWidget_add_data_file)

        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_7 = QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_10 = QLabel(self.tab_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.tableWidget_add_binary = QTableWidget(self.tab_5)
        if (self.tableWidget_add_binary.columnCount() < 2):
            self.tableWidget_add_binary.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.tableWidget_add_binary.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.tableWidget_add_binary.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        if (self.tableWidget_add_binary.rowCount() < 6):
            self.tableWidget_add_binary.setRowCount(6)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_add_binary.setVerticalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_add_binary.setVerticalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_add_binary.setVerticalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_add_binary.setVerticalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_add_binary.setVerticalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_add_binary.setVerticalHeaderItem(5, __qtablewidgetitem15)
        self.tableWidget_add_binary.setObjectName(u"tableWidget_add_binary")
        self.tableWidget_add_binary.setFrameShadow(QFrame.Sunken)
        self.tableWidget_add_binary.setLineWidth(1)
        self.tableWidget_add_binary.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_7.addWidget(self.tableWidget_add_binary)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_9 = QVBoxLayout(self.tab_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.tab_4)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_9.addWidget(self.label_11)

        self.textEdit_p = QTextEdit(self.tab_4)
        self.textEdit_p.setObjectName(u"textEdit_p")

        self.verticalLayout_9.addWidget(self.textEdit_p)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_3.addWidget(self.label_12)

        self.textEdit_add_module = QTextEdit(self.tab_2)
        self.textEdit_add_module.setObjectName(u"textEdit_add_module")

        self.verticalLayout_3.addWidget(self.textEdit_add_module)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_10 = QVBoxLayout(self.tab_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_10.addWidget(self.label_13)

        self.textEdit_exclude_module = QTextEdit(self.tab_3)
        self.textEdit_exclude_module.setObjectName(u"textEdit_exclude_module")

        self.verticalLayout_10.addWidget(self.textEdit_exclude_module)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_5.addWidget(self.groupBox_senior_config)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.groupBox_version_info = QGroupBox(MainWindow)
        self.groupBox_version_info.setObjectName(u"groupBox_version_info")
        self.groupBox_version_info.setEnabled(True)
        self.groupBox_version_info.setAlignment(Qt.AlignCenter)
        self.groupBox_version_info.setCheckable(True)
        self.groupBox_version_info.setChecked(False)
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_version_info)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tableWidget_version_info = QTableWidget(self.groupBox_version_info)
        if (self.tableWidget_version_info.columnCount() < 3):
            self.tableWidget_version_info.setColumnCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.tableWidget_version_info.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.tableWidget_version_info.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.tableWidget_version_info.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        if (self.tableWidget_version_info.rowCount() < 8):
            self.tableWidget_version_info.setRowCount(8)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_version_info.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_version_info.setVerticalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_version_info.setVerticalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_version_info.setVerticalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_version_info.setVerticalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_version_info.setVerticalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_version_info.setVerticalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_version_info.setVerticalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(0, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(1, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(1, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(2, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(2, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(3, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(3, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(4, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(4, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(5, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(5, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(6, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(6, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(7, 0, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_version_info.setItem(7, 2, __qtablewidgetitem42)
        self.tableWidget_version_info.setObjectName(u"tableWidget_version_info")

        self.horizontalLayout_15.addWidget(self.tableWidget_version_info)


        self.horizontalLayout_12.addWidget(self.groupBox_version_info)

        self.groupBox_log = QGroupBox(MainWindow)
        self.groupBox_log.setObjectName(u"groupBox_log")
        self.groupBox_log.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_log)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textEdit_log = QTextEdit(self.groupBox_log)
        self.textEdit_log.setObjectName(u"textEdit_log")

        self.verticalLayout_6.addWidget(self.textEdit_log)


        self.horizontalLayout_12.addWidget(self.groupBox_log)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.progressBar = QProgressBar(MainWindow)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout_5.addWidget(self.progressBar)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_help = QPushButton(MainWindow)
        self.btn_help.setObjectName(u"btn_help")

        self.horizontalLayout_10.addWidget(self.btn_help)

        self.btn_reset = QPushButton(MainWindow)
        self.btn_reset.setObjectName(u"btn_reset")

        self.horizontalLayout_10.addWidget(self.btn_reset)

        self.btn_start = QPushButton(MainWindow)
        self.btn_start.setObjectName(u"btn_start")

        self.horizontalLayout_10.addWidget(self.btn_start)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)


        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Pyinstaller打包精灵                                                             作者: 空心    QQ: 2448545222")
        self.groupBox.setTitle("项目信息")
        self.label.setText("main路径:")
        self.lineEdit_path_py.setPlaceholderText("要打包的py文件路径")
        self.btn_select_path_py.setText("选择文件")
        self.label_2.setText("保存路径:")
        self.lineEdit_path_save_dir.setPlaceholderText("exe打包到哪里, 默认在本程序的dist目录下")
        self.btn_select_path_save_dir.setText("选择目录")
        self.label_4.setText("临时路径:")
        self.lineEdit_path_temp.setPlaceholderText("打包过程产生的文件, 默认在本程序的build目录下")
        self.btn_select_path_temp.setText("选择目录")
        self.label_3.setText("图标路径:")
        self.lineEdit_path_icon.setPlaceholderText(".ico的图标文件")
        self.btn_select_path_icon.setText("选择图标")
        self.groupBox_basis_config.setTitle("基本配置")
        self.checkBox_single_file.setText("单文件")
        self.checkBox_UPX.setText("UPX压缩")
        self.checkBox_del_cmd.setText("去除命令行")
        self.checkBox_clear.setText("构前清理")
        self.checkBox_del_temp.setText("自动删除临时文件")
        self.label_5.setText("UPX路径:")
        self.lineEdit_path_UPX.setPlaceholderText("upx.exe的目录")
        self.btn_select_path_UPX.setText("选择目录")
        self.label_7.setText("exe重命名:")
        self.lineEdit_exe_name.setPlaceholderText("打包后的exe名称")
        self.label_6.setText("加密打包:")
        self.lineEdit_pwd.setPlaceholderText("最大16位密码")
        self.label_8.setText("Pyinstaller路径:")
        self.lineEdit_path_pyinstaller.setPlaceholderText("如选择'main路径'后未检测到; 请手动选择")
        self.btn_select_path_pyinstaller.setText("选择路径")
        self.groupBox_senior_config.setTitle("高级配置")
        self.label_9.setText("--add-data")
        ___qtablewidgetitem = self.tableWidget_add_data_file.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText("资源路径");
        ___qtablewidgetitem1 = self.tableWidget_add_data_file.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText("目标路径");
        ___qtablewidgetitem2 = self.tableWidget_add_data_file.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText("1");
        ___qtablewidgetitem3 = self.tableWidget_add_data_file.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText("2");
        ___qtablewidgetitem4 = self.tableWidget_add_data_file.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText("3");
        ___qtablewidgetitem5 = self.tableWidget_add_data_file.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText("4");
        ___qtablewidgetitem6 = self.tableWidget_add_data_file.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText("5");
        ___qtablewidgetitem7 = self.tableWidget_add_data_file.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText("6");
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "添加数据文件")
        self.label_10.setText("--add-binary")
        ___qtablewidgetitem8 = self.tableWidget_add_binary.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText("资源路径");
        ___qtablewidgetitem9 = self.tableWidget_add_binary.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText("目标路径");
        ___qtablewidgetitem10 = self.tableWidget_add_binary.verticalHeaderItem(0)
        ___qtablewidgetitem10.setText("1");
        ___qtablewidgetitem11 = self.tableWidget_add_binary.verticalHeaderItem(1)
        ___qtablewidgetitem11.setText("2");
        ___qtablewidgetitem12 = self.tableWidget_add_binary.verticalHeaderItem(2)
        ___qtablewidgetitem12.setText("3");
        ___qtablewidgetitem13 = self.tableWidget_add_binary.verticalHeaderItem(3)
        ___qtablewidgetitem13.setText("4");
        ___qtablewidgetitem14 = self.tableWidget_add_binary.verticalHeaderItem(4)
        ___qtablewidgetitem14.setText("5");
        ___qtablewidgetitem15 = self.tableWidget_add_binary.verticalHeaderItem(5)
        ___qtablewidgetitem15.setText("6");
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), "添加编译文件")
        self.label_11.setText("-p")
        self.textEdit_p.setPlaceholderText("多个路用英文逗号隔开")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), "添加额外的import路径")
        self.label_12.setText("--hidden-import")
        self.textEdit_add_module.setPlaceholderText("多个模块时 用英文逗号隔开; 如: os, sys, time.sleep")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "添加指定模块")
        self.label_13.setText("--exclude-module")
        self.textEdit_exclude_module.setPlaceholderText("多个模块时 用英文逗号隔开; 如: os, sys, time.sleep")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), "屏蔽指定模块")
        self.groupBox_version_info.setTitle("版本信息")
        ___qtablewidgetitem16 = self.tableWidget_version_info.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText("名称");
        ___qtablewidgetitem17 = self.tableWidget_version_info.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText("值");
        ___qtablewidgetitem18 = self.tableWidget_version_info.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText("示例");
        ___qtablewidgetitem19 = self.tableWidget_version_info.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText("1");
        ___qtablewidgetitem20 = self.tableWidget_version_info.verticalHeaderItem(1)
        ___qtablewidgetitem20.setText("2");
        ___qtablewidgetitem21 = self.tableWidget_version_info.verticalHeaderItem(2)
        ___qtablewidgetitem21.setText("3");
        ___qtablewidgetitem22 = self.tableWidget_version_info.verticalHeaderItem(3)
        ___qtablewidgetitem22.setText("4");
        ___qtablewidgetitem23 = self.tableWidget_version_info.verticalHeaderItem(4)
        ___qtablewidgetitem23.setText("5");
        ___qtablewidgetitem24 = self.tableWidget_version_info.verticalHeaderItem(5)
        ___qtablewidgetitem24.setText("6");
        ___qtablewidgetitem25 = self.tableWidget_version_info.verticalHeaderItem(6)
        ___qtablewidgetitem25.setText("7");
        ___qtablewidgetitem26 = self.tableWidget_version_info.verticalHeaderItem(7)
        ___qtablewidgetitem26.setText("8");

        __sortingEnabled = self.tableWidget_version_info.isSortingEnabled()
        self.tableWidget_version_info.setSortingEnabled(False)
        ___qtablewidgetitem27 = self.tableWidget_version_info.item(0, 0)
        ___qtablewidgetitem27.setText("公司名称");
        ___qtablewidgetitem28 = self.tableWidget_version_info.item(0, 2)
        ___qtablewidgetitem28.setText("空心科技有限公司 (qq2448545222)");
        ___qtablewidgetitem29 = self.tableWidget_version_info.item(1, 0)
        ___qtablewidgetitem29.setText("文件描述");
        ___qtablewidgetitem30 = self.tableWidget_version_info.item(1, 2)
        ___qtablewidgetitem30.setText("Pyinstaller打包精灵客户端");
        ___qtablewidgetitem31 = self.tableWidget_version_info.item(2, 0)
        ___qtablewidgetitem31.setText("文件版本");
        ___qtablewidgetitem32 = self.tableWidget_version_info.item(2, 2)
        ___qtablewidgetitem32.setText("1.0");
        ___qtablewidgetitem33 = self.tableWidget_version_info.item(3, 0)
        ___qtablewidgetitem33.setText("内部名称");
        ___qtablewidgetitem34 = self.tableWidget_version_info.item(3, 2)
        ___qtablewidgetitem34.setText("Pyinstasller打包精灵.exe");
        ___qtablewidgetitem35 = self.tableWidget_version_info.item(4, 0)
        ___qtablewidgetitem35.setText("法律版权");
        ___qtablewidgetitem36 = self.tableWidget_version_info.item(4, 2)
        ___qtablewidgetitem36.setText("Copyright(C) 2022 - 2022 qq2448545222. All Right Reserved");
        ___qtablewidgetitem37 = self.tableWidget_version_info.item(5, 0)
        ___qtablewidgetitem37.setText("原始名称");
        ___qtablewidgetitem38 = self.tableWidget_version_info.item(5, 2)
        ___qtablewidgetitem38.setText("Pyinstasller打包精灵.exe");
        ___qtablewidgetitem39 = self.tableWidget_version_info.item(6, 0)
        ___qtablewidgetitem39.setText("产品名称");
        ___qtablewidgetitem40 = self.tableWidget_version_info.item(6, 2)
        ___qtablewidgetitem40.setText("Pyinstasller打包精灵");
        ___qtablewidgetitem41 = self.tableWidget_version_info.item(7, 0)
        ___qtablewidgetitem41.setText("产品版本");
        ___qtablewidgetitem42 = self.tableWidget_version_info.item(7, 2)
        ___qtablewidgetitem42.setText("1.0");
        self.tableWidget_version_info.setSortingEnabled(__sortingEnabled)

        self.groupBox_log.setTitle("日志")
        self.btn_help.setText("使用说明")
        self.btn_reset.setText("重置")
        self.btn_start.setText("开始打包")
    # retranslateUi
