# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'yes_no_message_boxSjljMr.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import Resources.resources_rc

class Ui_YESNOMessageBox(object):
    def setupUi(self, YESNOMessageBox):
        if not YESNOMessageBox.objectName():
            YESNOMessageBox.setObjectName(u"YESNOMessageBox")
        YESNOMessageBox.setWindowModality(Qt.WindowModality.ApplicationModal)
        YESNOMessageBox.resize(328, 128)
        YESNOMessageBox.setMinimumSize(QSize(328, 128))
        YESNOMessageBox.setStyleSheet(u"QToolTip {\n"
"    background-color: #2e2e2e;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5b5e60;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"    opacity: 200;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3c3f41;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"	padding: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #4a90e2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}\n"
"\n"
"/*\n"
"red: ff050d\n"
"green: 0dce1d\n"
"*/")
        YESNOMessageBox.setModal(True)
        self.verticalLayout = QVBoxLayout(YESNOMessageBox)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 3)
        self.frame = QFrame(YESNOMessageBox)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"QFrame {\n"
"	border-top-left-radius: 9px;\n"
"	border-top-right-radius: 9px;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/ico/Icons/ico/phils-hub.ico"))

        self.horizontalLayout.addWidget(self.label)

        self.msg_label = QLabel(self.frame)
        self.msg_label.setObjectName(u"msg_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy1)
        self.msg_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.msg_label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(YESNOMessageBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	border-bottom-left-radius: 9px;\n"
"	border-bottom-right-radius: 9px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.yes_btn = QPushButton(self.frame_2)
        self.yes_btn.setObjectName(u"yes_btn")
        self.yes_btn.setMinimumSize(QSize(0, 0))
        self.yes_btn.setStyleSheet(u"QPushButton {\n"
"	border-bottom-right-radius: 0px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.yes_btn)

        self.no_btn = QPushButton(self.frame_2)
        self.no_btn.setObjectName(u"no_btn")
        self.no_btn.setMinimumSize(QSize(0, 0))
        self.no_btn.setStyleSheet(u"QPushButton {\n"
"	border-bottom-left-radius: 0px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.no_btn)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(YESNOMessageBox)

        QMetaObject.connectSlotsByName(YESNOMessageBox)
    # setupUi

    def retranslateUi(self, YESNOMessageBox):
        YESNOMessageBox.setWindowTitle(QCoreApplication.translate("YESNOMessageBox", u"Phils-Hub - YES/NO Message Box", None))
        self.label.setText("")
        self.msg_label.setText(QCoreApplication.translate("YESNOMessageBox", u"YES/NO Message Box...", None))
        self.yes_btn.setText(QCoreApplication.translate("YESNOMessageBox", u"YES", None))
        self.no_btn.setText(QCoreApplication.translate("YESNOMessageBox", u"NO", None))
    # retranslateUi

