# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ok_message_boxLfZxFk.ui'
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

class Ui_OKMessageBox(object):
    def setupUi(self, OKMessageBox):
        if not OKMessageBox.objectName():
            OKMessageBox.setObjectName(u"OKMessageBox")
        OKMessageBox.setWindowModality(Qt.WindowModality.ApplicationModal)
        OKMessageBox.resize(328, 128)
        OKMessageBox.setMinimumSize(QSize(328, 128))
        OKMessageBox.setStyleSheet(u"QToolTip {\n"
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
        OKMessageBox.setModal(True)
        self.verticalLayout = QVBoxLayout(OKMessageBox)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 3)
        self.frame = QFrame(OKMessageBox)
        self.frame.setObjectName(u"frame")
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy)
        self.msg_label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.msg_label)


        self.verticalLayout.addWidget(self.frame)

        self.ok_btn = QPushButton(OKMessageBox)
        self.ok_btn.setObjectName(u"ok_btn")
        self.ok_btn.setMinimumSize(QSize(0, 0))
        self.ok_btn.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.verticalLayout.addWidget(self.ok_btn)


        self.retranslateUi(OKMessageBox)

        QMetaObject.connectSlotsByName(OKMessageBox)
    # setupUi

    def retranslateUi(self, OKMessageBox):
        OKMessageBox.setWindowTitle(QCoreApplication.translate("OKMessageBox", u"Phils-Hub - OK Message Box", None))
        self.label.setText("")
        self.msg_label.setText(QCoreApplication.translate("OKMessageBox", u"OK Message Box...", None))
        self.ok_btn.setText(QCoreApplication.translate("OKMessageBox", u"OK", None))
    # retranslateUi

