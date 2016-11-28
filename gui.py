from PyQt5.QtWidgets import (QVBoxLayout, QApplication, QGroupBox, QPushButton, QHBoxLayout, QWidget, QLineEdit)
import graph
import networkx as nx


class Window(QWidget):
    def dodaj(self):
        widget = Group()
        self.layout.addWidget(widget)
        self.tab.append(widget)

    def licz(self):
        for i in self.tab:
            activity = i.ed1.displayText()
            how_long = i.ed2.displayText()
            how_long = int(how_long)
            sequence = i.ed3.displayText()
            graph.add_Edge(self.Graph, int(sequence[0]), int(sequence[2]), how_long)
        nx.set_node_attributes(self.Graph, 't1', 0)
        nx.set_node_attributes(self.Graph, 't2', 0)
        nx.set_node_attributes(self.Graph, 'luz', 0)
        nx.set_node_attributes(self.Graph, 'from', 0)
        graph.PERT(self.Graph)

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.Graph = nx.DiGraph()

        self.tab = []
        self.layout = QVBoxLayout()
        btn_dodaj = QPushButton("Dodaj zdarzenie", self)
        btn_dodaj.clicked.connect(self.dodaj)

        btn_licz = QPushButton("Licz", self)
        btn_licz.clicked.connect(self.licz)

        self.layout.addWidget(btn_dodaj)
        self.layout.addWidget(btn_licz)
        self.setLayout(self.layout)
        self.setWindowTitle("Group Box")
        self.resize(480, 320)


class Group(QGroupBox):
    def __init__(self, parent=None):
        super(Group, self).__init__(parent)

        self.initGroup()

    def initGroup(self):
        hbox = QHBoxLayout()
        self.ed1 = QLineEdit()
        self.ed1.setPlaceholderText("nazwa czynności")
        self.ed2 = QLineEdit()
        self.ed2.setPlaceholderText("czas trwania")
        self.ed3 = QLineEdit()
        self.ed3.setPlaceholderText("kolejność zdarzeń")
        hbox.addWidget(self.ed1)
        hbox.addWidget(self.ed2)
        hbox.addWidget(self.ed3)
        self.setLayout(hbox)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())
