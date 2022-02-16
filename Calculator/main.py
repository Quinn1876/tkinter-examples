"""
Written By Quinn Hodges
With Help from Alishba Naseer
"""

from tkinter import *

class Calculator(Frame):
      
      def __init__(self, master=None):
            Frame.__init__(self, master)
            ########################### CLASS FIELDS ##########################
            self.cache = None
            self.operator = ''
            self.master = master
            self.display_StringVar = StringVar()
            self.display_text = '0'
            self.display_StringVar.set('0')
            self.equalsPressed = False
            
            ########################## FRAME ELEMENTS #########################
            self.display = Label(master=self.master, textvariable=self.display_StringVar)
            self.row_1 = Frame(master=self.master)
            self.row_2 = Frame(master=self.master)
            self.row_3 = Frame(master=self.master)
            self.row_4 = Frame(master=self.master)
            self.row_5 = Frame(master=self.master)
            
            ############################ ROW 1 ################################
            self.button_1 = Button(master=self.row_1, text='1', command=self.addOneDisplay)
            self.button_2 = Button(master=self.row_1, text='2', command=self.addTwoDisplay)
            self.button_3 = Button(master=self.row_1, text='3', command=self.addThreeDisplay)
            self.button_pls = Button(master=self.row_1, text='+', command=self.plus)
            
            ############################ ROW 2 ################################
            self.button_4 = Button(master=self.row_2, text='4', command=self.addFourDisplay)
            self.button_5 = Button(master=self.row_2, text='5', command=self.addFiveDisplay)
            self.button_6 = Button(master=self.row_2, text='6', command=self.addSixDisplay)
            self.button_sub = Button(master=self.row_2, text=' -', command=self.minus)
            
            ############################ ROW 3 ################################
            self.button_7 = Button(master=self.row_3, text='7', command=self.addSevenDisplay)
            self.button_8 = Button(master=self.row_3, text='8', command=self.addEightDisplay)
            self.button_9 = Button(master=self.row_3, text='9', command=self.addNineDisplay)
            self.button_mul = Button(master=self.row_3, text=' *', command=self.multiply)
            
            ############################ ROW 4 ################################
            self.button_0 = Button(master=self.row_4, text='0', command=self.addZeroDisplay)            
            self.button_div = Button(master=self.row_4, text=' /', command=self.divide)
            self.button_eql = Button(master=self.row_4, text='   =  ', command=self.equals)
            
            ############################ ROW 5 ################################
            self.button_clear = Button(master=self.row_5, text='clear', command=self.clear)
            
            ########################## Packing ################################
            self.display.pack(side=TOP)
            self.row_1.pack(side=TOP)
            self.row_2.pack(side=TOP)
            self.row_3.pack(side=TOP)
            self.row_4.pack(side=TOP)       
            self.row_5.pack(side=TOP)       
            
            self.button_pls.pack(side=LEFT)
            self.button_sub.pack(side=LEFT)
            self.button_div.pack(side=LEFT)
            self.button_mul.pack(side=LEFT)
            self.button_0.pack(side=LEFT)
            self.button_eql.pack(side=LEFT)
            self.button_1.pack(side=LEFT)
            self.button_2.pack(side=LEFT)
            self.button_3.pack(side=LEFT)
            self.button_4.pack(side=LEFT)
            self.button_5.pack(side=LEFT)
            self.button_6.pack(side=LEFT)
            self.button_7.pack(side=LEFT)
            self.button_8.pack(side=LEFT)
            self.button_9.pack(side=LEFT)
            self.button_clear.pack(side=LEFT)
            
      ####################### CLASS METHODS ###################################
      def addZeroDisplay(self):
            if self.equalsPressed:
                  self.clear()
                  
            if self.display_text != '0':
                  self.display_text += '0'
                  self.display_StringVar.set(self.display_text)
            
      def addOneDisplay(self):
            if self.equalsPressed:
                  self.clear()
                  
            if self.display_text == '0':
                  self.display_text=''
            
            self.display_text += '1'
            self.display_StringVar.set(self.display_text)
            
      def addTwoDisplay(self):
            if self.equalsPressed:
                  self.clear()
            
            if self.display_text == '0':
                  self.display_text=''
                  
            self.display_text += '2'
            self.display_StringVar.set(self.display_text)
            
      def addThreeDisplay(self):
            if self.equalsPressed:
                  self.clear()
            
            if self.display_text == '0':
                  self.display_text=''
                  
            self.display_text += '3'
            self.display_StringVar.set(self.display_text)
            
      def addFourDisplay(self):
            if self.equalsPressed:
                  self.clear()
                  
            if self.display_text == '0':
                  self.display_text=''
                  
            self.display_text += '4'
            self.display_StringVar.set(self.display_text)
            
      def addFiveDisplay(self):
            if self.equalsPressed:
                  self.clear()
                  
            if self.display_text == '0':
                  self.display_text=''
                  
            self.display_text += '5'
            self.display_StringVar.set(self.display_text)
            
      def addSixDisplay(self):
            if self.equalsPressed:
                  self.clear()
                  
            if self.display_text == '0':
                  self.display_text=''
                  
            self.display_text += '6'
            self.display_StringVar.set(self.display_text)
            
      def addSevenDisplay(self):
            if self.equalsPressed:
                  self.clear()
                  
            if self.display_text == '0':
                  self.display_text=''
                  
            self.display_text += '7'
            self.display_StringVar.set(self.display_text)
            
      def addEightDisplay(self):
            if self.equalsPressed:
                  self.clear()
                  
            if self.display_text == '0':
                  self.display_text=''
                  
            self.display_text += '8'
            self.display_StringVar.set(self.display_text)
            
      def addNineDisplay(self):
            if self.equalsPressed:
                  self.clear()
                  
            if self.display_text == '0':
                  self.display_text=''
                  
            self.display_text += '9'
            self.display_StringVar.set(self.display_text)
            
      def plus(self):
            if self.equalsPressed:
                  self.clear()
            else:      
                  self.evaluateOperator()
                  self.operator = '+'
            
      def minus(self):
            if self.equalsPressed:
                  self.clear()
            else:
                  self.evaluateOperator()
                  self.operator = '-'
            
      def divide(self):
            if self.equalsPressed:
                  self.clear()
            else:
                  self.evaluateOperator()
                  self.operator = '/'
            
      def multiply(self):
            if self.equalsPressed:
                  self.clear()
            else:
                  self.evaluateOperator()
                  self.operator = '*'
            
      def equals(self):
            if self.equalsPressed:
                  self.clear()
            else:
                  self.evaluateOperator()
                  self.equalsPressed = True
                  self.display_text = str(self.cache)
                  self.display_StringVar.set(self.display_text)
            
      def clear(self):
            self.display_text = '0'
            self.display_StringVar.set(self.display_text)
            self.cache = None
            self.operator = ''
            self.equalsPressed = False
            
            
      def evaluateOperator(self):
            if self.operator == '':
                  self.cache = int(self.display_text)
            elif self.operator == '+':
                  assert self.cache != None
                  self.cache += int(self.display_text)
            elif self.operator == '-':
                  assert self.cache != None
                  self.cache -= int(self.display_text)
            elif self.operator == '/':
                  assert self.cache != None
                  self.cache /= int(self.display_text)
            elif self.operator == '*':
                  assert self.cache != None
                  self.cache *= int(self.display_text)

            self.display_text = '0'
            self.display_StringVar.set(self.display_text)

if __name__ == "__main__":
      app = Tk()
      main = Calculator(app)
      
      app.mainloop()