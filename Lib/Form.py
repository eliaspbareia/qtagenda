from PySide2.QtWidgets import ( QDateEdit, QLineEdit, QVBoxLayout, QFrame, QFormLayout)
from PySide2.QtCore import *
from Model.Dataset import Dataset as dataset
from Model.Person import Person as model
"""
Principais componentes:
QLineEdit 
QTextEdit
QDateEdit
QGroupBox - agrupa os componentes acima
"""

class Form(QFrame):

    def __init__(self, master=None, *campos, **kwargs):
        super().__init__(master)

        self.formlayout = QFormLayout()
        self.formulario = self.form()
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.formlayout)
        self.setLayout(self.mainLayout)
        self.setWindowTitle(self.tr("Agenda"))
        self.rowid = 0

    def form(self):
        self.nameEdit = QLineEdit()
        self.emailEdit = QLineEdit()
        self.phoneEdit = QLineEdit()
        self.phoneEdit.setInputMask("(00)0000-0000")
        self.dtanascEdit = QDateEdit()
        self.formlayout.addRow("&Nome",self.nameEdit)
        self.formlayout.addRow("&Email", self.emailEdit)
        self.formlayout.addRow("&Celular", self.phoneEdit)
        self.formlayout.addRow("&Data Nasc.", self.dtanascEdit)

    def lerdetalhes(self, index):
        records = dataset.selectbyid(model, index)
        for row in records:
            self.rowid = row.id
            self.nameEdit.setText(row.nomeperson)
            self.emailEdit.setText(row.emailperson)
            self.phoneEdit.setText(row.telefoneperson)
            self.dtanascEdit.setDate(row.dtanascimentoperson)

    def limparformulario(self):
        self.rowid = 0
        self.nameEdit.setText('')
        self.nameEdit.setFocus()
        self.emailEdit.setText('')
        self.phoneEdit.setText('')
        self.dtanascEdit.setDate(QDate.currentDate())


    def cancel(self):
        self.newBtn.setEnabled(True)

    def pegavalores(self):
        nnome = self.nameEdit.text()
        eemail = self.emailEdit.text()
        pphone = self.phoneEdit.text()
        ddtanascimento = self.dtanascEdit.text()
        if self.rowid == 0:
            values = {'nomeperson': nnome, 'emailperson': eemail, 'telefoneperson': pphone, 'dtanascimentoperson': ddtanascimento}
        else:
            values = {'id': self.rowid,'nomeperson': nnome, 'emailperson': eemail, 'telefoneperson': pphone, 'dtanascimentoperson': ddtanascimento}
        return values



