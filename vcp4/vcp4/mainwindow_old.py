import os
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QAbstractButton
from qtpyvcp.plugins import getPlugin
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlDatabase
from resources import resources_rc

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        ## Here
        self.rapidZero.clicked.connect(self.buttonRapidZero)
        self.rapidTwentyFive.clicked.connect(self.buttonRapidTwentyFive)
        self.rapidFifty.clicked.connect(self.buttonRapidFifty)
        self.rapidSeventyFive.clicked.connect(self.buttonRapidSeventyFive)
        self.rapidHundred.clicked.connect(self.buttonRapidHundred)
        self.offsetButtonGroup.buttonClicked.connect(self.offsetHandleKeys)
        self.mdiButtonGroup.buttonClicked.connect(self.mdiHandleKeys)
        self.mdiBackSpaceKey.clicked.connect(self.mdiBackSpace)
        self.toolOffsetGroup.buttonClicked.connect(self.toolHandleKeys)
        self.toolOffsetBackspace.clicked.connect(self.toolBackSpace)

        self.mesgbutton.clicked.connect(self.buttonmesgbutton)
        self.tooltblbutton.clicked.connect(self.buttontooltblbutton)
        self.runbutton.clicked.connect(self.buttonrunbutton)
        self.toolmeasbutton.clicked.connect(self.buttontoolmeasbutton)
        self.mdibutton2.clicked.connect(self.buttonmdibutton2)
        self.editbutton.clicked.connect(self.buttoneditbutton)
        self.workoffbutton.clicked.connect(self.buttonworkoffbutton)
        self.jogbutton.clicked.connect(self.buttonjogbutton)
        self.refrtnbutton.clicked.connect(self.buttonrefrtnbutton)

# add any custom methods here


    def offsetHandleKeys(self, button):
        char = str(button.text())
        text = self.offsetLabel.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.offsetLabel.setText(text)


    def mdiHandleKeys(self, button):
        char = str(button.text())
        text = self.mdiEntry.text() or '0'
        if text != '0':
            text += char
        else:
            text = char
        self.mdiEntry.setText(text)

    def mdiBackSpace(self):
        if len(self.mdiEntry.text()) > 0:
            text = self.mdiEntry.text()[:-1]
            self.mdiEntry.setText(text)



    def toolHandleKeys(self, button):
        text = self.toolOffsetLabel.text()
        if len(text) > 0:
            self.toolOffsetLabel.setText(text + button.text())
        else:
            self.toolOffsetLabel.setText(button.text())

    def toolBackSpace(self):
        text = self.toolOffsetLabel.text()[:-1]
        self.toolOffsetLabel.setText(text)
        

    #rapid button   
 
    def buttonRapidZero(self):
        self.rapidZero.setChecked(True)
        self.rapidTwentyFive.setChecked(False)
        self.rapidFifty.setChecked(False)
        self.rapidSeventyFive.setChecked(False)
        self.rapidHundred.setChecked(False)

    def buttonRapidTwentyFive(self):
        self.rapidZero.setChecked(False)
        self.rapidTwentyFive.setChecked(True)
        self.rapidFifty.setChecked(False)
        self.rapidSeventyFive.setChecked(False)
        self.rapidHundred.setChecked(False)

    def buttonRapidFifty(self):
        self.rapidZero.setChecked(False)
        self.rapidTwentyFive.setChecked(False)
        self.rapidFifty.setChecked(True)
        self.rapidSeventyFive.setChecked(False)
        self.rapidHundred.setChecked(False)

    def buttonRapidSeventyFive(self):
        self.rapidZero.setChecked(False)
        self.rapidTwentyFive.setChecked(False)
        self.rapidFifty.setChecked(False)
        self.rapidSeventyFive.setChecked(True)
        self.rapidHundred.setChecked(False)

    def buttonRapidHundred(self):
        self.rapidZero.setChecked(False)
        self.rapidTwentyFive.setChecked(False)
        self.rapidFifty.setChecked(False)
        self.rapidSeventyFive.setChecked(False)
        self.rapidHundred.setChecked(True)
     
       #tab selection button  
    def buttonmesgbutton(self):
        self.mesgbutton.setChecked(True)
        self.tooltblbutton.setChecked(False)
        self.runbutton.setChecked(False)
        self.mdibutton2.setChecked(False)
        self.editbutton.setChecked(False)
        self.toolmeasbutton.setChecked(False)
        self.workoffbutton.setChecked(False)
        self.jogbutton.setChecked(False)
        self.refrtnbutton.setChecked(False)


    def buttontooltblbutton(self):
        self.mesgbutton.setChecked(False)
        self.tooltblbutton.setChecked(True)
        self.runbutton.setChecked(False)
        self.mdibutton2.setChecked(False)
        self.editbutton.setChecked(False)
        self.toolmeasbutton.setChecked(False)
        self.workoffbutton.setChecked(False)
        self.jogbutton.setChecked(False) 
        self.refrtnbutton.setChecked(False)       

    def buttonrunbutton(self):
        self.mesgbutton.setChecked(False)
        self.tooltblbutton.setChecked(False)
        self.runbutton.setChecked(True)
        self.mdibutton2.setChecked(False)
        self.editbutton.setChecked(False)
        self.toolmeasbutton.setChecked(False)
        self.workoffbutton.setChecked(False)
        self.jogbutton.setChecked(False)

    def buttonmdibutton2(self):
        self.mesgbutton.setChecked(False)
        self.tooltblbutton.setChecked(False)
        self.runbutton.setChecked(False)
        self.mdibutton2.setChecked(True)
        self.editbutton.setChecked(False)
        self.toolmeasbutton.setChecked(False)
        self.workoffbutton.setChecked(False)
        self.jogbutton.setChecked(False)   
        self.refrtnbutton.setChecked(False)

    def buttoneditbutton(self):
        self.mesgbutton.setChecked(False)
        self.tooltblbutton.setChecked(False)
        self.runbutton.setChecked(False)
        self.mdibutton2.setChecked(False)
        self.editbutton.setChecked(True)
        self.toolmeasbutton.setChecked(False)
        self.workoffbutton.setChecked(False)
        self.jogbutton.setChecked(False)
        self.refrtnbutton.setChecked(False)


    def buttontoolmeasbutton(self):
        self.mesgbutton.setChecked(False)
        self.tooltblbutton.setChecked(False)
        self.runbutton.setChecked(False)
        self.mdibutton2.setChecked(False)
        self.editbutton.setChecked(False)
        self.toolmeasbutton.setChecked(True)
        self.workoffbutton.setChecked(False)
        self.jogbutton.setChecked(False)
        self.refrtnbutton.setChecked(False)

    def buttonworkoffbutton(self):
        self.mesgbutton.setChecked(False)
        self.tooltblbutton.setChecked(False)
        self.runbutton.setChecked(False)
        self.mdibutton2.setChecked(False)
        self.editbutton.setChecked(False)
        self.toolmeasbutton.setChecked(False)
        self.workoffbutton.setChecked(True)
        self.jogbutton.setChecked(False)
        self.refrtnbutton.setChecked(False)

    def buttonjogbutton(self):
     
        self.mesgbutton.setChecked(False)
        self.tooltblbutton.setChecked(False)
        self.runbutton.setChecked(False)
        self.mdibutton2.setChecked(False)
        self.editbutton.setChecked(False)
        self.toolmeasbutton.setChecked(False)
        self.workoffbutton.setChecked(False)
        self.jogbutton.setChecked(True)        
        self.refrtnbutton.setChecked(False)

    def buttonrefrtnbutton(self):
     
        self.mesgbutton.setChecked(False)
        self.tooltblbutton.setChecked(False)
        self.runbutton.setChecked(False)
        self.mdibutton2.setChecked(False)
        self.editbutton.setChecked(False)
        self.toolmeasbutton.setChecked(False)
        self.workoffbutton.setChecked(False)
        self.jogbutton.setChecked(False)        
        self.refrtnbutton.setChecked(True)

    @Slot(QAbstractButton)
    def on_leftnavbuttons_buttonClicked(self, button):
        self.leftstack.setCurrentIndex(button.property('pageleft'))
        self.rightstack.setCurrentIndex(button.property('pageright'))
        self.jogstack.setCurrentIndex(button.property('pageupleft'))
    

 #   @Slot(QAbstractButton)
  #  def on_rightnavbuttons_buttonClicked(self, button):
   #     self.mainstack.setCurrentIndex(button.property('page'))
  #      self.leftstack.setCurrentIndex(button.property('pageleft'))
   #     self.jogstack.setCurrentIndex(button.property('pageupleft'))
        

   # @Slot(QAbstractButton)
    #def on_centernavbuttons_buttonClicked(self, button):
   #     self.mainstack.setCurrentIndex(button.property('page'))
   #     self.leftstack.setCurrentIndex(button.property('pageleft'))

   # @Slot(QAbstractButton)
    #def on_notifybutton_buttonClicked(self, button):
     #   self.leftstack.setCurrentIndex(button.property('pageleft'))
     #   self.rightstack.setCurrentIndex(button.property('pageright'))
      #  self.jogstack.setCurrentIndex(button.property('pageupleft'))



