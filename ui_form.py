# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 608)
        MainWindow.setStyleSheet(u"background-color: #1f1e2d;\n"
"color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 151, 111))
        self.label.setPixmap(QPixmap(u"../../Im\u00e1genes/Screenshots/Captura de pantalla 2025-10-10 003256.png"))
        self.label.setScaledContents(True)
        self.tableProcesos = QTableWidget(self.centralwidget)
        if (self.tableProcesos.columnCount() < 4):
            self.tableProcesos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProcesos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProcesos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProcesos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProcesos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableProcesos.setObjectName(u"tableProcesos")
        self.tableProcesos.setEnabled(True)
        self.tableProcesos.setGeometry(QRect(620, 50, 441, 481))
        self.tableProcesos.setAcceptDrops(False)
        self.tableProcesos.setAutoFillBackground(False)
        self.tableProcesos.setStyleSheet(u"QTableWidget {\n"
"    background-color: #26253a;             /* Fondo de tabla oscuro */\n"
"    color: #f0f0f0;                        /* Texto claro */\n"
"    gridline-color: #3a3950;               /* L\u00edneas sutiles */\n"
"    selection-background-color: #ff7b00;   /* Naranja vibrante para selecci\u00f3n */\n"
"    selection-color: #ffffff;              /* Texto blanco sobre selecci\u00f3n */\n"
"    alternate-background-color: #2d2c44;   /* Filas alternadas */\n"
"    border: none;\n"
"    border-radius: 6px;                    /* Bordes redondeados */\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #2f2e48;             /* Encabezado intermedio */\n"
"    color: #ff9500;                        /* Texto naranja moderno */\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    padding: 8px;\n"
"    border-bottom: 2px solid #ff7b00;      /* L\u00ednea inferior naranja */\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #2f2e48;\n"
"    border"
                        ": none;\n"
"}\n"
"\n"
"/* ScrollBar vertical */\n"
"QScrollBar:vertical {\n"
"    background: #1f1e2d;\n"
"    width: 10px;\n"
"    margin: 2px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #ff7b00,\n"
"        stop:1 #ffae42\n"
"    );                                     /* Degradado naranja cyberpunk */\n"
"    border-radius: 5px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: qlineargradient(\n"
"        x1:0, y1:0, x2:1, y2:0,\n"
"        stop:0 #ff9500,\n"
"        stop:1 #ff7b00\n"
"    );\n"
"}\n"
"\n"
"/* Opcional: bordes suaves en hover */\n"
"QTableWidget::item:hover {\n"
"    background-color: rgba(255, 123, 0, 0.2);  /* Naranja transl\u00facido */\n"
"    border-radius: 4px;\n"
"}\n"
"")
        self.tableProcesos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableProcesos.setAlternatingRowColors(True)
        self.tableProcesos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableProcesos.setShowGrid(True)
        self.tableProcesos.setSortingEnabled(True)
        self.tableProcesos.setRowCount(0)
        self.tableProcesos.setColumnCount(4)
        self.tableProcesos.horizontalHeader().setCascadingSectionResizes(True)
        self.tableProcesos.horizontalHeader().setStretchLastSection(True)
        self.tableProcesos.verticalHeader().setStretchLastSection(True)
        self.progressBarCPU = QProgressBar(self.centralwidget)
        self.progressBarCPU.setObjectName(u"progressBarCPU")
        self.progressBarCPU.setGeometry(QRect(10, 200, 161, 61))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.progressBarCPU.setFont(font)
        self.progressBarCPU.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #ff4fa0;\n"
"    border-radius: 12px;\n"
"    text-align: center;\n"
"    background-color: #1a1a2e;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #ff4fa0,\n"
"        stop: 0.5 #d94fff,\n"
"        stop: 1 #ff85d0\n"
"    );\n"
"    /* brillo suave tipo ne\u00f3n */\n"
"    box-shadow: 0px 0px 12px #ff4fa0;\n"
"}\n"
"QProgressBar {\n"
"    border: 2px solid #ff4fa0;\n"
"    border-radius: 12px;\n"
"    text-align: center;\n"
"    background-color: #1a1a2e;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #ff4fa0,\n"
"        stop: 0.5 #d94fff,\n"
"        stop: 1 #ff85d0\n"
"    );\n"
"    /* brillo"
                        " suave tipo ne\u00f3n */\n"
"    box-shadow: 0px 0px 12px #ff4fa0;\n"
"}\n"
"")
        self.progressBarCPU.setValue(49)
        self.progressBarMem = QProgressBar(self.centralwidget)
        self.progressBarMem.setObjectName(u"progressBarMem")
        self.progressBarMem.setGeometry(QRect(10, 320, 161, 61))
        self.progressBarMem.setFont(font)
        self.progressBarMem.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #00ff85;\n"
"    border-radius: 12px;\n"
"    text-align: center;\n"
"    background-color: #1a1a2e;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #00ff85,\n"
"        stop: 0.5 #00d46a,\n"
"        stop: 1 #66ffb2\n"
"    );\n"
"    box-shadow: 0px 0px 12px #00ff85;\n"
"}\n"
"")
        self.progressBarMem.setValue(49)
        self.progressBarDisc = QProgressBar(self.centralwidget)
        self.progressBarDisc.setObjectName(u"progressBarDisc")
        self.progressBarDisc.setGeometry(QRect(10, 440, 161, 61))
        self.progressBarDisc.setFont(font)
        self.progressBarDisc.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #3a7dff;\n"
"    border-radius: 12px;\n"
"    text-align: center;\n"
"    background-color: #1a1a2e;\n"
"    color: #ffffff;\n"
"    font-weight: bold;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #3a7dff,\n"
"        stop: 0.5 #1f5fff,\n"
"        stop: 1 #6aa8ff\n"
"    );\n"
"    box-shadow: 0px 0px 12px #3a7dff;\n"
"}\n"
"")
        self.progressBarDisc.setValue(49)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 160, 51, 31))
        font1 = QFont()
        font1.setFamilies([u"Microsoft Yi Baiti"])
        font1.setPointSize(19)
        self.label_2.setFont(font1)
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setScaledContents(False)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 280, 131, 31))
        self.label_3.setFont(font1)
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setScaledContents(False)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 400, 81, 31))
        self.label_4.setFont(font1)
        self.label_4.setTextFormat(Qt.TextFormat.AutoText)
        self.label_4.setScaledContents(False)
        self.pushButtonKill = QPushButton(self.centralwidget)
        self.pushButtonKill.setObjectName(u"pushButtonKill")
        self.pushButtonKill.setGeometry(QRect(620, 540, 80, 21))
        self.graphic1 = PlotWidget(self.centralwidget)
        self.graphic1.setObjectName(u"graphic1")
        self.graphic1.setGeometry(QRect(230, 20, 361, 161))
        self.graphic1.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_5 = QLabel(self.graphic1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(310, 0, 51, 31))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u" background-color: #26253a; \n"
"color: #ff4fa0;")
        self.label_5.setTextFormat(Qt.TextFormat.AutoText)
        self.label_5.setScaledContents(False)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(710, 546, 81, 31))
        self.label_9.setFont(font1)
        self.label_9.setTextFormat(Qt.TextFormat.AutoText)
        self.label_9.setScaledContents(False)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(860, 546, 141, 31))
        self.label_10.setFont(font1)
        self.label_10.setTextFormat(Qt.TextFormat.AutoText)
        self.label_10.setScaledContents(False)
        self.SpinCantidad = QSpinBox(self.centralwidget)
        self.SpinCantidad.setObjectName(u"SpinCantidad")
        self.SpinCantidad.setGeometry(QRect(760, 540, 91, 36))
        self.SpinCantidad.setMinimum(1)
        self.SpinCantidad.setMaximum(1000)
        self.SpinIntervalo = QSpinBox(self.centralwidget)
        self.SpinIntervalo.setObjectName(u"SpinIntervalo")
        self.SpinIntervalo.setGeometry(QRect(970, 540, 91, 36))
        self.SpinIntervalo.setMinimum(1)
        self.SpinIntervalo.setMaximum(1000)
        self.graphic2 = PlotWidget(self.centralwidget)
        self.graphic2.setObjectName(u"graphic2")
        self.graphic2.setGeometry(QRect(230, 210, 361, 141))
        self.graphic2.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_6 = QLabel(self.graphic2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(260, 0, 131, 31))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u" background-color: #26253a; \n"
"color: #00ff85;")
        self.label_6.setTextFormat(Qt.TextFormat.AutoText)
        self.label_6.setScaledContents(False)
        self.graphic3 = PlotWidget(self.centralwidget)
        self.graphic3.setObjectName(u"graphic3")
        self.graphic3.setGeometry(QRect(230, 400, 361, 141))
        self.graphic3.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        self.label_7 = QLabel(self.graphic3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(290, 0, 81, 31))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: #26253a; \n"
"color: #3a7dff;")
        self.label_7.setTextFormat(Qt.TextFormat.AutoText)
        self.label_7.setScaledContents(False)
        self.TotalDisc = QLabel(self.centralwidget)
        self.TotalDisc.setObjectName(u"TotalDisc")
        self.TotalDisc.setGeometry(QRect(230, 550, 111, 31))
        font2 = QFont()
        font2.setFamilies([u"Microsoft Yi Baiti"])
        font2.setPointSize(14)
        self.TotalDisc.setFont(font2)
        self.TotalDisc.setTextFormat(Qt.TextFormat.AutoText)
        self.TotalDisc.setScaledContents(False)
        self.pushButtonRefresh = QPushButton(self.centralwidget)
        self.pushButtonRefresh.setObjectName(u"pushButtonRefresh")
        self.pushButtonRefresh.setGeometry(QRect(620, 560, 80, 21))
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(620, 10, 181, 31))
        font3 = QFont()
        font3.setFamilies([u"Microsoft Yi Baiti"])
        font3.setPointSize(16)
        self.label_11.setFont(font3)
        self.label_11.setStyleSheet(u"QLabel {\n"
"    padding: 2px 4px;  /* arriba/abajo = 2px, izquierda/derecha = 4px */\n"
"}")
        self.label_11.setTextFormat(Qt.TextFormat.AutoText)
        self.label_11.setScaledContents(False)
        self.LineEditFiltroNombre = QLineEdit(self.centralwidget)
        self.LineEditFiltroNombre.setObjectName(u"LineEditFiltroNombre")
        self.LineEditFiltroNombre.setGeometry(QRect(750, 13, 311, 31))
        self.LineEditFiltroNombre.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #ff7b00;       /* Borde naranja vibrante */\n"
"    border-radius: 8px;              /* Bordes redondeados */\n"
"    padding: 6px;                    /* Espaciado interno */\n"
"    background-color: #1f1e2d;       /* Fondo oscuro */\n"
"    color: #ffffff;                  /* Texto blanco */\n"
"    selection-background-color: #ff7b00; /* Selecci\u00f3n naranja */\n"
"    selection-color: #000000;        /* Texto negro al seleccionar */\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.UsadoDisc = QLabel(self.centralwidget)
        self.UsadoDisc.setObjectName(u"UsadoDisc")
        self.UsadoDisc.setGeometry(QRect(340, 550, 151, 31))
        self.UsadoDisc.setFont(font2)
        self.UsadoDisc.setTextFormat(Qt.TextFormat.AutoText)
        self.UsadoDisc.setScaledContents(False)
        self.LibreDisc = QLabel(self.centralwidget)
        self.LibreDisc.setObjectName(u"LibreDisc")
        self.LibreDisc.setGeometry(QRect(470, 550, 141, 31))
        self.LibreDisc.setFont(font2)
        self.LibreDisc.setTextFormat(Qt.TextFormat.AutoText)
        self.LibreDisc.setScaledContents(False)
        self.TotalMem = QLabel(self.centralwidget)
        self.TotalMem.setObjectName(u"TotalMem")
        self.TotalMem.setGeometry(QRect(230, 360, 111, 31))
        self.TotalMem.setFont(font2)
        self.TotalMem.setTextFormat(Qt.TextFormat.AutoText)
        self.TotalMem.setScaledContents(False)
        self.UsadoMem = QLabel(self.centralwidget)
        self.UsadoMem.setObjectName(u"UsadoMem")
        self.UsadoMem.setGeometry(QRect(340, 360, 151, 31))
        self.UsadoMem.setFont(font2)
        self.UsadoMem.setTextFormat(Qt.TextFormat.AutoText)
        self.UsadoMem.setScaledContents(False)
        self.LibreMem = QLabel(self.centralwidget)
        self.LibreMem.setObjectName(u"LibreMem")
        self.LibreMem.setGeometry(QRect(460, 360, 141, 31))
        self.LibreMem.setFont(font2)
        self.LibreMem.setTextFormat(Qt.TextFormat.AutoText)
        self.LibreMem.setScaledContents(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1076, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        ___qtablewidgetitem = self.tableProcesos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        ___qtablewidgetitem1 = self.tableProcesos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOMBRE", None));
        ___qtablewidgetitem2 = self.tableProcesos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CPU %", None));
        ___qtablewidgetitem3 = self.tableProcesos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"RAM %", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MEMORIA", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DISCO", None))
        self.pushButtonKill.setText(QCoreApplication.translate("MainWindow", u"KILL", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Filtrar</span></p><p><span style=\" font-size:16pt;\"><br/></span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Intervalo(ms)</span></p><p><br/></p><p><span style=\" font-size:16pt;\"><br/></span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MEMORIA", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DISCO", None))
        self.TotalDisc.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.pushButtonRefresh.setText(QCoreApplication.translate("MainWindow", u"REFRESH", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Filtrar Nombre", None))
        self.UsadoDisc.setText(QCoreApplication.translate("MainWindow", u"Usado:", None))
        self.LibreDisc.setText(QCoreApplication.translate("MainWindow", u"Libre:", None))
        self.TotalMem.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.UsadoMem.setText(QCoreApplication.translate("MainWindow", u"Usado:", None))
        self.LibreMem.setText(QCoreApplication.translate("MainWindow", u"Libre:", None))
    # retranslateUi

