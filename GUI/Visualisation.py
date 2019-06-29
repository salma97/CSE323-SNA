# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
import matplotlib.pyplot as plt
import copy
import os


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FormContainer = QtWidgets.QVBoxLayout()
        self.FormContainer.setObjectName("FormContainer")
        self.GraphView = QtWidgets.QWidget(Form)
        self.GraphView.setMinimumSize(QtCore.QSize(400, 300))
        self.GraphView.setObjectName("GraphView")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.GraphView)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ImageLabel = QtWidgets.QLabel()
        self.horizontalLayout_4.addWidget(self.ImageLabel)
        self.FormContainer.addWidget(self.GraphView)
        self.inputWidget = QtWidgets.QWidget(Form)
        self.inputWidget.setMaximumSize(QtCore.QSize(700, 50))
        self.inputWidget.setObjectName("inputWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.inputWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.inputWidgetLayout = QtWidgets.QHBoxLayout()
        self.inputWidgetLayout.setObjectName("inputWidgetLayout")
        self.OpenFile = QtWidgets.QPushButton(self.inputWidget)
        self.OpenFile.setObjectName("OpenFile")
        self.inputWidgetLayout.addWidget(self.OpenFile)
        self.Betweenness = QtWidgets.QPushButton(self.inputWidget)
        self.Betweenness.setObjectName("Betweenness")
        self.inputWidgetLayout.addWidget(self.Betweenness)
        self.Closeness = QtWidgets.QPushButton(self.inputWidget)
        self.Closeness.setObjectName("Closeness")
        self.inputWidgetLayout.addWidget(self.Closeness)
        self.Degree = QtWidgets.QPushButton(self.inputWidget)
        self.Degree.setObjectName("Degree")
        self.inputWidgetLayout.addWidget(self.Degree)
        self.horizontalLayout_3.addLayout(self.inputWidgetLayout)
        self.FormContainer.addWidget(self.inputWidget)
        self.horizontalLayout.addLayout(self.FormContainer)

        self.FileContents = []
        self.Graph = []

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.OpenFile.clicked.connect(self.OpenFileDialog)
        self.Degree.clicked.connect(self.DegreeCentrality)
        self.Closeness.clicked.connect(self.ClosenessCentrality)
        self.Betweenness.clicked.connect(self.BetweennessCentrality)

    def OpenFileDialog(self):
        self.FileDialog = QtWidgets.QFileDialog()
        fname = self.FileDialog.getOpenFileName()
        f = open(fname[0])
        if f.mode == 'r':
            self.FileContents = f.readlines()

    def DegreeCentrality(self):
        self.ViewGraph(0)

    def ClosenessCentrality(self):
        self.ViewGraph(1)

    def BetweennessCentrality(self):
        self.ViewGraph(2)

    def ViewGraph(self, option):
        G = nx.Graph()
        elist = []
        for line in self.FileContents:
            edge = line.split()
            elist.append(edge)
        elist.remove(elist[0])
        G.add_weighted_edges_from(elist)
        if option == 0:
            a = nx.degree_centrality(G)
        elif option == 1:
            a = nx.closeness_centrality(G)
        else:
            a = nx.betweenness_centrality(G)
        b = []
        for e in a.values():
            b.append(500 + (e*2*3*5*7)**1.5)
        nx.draw(G, with_labels=True, node_size=b)
        plt.savefig("Graph.png")  # save as png
        plt.close()

        pixmap = QtGui.QPixmap("Graph.png")
        self.ImageLabel.setPixmap(pixmap)
        self.GraphView.setMinimumSize(pixmap.width()+15, pixmap.height()+15)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.OpenFile.setText(_translate("Form", "Open File"))
        self.Betweenness.setText(_translate("Form", "Betweenness"))
        self.Closeness.setText(_translate("Form", "Closeness"))
        self.Degree.setText(_translate("Form", "Degree"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
