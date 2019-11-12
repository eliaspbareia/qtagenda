from PySide2.QtWidgets import (QFrame, QAbstractItemView, QFormLayout, QVBoxLayout, QHBoxLayout)
from PySide2.QtWidgets import QListWidget


class Listagem(QFrame):

    def __init__(self, master=None):

        super().__init__(master)
        self.listView = QListWidget(self)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.formlayout = QFormLayout()
        self.formlayout.addWidget(self.listView)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.formlayout)

        self.setLayout(self.mainLayout)

    def limpar(self):
        self.listView.clear()

    def insert(self, registro):
        self.listView.addItem(registro)

    def delete(self, index):
        self.listView.itemDelegateForRow(index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.listView.currentIndex())
        self.listView.clicked.connect(handler)

    def itemselecionado(self, item):
        print('!!! click {}'.format(item.text()))

