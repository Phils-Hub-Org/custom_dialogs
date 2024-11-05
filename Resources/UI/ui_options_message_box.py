# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_message_boxpZbOEC.ui'
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
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)
import Resources.resources_rc

class Ui_OptionsMessageBox(object):
    def setupUi(self, OptionsMessageBox):
        if not OptionsMessageBox.objectName():
            OptionsMessageBox.setObjectName(u"OptionsMessageBox")
        OptionsMessageBox.setWindowModality(Qt.WindowModality.ApplicationModal)
        OptionsMessageBox.resize(328, 128)
        OptionsMessageBox.setMinimumSize(QSize(328, 128))
        OptionsMessageBox.setStyleSheet(u"QToolTip {\n"
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
"QRadioButton {\n"
"    color: #ffffff;\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    background-color: #2e2e2e;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: #4a90e2;\n"
"    border-color: #3d78b2;\n"
""
                        "}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4a90e2;\n"
"    border-color: #3d78b2;\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}")
        OptionsMessageBox.setModal(True)
        self.verticalLayout = QVBoxLayout(OptionsMessageBox)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 3)
        self.frame = QFrame(OptionsMessageBox)
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

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.msg_label = QLabel(self.frame_3)
        self.msg_label.setObjectName(u"msg_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy2)
        self.msg_label.setMaximumSize(QSize(16777215, 16))
        self.msg_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.msg_label)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	border-bottom-left-radius: 9px;\n"
"	border-bottom-right-radius: 9px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.option1 = QRadioButton(self.frame_2)
        self.option1.setObjectName(u"option1")
        self.option1.setChecked(True)

        self.verticalLayout_2.addWidget(self.option1)

        self.option2 = QRadioButton(self.frame_2)
        self.option2.setObjectName(u"option2")

        self.verticalLayout_2.addWidget(self.option2)

        self.option3 = QRadioButton(self.frame_2)
        self.option3.setObjectName(u"option3")
        self.option3.setChecked(False)

        self.verticalLayout_2.addWidget(self.option3)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.submit_btn = QPushButton(OptionsMessageBox)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setMinimumSize(QSize(0, 0))
        self.submit_btn.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.verticalLayout.addWidget(self.submit_btn)


        self.retranslateUi(OptionsMessageBox)

        QMetaObject.connectSlotsByName(OptionsMessageBox)
    # setupUi

    def retranslateUi(self, OptionsMessageBox):
        OptionsMessageBox.setWindowTitle(QCoreApplication.translate("OptionsMessageBox", u"Phils-Hub - Options Message Box", None))
        self.label.setText("")
        self.msg_label.setText(QCoreApplication.translate("OptionsMessageBox", u"Options Message Box...", None))
        self.option1.setText(QCoreApplication.translate("OptionsMessageBox", u"RadioButton", None))
        self.option2.setText(QCoreApplication.translate("OptionsMessageBox", u"RadioButton", None))
        self.option3.setText(QCoreApplication.translate("OptionsMessageBox", u"RadioButton", None))
        self.submit_btn.setText(QCoreApplication.translate("OptionsMessageBox", u"Submit", None))
    # retranslateUi

