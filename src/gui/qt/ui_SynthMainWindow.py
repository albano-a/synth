# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SynthMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QDockWidget,
    QFrame, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QToolBar, QWidget)
from gui.resources import main_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 775)
        icon = QIcon()
        icon.addFile(u":/icons/icons/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.actionOpen_LAS = QAction(MainWindow)
        self.actionOpen_LAS.setObjectName(u"actionOpen_LAS")
        self.actionOpen_Wavelet = QAction(MainWindow)
        self.actionOpen_Wavelet.setObjectName(u"actionOpen_Wavelet")
        self.actionRecent_Files = QAction(MainWindow)
        self.actionRecent_Files.setObjectName(u"actionRecent_Files")
        self.actionPNG = QAction(MainWindow)
        self.actionPNG.setObjectName(u"actionPNG")
        self.actionPDF = QAction(MainWindow)
        self.actionPDF.setObjectName(u"actionPDF")
        self.actionCSV = QAction(MainWindow)
        self.actionCSV.setObjectName(u"actionCSV")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionShow_Hide_Controls_Panel = QAction(MainWindow)
        self.actionShow_Hide_Controls_Panel.setObjectName(u"actionShow_Hide_Controls_Panel")
        self.actionAbout_Synth = QAction(MainWindow)
        self.actionAbout_Synth.setObjectName(u"actionAbout_Synth")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.mwDisplayWidget = QWidget(self.centralwidget)
        self.mwDisplayWidget.setObjectName(u"mwDisplayWidget")

        self.gridLayout_3.addWidget(self.mwDisplayWidget, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1033, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuExport_Figure = QMenu(self.menuFile)
        self.menuExport_Figure.setObjectName(u"menuExport_Figure")
        self.menuExport_Synthetic = QMenu(self.menuFile)
        self.menuExport_Synthetic.setObjectName(u"menuExport_Synthetic")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setMinimumSize(QSize(428, 495))
        self.dockWidget.setMaximumSize(QSize(450, 524287))
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout_2 = QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.dockWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mwDepthBottomInput = QLineEdit(self.groupBox)
        self.mwDepthBottomInput.setObjectName(u"mwDepthBottomInput")

        self.gridLayout_5.addWidget(self.mwDepthBottomInput, 3, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 3, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 3, 0, 1, 1)

        self.mwDepthTopInput = QLineEdit(self.groupBox)
        self.mwDepthTopInput.setObjectName(u"mwDepthTopInput")

        self.gridLayout_5.addWidget(self.mwDepthTopInput, 3, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_5.addWidget(self.label_6, 3, 4, 1, 1)

        self.mwRhobCurveCombobox = QComboBox(self.groupBox)
        self.mwRhobCurveCombobox.setObjectName(u"mwRhobCurveCombobox")

        self.gridLayout_5.addWidget(self.mwRhobCurveCombobox, 2, 1, 1, 4)

        self.mwVpCurveCombobox = QComboBox(self.groupBox)
        self.mwVpCurveCombobox.setObjectName(u"mwVpCurveCombobox")

        self.gridLayout_5.addWidget(self.mwVpCurveCombobox, 1, 1, 1, 4)

        self.mwBrowseButton = QPushButton(self.groupBox)
        self.mwBrowseButton.setObjectName(u"mwBrowseButton")

        self.gridLayout_5.addWidget(self.mwBrowseButton, 0, 4, 1, 1)

        self.mwLasFileInput = QLineEdit(self.groupBox)
        self.mwLasFileInput.setObjectName(u"mwLasFileInput")

        self.gridLayout_5.addWidget(self.mwLasFileInput, 0, 1, 1, 3)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.dockWidgetContents)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.mwWaveletTypeStackedWidget = QStackedWidget(self.groupBox_2)
        self.mwWaveletTypeStackedWidget.setObjectName(u"mwWaveletTypeStackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mwWaveletTypeStackedWidget.sizePolicy().hasHeightForWidth())
        self.mwWaveletTypeStackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_11 = QGridLayout(self.page)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer, 4, 0, 1, 3)

        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_10.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.gridLayout_10.addWidget(self.label_7, 0, 0, 1, 3)

        self.mwRickerPeakFreqInput = QLineEdit(self.page)
        self.mwRickerPeakFreqInput.setObjectName(u"mwRickerPeakFreqInput")

        self.gridLayout_10.addWidget(self.mwRickerPeakFreqInput, 1, 1, 1, 1)

        self.mwRickerTimeInput = QLineEdit(self.page)
        self.mwRickerTimeInput.setObjectName(u"mwRickerTimeInput")

        self.gridLayout_10.addWidget(self.mwRickerTimeInput, 3, 1, 1, 1)

        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 2, 0, 1, 1)

        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_10.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_13 = QLabel(self.page)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_10.addWidget(self.label_13, 2, 2, 1, 1)

        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_10.addWidget(self.label_12, 3, 2, 1, 1)

        self.mwRickerSamplesInput = QLineEdit(self.page)
        self.mwRickerSamplesInput.setObjectName(u"mwRickerSamplesInput")

        self.gridLayout_10.addWidget(self.mwRickerSamplesInput, 2, 1, 1, 1)

        self.label_14 = QLabel(self.page)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_10.addWidget(self.label_14, 1, 2, 1, 1)

        self.mwRickerGenerateButton = QPushButton(self.page)
        self.mwRickerGenerateButton.setObjectName(u"mwRickerGenerateButton")

        self.gridLayout_10.addWidget(self.mwRickerGenerateButton, 5, 0, 1, 3)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.mwWaveletTypeStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_13 = QGridLayout(self.page_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.mwOrmsbyLowCutoffFreqInput = QLineEdit(self.page_2)
        self.mwOrmsbyLowCutoffFreqInput.setObjectName(u"mwOrmsbyLowCutoffFreqInput")

        self.gridLayout_12.addWidget(self.mwOrmsbyLowCutoffFreqInput, 2, 5, 1, 1)

        self.label_18 = QLabel(self.page_2)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_12.addWidget(self.label_18, 2, 4, 1, 1)

        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_12.addWidget(self.label_15, 1, 0, 1, 1)

        self.mwOrmsbyHighCutoffFreqInput = QLineEdit(self.page_2)
        self.mwOrmsbyHighCutoffFreqInput.setObjectName(u"mwOrmsbyHighCutoffFreqInput")

        self.gridLayout_12.addWidget(self.mwOrmsbyHighCutoffFreqInput, 1, 5, 1, 1)

        self.label_16 = QLabel(self.page_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_12.addWidget(self.label_16, 1, 4, 1, 1)

        self.mwOrmsbyHighFreqInput = QLineEdit(self.page_2)
        self.mwOrmsbyHighFreqInput.setObjectName(u"mwOrmsbyHighFreqInput")

        self.gridLayout_12.addWidget(self.mwOrmsbyHighFreqInput, 1, 1, 1, 1)

        self.label_17 = QLabel(self.page_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_12.addWidget(self.label_17, 2, 0, 1, 1)

        self.mwOrmsbyLowFreqInput = QLineEdit(self.page_2)
        self.mwOrmsbyLowFreqInput.setObjectName(u"mwOrmsbyLowFreqInput")

        self.gridLayout_12.addWidget(self.mwOrmsbyLowFreqInput, 2, 1, 1, 1)

        self.label_22 = QLabel(self.page_2)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_12.addWidget(self.label_22, 2, 2, 1, 1)

        self.label_24 = QLabel(self.page_2)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_12.addWidget(self.label_24, 2, 6, 1, 1)

        self.label_25 = QLabel(self.page_2)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_12.addWidget(self.label_25, 1, 6, 1, 1)

        self.label_23 = QLabel(self.page_2)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_12.addWidget(self.label_23, 1, 2, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.mwOrmsbySamplesInput = QLineEdit(self.page_2)
        self.mwOrmsbySamplesInput.setObjectName(u"mwOrmsbySamplesInput")

        self.gridLayout_14.addWidget(self.mwOrmsbySamplesInput, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_2, 2, 0, 1, 2)

        self.label_20 = QLabel(self.page_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_14.addWidget(self.label_20, 1, 0, 1, 1)

        self.mwOrmsbyTimeInput = QLineEdit(self.page_2)
        self.mwOrmsbyTimeInput.setObjectName(u"mwOrmsbyTimeInput")

        self.gridLayout_14.addWidget(self.mwOrmsbyTimeInput, 1, 1, 1, 1)

        self.label_19 = QLabel(self.page_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_14.addWidget(self.label_19, 0, 0, 1, 1)

        self.mwGenerateOrmsbyButton = QPushButton(self.page_2)
        self.mwGenerateOrmsbyButton.setObjectName(u"mwGenerateOrmsbyButton")

        self.gridLayout_14.addWidget(self.mwGenerateOrmsbyButton, 3, 0, 1, 2)


        self.gridLayout_12.addLayout(self.gridLayout_14, 3, 0, 1, 7)

        self.line = QFrame(self.page_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_12.addWidget(self.line, 1, 3, 2, 1)

        self.label_21 = QLabel(self.page_2)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_12.addWidget(self.label_21, 0, 0, 1, 7)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.mwWaveletTypeStackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_16 = QGridLayout(self.page_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_26 = QLabel(self.page_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_15.addWidget(self.label_26, 0, 0, 1, 1)

        self.mwWaveletFilePathInput = QLineEdit(self.page_3)
        self.mwWaveletFilePathInput.setObjectName(u"mwWaveletFilePathInput")

        self.gridLayout_15.addWidget(self.mwWaveletFilePathInput, 0, 1, 1, 1)

        self.label_27 = QLabel(self.page_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_15.addWidget(self.label_27, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_3, 3, 0, 1, 3)

        self.mwWaveletFilePathBrowseButton = QPushButton(self.page_3)
        self.mwWaveletFilePathBrowseButton.setObjectName(u"mwWaveletFilePathBrowseButton")

        self.gridLayout_15.addWidget(self.mwWaveletFilePathBrowseButton, 0, 2, 1, 1)

        self.mwWaveletFileSkiprowsInput = QLineEdit(self.page_3)
        self.mwWaveletFileSkiprowsInput.setObjectName(u"mwWaveletFileSkiprowsInput")

        self.gridLayout_15.addWidget(self.mwWaveletFileSkiprowsInput, 1, 1, 1, 2)

        self.label_28 = QLabel(self.page_3)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_15.addWidget(self.label_28, 2, 0, 1, 1)

        self.mwFileReadButton = QPushButton(self.page_3)
        self.mwFileReadButton.setObjectName(u"mwFileReadButton")

        self.gridLayout_15.addWidget(self.mwFileReadButton, 4, 0, 1, 3)

        self.mwWaveletFileDelimiterCombobox = QComboBox(self.page_3)
        self.mwWaveletFileDelimiterCombobox.addItem("")
        self.mwWaveletFileDelimiterCombobox.addItem("")
        self.mwWaveletFileDelimiterCombobox.addItem("")
        self.mwWaveletFileDelimiterCombobox.addItem("")
        self.mwWaveletFileDelimiterCombobox.setObjectName(u"mwWaveletFileDelimiterCombobox")

        self.gridLayout_15.addWidget(self.mwWaveletFileDelimiterCombobox, 2, 1, 1, 2)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.mwWaveletTypeStackedWidget.addWidget(self.page_3)

        self.gridLayout_7.addWidget(self.mwWaveletTypeStackedWidget, 1, 0, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)

        self.mwFileTypeRadioButton = QRadioButton(self.groupBox_2)
        self.mwWaveletTypeRadioGroup = QButtonGroup(MainWindow)
        self.mwWaveletTypeRadioGroup.setObjectName(u"mwWaveletTypeRadioGroup")
        self.mwWaveletTypeRadioGroup.addButton(self.mwFileTypeRadioButton)
        self.mwFileTypeRadioButton.setObjectName(u"mwFileTypeRadioButton")

        self.gridLayout_9.addWidget(self.mwFileTypeRadioButton, 0, 3, 1, 1)

        self.mwOrmsbyTypeRadioButton = QRadioButton(self.groupBox_2)
        self.mwWaveletTypeRadioGroup.addButton(self.mwOrmsbyTypeRadioButton)
        self.mwOrmsbyTypeRadioButton.setObjectName(u"mwOrmsbyTypeRadioButton")

        self.gridLayout_9.addWidget(self.mwOrmsbyTypeRadioButton, 0, 2, 1, 1)

        self.mwRickerTypeRadioButton = QRadioButton(self.groupBox_2)
        self.mwWaveletTypeRadioGroup.addButton(self.mwRickerTypeRadioButton)
        self.mwRickerTypeRadioButton.setObjectName(u"mwRickerTypeRadioButton")

        self.gridLayout_9.addWidget(self.mwRickerTypeRadioButton, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer, 0, 4, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        self.mwWaveletPreviewWidget = QWidget(self.groupBox_2)
        self.mwWaveletPreviewWidget.setObjectName(u"mwWaveletPreviewWidget")
        sizePolicy.setHeightForWidth(self.mwWaveletPreviewWidget.sizePolicy().hasHeightForWidth())
        self.mwWaveletPreviewWidget.setSizePolicy(sizePolicy)
        self.mwWaveletPreviewWidget.setStyleSheet(u"border: 1px solid #000; background-color: white")

        self.gridLayout_7.addWidget(self.mwWaveletPreviewWidget, 2, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)

        self.mwComputeButton = QPushButton(self.dockWidgetContents)
        self.mwComputeButton.setObjectName(u"mwComputeButton")

        self.gridLayout.addWidget(self.mwComputeButton, 2, 0, 1, 1)

        self.mwExportResultsButton = QPushButton(self.dockWidgetContents)
        self.mwExportResultsButton.setObjectName(u"mwExportResultsButton")

        self.gridLayout.addWidget(self.mwExportResultsButton, 3, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_LAS)
        self.menuFile.addAction(self.actionOpen_Wavelet)
        self.menuFile.addAction(self.actionRecent_Files)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport_Synthetic.menuAction())
        self.menuFile.addAction(self.menuExport_Figure.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuExport_Figure.addAction(self.actionPNG)
        self.menuExport_Figure.addAction(self.actionPDF)
        self.menuExport_Synthetic.addAction(self.actionCSV)
        self.menuView.addAction(self.actionShow_Hide_Controls_Panel)
        self.menuHelp.addAction(self.actionAbout_Synth)
        self.toolBar.addAction(self.actionOpen_LAS)

        self.retranslateUi(MainWindow)

        self.mwWaveletTypeStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen_LAS.setText(QCoreApplication.translate("MainWindow", u"Open LAS...", None))
        self.actionOpen_Wavelet.setText(QCoreApplication.translate("MainWindow", u"Open Wavelet...", None))
        self.actionRecent_Files.setText(QCoreApplication.translate("MainWindow", u"Recent Files", None))
        self.actionPNG.setText(QCoreApplication.translate("MainWindow", u"PNG", None))
        self.actionPDF.setText(QCoreApplication.translate("MainWindow", u"PDF", None))
        self.actionCSV.setText(QCoreApplication.translate("MainWindow", u"CSV", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionShow_Hide_Controls_Panel.setText(QCoreApplication.translate("MainWindow", u"Show/Hide Controls Panel", None))
        self.actionAbout_Synth.setText(QCoreApplication.translate("MainWindow", u"About Synth", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuExport_Figure.setTitle(QCoreApplication.translate("MainWindow", u"Export Figure...", None))
        self.menuExport_Synthetic.setTitle(QCoreApplication.translate("MainWindow", u"Export Synthetic...", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Well Log", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"to", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Depth range:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"VP curve:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"RHOB curve:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LAS File:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"meters", None))
        self.mwBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Wavelet", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Peak Frequency:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Ricker", None))
        self.mwRickerPeakFreqInput.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.mwRickerTimeInput.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Samples:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.mwRickerSamplesInput.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.mwRickerGenerateButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.mwOrmsbyLowCutoffFreqInput.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Low Cutoff Freq.", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"High Freq.", None))
        self.mwOrmsbyHighCutoffFreqInput.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"High Cutoff Freq.", None))
        self.mwOrmsbyHighFreqInput.setText(QCoreApplication.translate("MainWindow", u"40", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Low Freq.", None))
        self.mwOrmsbyLowFreqInput.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.mwOrmsbySamplesInput.setText(QCoreApplication.translate("MainWindow", u"36", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.mwOrmsbyTimeInput.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Samples:", None))
        self.mwGenerateOrmsbyButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Ormsby", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Path:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Skiprows", None))
        self.mwWaveletFilePathBrowseButton.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Delimiter", None))
        self.mwFileReadButton.setText(QCoreApplication.translate("MainWindow", u"Read", None))
        self.mwWaveletFileDelimiterCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"space", None))
        self.mwWaveletFileDelimiterCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"tab", None))
        self.mwWaveletFileDelimiterCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"comma", None))
        self.mwWaveletFileDelimiterCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"semicolon", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.mwFileTypeRadioButton.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.mwOrmsbyTypeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Ormsby", None))
        self.mwRickerTypeRadioButton.setText(QCoreApplication.translate("MainWindow", u"Ricker", None))
        self.mwComputeButton.setText(QCoreApplication.translate("MainWindow", u"Compute Synthetic", None))
        self.mwExportResultsButton.setText(QCoreApplication.translate("MainWindow", u"Export Results", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

