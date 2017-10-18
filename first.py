
import wx
class FirstFrame(wx.Frame):



    def __init__(self,*args,**kw):
        super(FirstFrame, self).__init__(*args,**kw, size=(500,600))
        

        self.lnitUI()
        self.Centre()
        self.Show()

    def lnitUI(self):

    	pnl=wx.Panel(self)
    	self.Apply={}
    	

    	st=wx.StaticText(pnl, label="Survey about Students", pos=(110,25))
    	font=st.GetFont()
    	font.PointSize +=10
    	font=font.Bold()
    	st.SetFont(font)


    	QT1=wx.StaticText(pnl, label="Q1. What's your major?", pos=(25,120))
    	fontQ1=QT1.GetFont()
    	fontQ1.PointSize +=5
    	fontQ1=fontQ1.Bold()
    	QT1.SetFont(fontQ1)
    	
    	
    	self.tc=wx.TextCtrl(pnl, pos=(50, 170), size=(400,25))
    	self.tc.Bind(wx.EVT_TEXT, self.Q1Answer)
    	
    	QT2=wx.StaticText(pnl, label="Q2. What's your name?", pos=(25,200))
    	QT2.SetFont(fontQ1)

    	self.tc2=wx.TextCtrl(pnl, pos=(50, 250), size=(400,25))
    	self.tc2.Bind(wx.EVT_TEXT, self.Q2Answer)
    	
    	QT3=wx.StaticText(pnl, label="Q3. Selet your grade", pos=(25, 300))
    	QT3.SetFont(fontQ1)

    	self.Q3b1=wx.RadioButton(pnl, label="1'st grade", pos=(50, 340))
    	self.Q3b2=wx.RadioButton(pnl, label="2'nd grade", pos=(150, 340))
    	self.Q3b3=wx.RadioButton(pnl, label="3'rd grade", pos=(250, 340))
    	self.Q3b4=wx.RadioButton(pnl, label="4'th grade", pos=(350, 340))

    	self.Q3b1.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
    	self.Q3b2.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
    	self.Q3b3.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
    	self.Q3b4.Bind(wx.EVT_RADIOBUTTON, self.SetVal)


    	self.button1=wx.Button(pnl, label="Next", pos=(200, 400))
    	self.button1.Bind(wx.EVT_BUTTON, self.Next)


    	self.makeMenuBar()

    	self.CreateStatusBar()
    	self.SetStatusText("Welcme to Our Analysis!")

    def makeMenuBar(self):
    	fileMenu=wx.Menu()
    	helloItem=fileMenu.Append(-1, "&Hello...\tCtrl-H")
    	fileMenu.AppendSeparator()
    	exitItem=fileMenu.Append(wx.ID_EXIT)
    	helpMenu=wx.Menu()
    	aboutItem=helpMenu.Append(wx.ID_ABOUT)

    	menuBar=wx.MenuBar()
    	menuBar.Append(fileMenu, "&File")
    	menuBar.Append(helpMenu, "&Help")

    	self.SetMenuBar(menuBar)

    	self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
    	self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
    	self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

    def OnExit(self, event):
    	self.Close(True)

    def OnHello(self, event):
    	wx.MessageBox("Thank you for your help")

    def OnAbout(self, event):
    	wx.MessageBox("This is a sample survey form", "About Our survey",
    		wx.OK|wx.ICON_INFORMATION)

    def SetVal(self, event):
    	state1= self.Q3b1.GetValue()
    	state2= self.Q3b2.GetValue()
    	state3= self.Q3b3.GetValue()
    	state4= self.Q3b4.GetValue()
    	if state1==True:
    		self.Apply['grade']="1'st grade"
    	elif state2==True:
    		self.Apply['grade']="2'nd grade"
    	elif state3==True:
    		self.Apply['grade']="3'rd grade"
    	else:
    		self.Apply['grade']="4'th grade"
    	 

    def Q1Answer(self,event):
    	self.Apply['major']= str(self.tc.GetValue())
    	

    def Q2Answer(self,event):
    	self.Apply['name']= str(self.tc2.GetValue())

    def Next(self, event):
    	
    	print(self.Apply)
    	self.Close()

    	SecondFrame(None, title='Survey form')
    	
    


class SecondFrame(wx.Frame):

	def __init__(self,*args,**kw):
		super(SecondFrame, self).__init__(*args,**kw, size=(500,600))
		self.lnitUI()
		self.Centre()
		self.Show()

	def lnitUI(self):
		pnl=wx.Panel(self)


		vbox=wx.BoxSizer(wx.VERTICAL)
		tc1=wx.TextCtrl(pnl, pos=(1, 1), size=(0,0)) 



		st=wx.StaticText(pnl, label="Survey about Students", pos=(110,25))
		font=st.GetFont()
		font.PointSize +=10
		font=font.Bold()
		st.SetFont(font)

		hbox1=wx.BoxSizer(wx.HORIZONTAL)
		QT4=wx.StaticText(pnl, label="Q4. What did you do in summer vacation?")
		fontQ4=QT4.GetFont()
		fontQ4.PointSize +=5
		fontQ4=fontQ4.Bold()
		QT4.SetFont(fontQ4)
		hbox1.Add(QT4, 0, flag=wx.LEFT, border=25)
		vbox.Add(hbox1, 0, flag=wx.TOP, border=120)
		

		
		hbox2=wx.BoxSizer(wx.HORIZONTAL)
		self.Q4c1=wx.RadioButton(pnl, label="Study")
		self.Q4c2=wx.RadioButton(pnl, label="Exercise")
		self.Q4c3=wx.RadioButton(pnl, label="Travel")
		self.Q4c4=wx.RadioButton(pnl, label="Experiment")

		hbox2.Add(self.Q4c1, flag=wx.LEFT, border=50)
		hbox2.Add(self.Q4c2, flag=wx.LEFT, border=50)
		hbox2.Add(self.Q4c3, flag=wx.LEFT, border=50)
		hbox2.Add(self.Q4c4, flag=wx.LEFT, border=50)
		vbox.Add(hbox2, flag=wx.TOP, border=20)
		
		

		self.Q4c1.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
		self.Q4c2.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
		self.Q4c3.Bind(wx.EVT_RADIOBUTTON, self.SetVal)
		self.Q4c4.Bind(wx.EVT_RADIOBUTTON, self.SetVal)

		

		

		hbox3=wx.BoxSizer(wx.HORIZONTAL)
		button2=wx.Button(pnl, label="Back")
		button2.Bind(wx.EVT_BUTTON, self.Back)
		hbox3.Add(button2, flag=wx.LEFT, border=140)

		button3=wx.Button(pnl, label="Submit")
		button3.Bind(wx.EVT_BUTTON, self.Submit)
		hbox3.Add(button3, flag=wx.LEFT, border=20)

		vbox.Add(hbox3, flag=wx.TOP, border=100)
		pnl.SetSizer(vbox)



		self.makeMenuBar()
		self.CreateStatusBar()
		self.SetStatusText("Welcme to Our Analysis!")



	def SetVal(self, event):

		state1= self.Q4c1.GetValue()
		state2= self.Q4c2.GetValue()
		state3= self.Q4c3.GetValue()
		state4= self.Q4c4.GetValue()

		if state1==True:
			self.result=1
			
		elif state2==True:
			self.result=2
		elif state3==True:
			self.result=3
		elif state4==True:
			self.result=4
	


	def Back(self, event):
		self.Close(True)
		frm=FirstFrame(None, title='Survey form')
		

	def Submit(self, event):
		self.Close(True)
		wx.MessageBox("Thank you for your help")



	

	def makeMenuBar(self):
		fileMenu=wx.Menu()
		helloItem=fileMenu.Append(-1, "&Hello...\tCtrl-H")
		fileMenu.AppendSeparator()
		exitItem=fileMenu.Append(wx.ID_EXIT)
		helpMenu=wx.Menu()
		aboutItem=helpMenu.Append(wx.ID_ABOUT)

		menuBar=wx.MenuBar()
		menuBar.Append(fileMenu, "&File")
		menuBar.Append(helpMenu, "&Help")

		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.OnHello, helloItem)
		self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
		self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)

	def OnExit(self, event):
		self.Close(True)

	def OnHello(self, event):
		wx.MessageBox("Thank you for your help")

	def OnAbout(self, event):
		wx.MessageBox("This is a sample survey form", "About Our survey",
			wx.OK|wx.ICON_INFORMATION)




def main():

	
	app=wx.App()
	frm=FirstFrame(None, title='Survey form')
	frm.Show()
	app.MainLoop()


if __name__ == '__main__':

	main()



    

    








