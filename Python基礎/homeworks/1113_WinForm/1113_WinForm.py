# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext
import os

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		self.currentpath=os.getcwd()
		self.currentfile="未命名.txt"
		self.isnew=True
		self.isedited=False
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"未命名.txt", pos = wx.DefaultPosition, size = wx.Size( 626,419 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.option_newfile = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"建立新檔", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.option_newfile )

		self.option_openfile = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"開啟舊檔", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.option_openfile )

		self.m_menu1.AppendSeparator()

		self.option_savefile = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.option_savefile )

		self.m_menu1.AppendSeparator()

		self.option_exit = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"結束程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.option_exit )

		self.m_menubar1.Append( self.m_menu1, u"功能" )

		self.m_menu2 = wx.Menu()
		self.option_aboutthis = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"關於本程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.option_aboutthis.SetBitmap( wx.NullBitmap )
		self.m_menu2.Append( self.option_aboutthis )

		self.m_menubar1.Append( self.m_menu2, u"關於" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.notepadtextarea = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		bSizer1.Add( self.notepadtextarea, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.newOpen, id = self.option_newfile.GetId() )
		self.Bind( wx.EVT_MENU, self.outOpen, id = self.option_openfile.GetId() )
		self.Bind( wx.EVT_MENU, self.outSave, id = self.option_savefile.GetId() )
		self.Bind( wx.EVT_MENU, self.theExit, id = self.option_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.msgAboutthis, id = self.option_aboutthis.GetId() )
		self.notepadtextarea.Bind( wx.EVT_TEXT, self.textchange )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def newOpen( self, event ): #建立新檔
		self.notepadtextarea.Value=""
		self.currentpath=os.getcwd()
		self.currentfile="未命名.txt"
		self.Title=self.currentfile
		self.isnew=True
		self.isedited=False
		pass

	def outOpen( self, event ): #開啟舊檔
		txtfilepath_=wx.FileSelector(
			"開啟舊檔",
			wildcard="*.txt",
			flags=wx.FD_OPEN
		)
		if txtfilepath_:
			i_=txtfilepath_.rfind('\\')+1
			self.currentpath=txtfilepath_[:i_]
			self.currentfile=txtfilepath_[i_:]
			self.Title=self.currentfile
			with open(txtfilepath_,mode='r',encoding='utf-8') as txtfile_:
				self.notepadtextarea.Value=txtfile_.read()
			self.isnew=False
			self.isedited=False
			pass

	def outSave( self, event ): #儲存檔案
		if self.isnew:
			name_="未命名"
			while(os.path.exists(self.currentpath+name_+".txt")):
				name_+="(1)"
			txtfilepath_=wx.FileSelector(
				"儲存檔案",
				wildcard=name_+"txt",
				flags=wx.FD_SAVE
			)
			if txtfilepath_:
				i_=txtfilepath_.rfind('\\')+1
				self.currentpath=txtfilepath_[:i_]
				self.currentfile=txtfilepath_[i_:]
				txtfilepath_=txtfilepath_.replace('*','')
				with open(txtfilepath_,mode='w',encoding='utf-8') as txtfile_:
					txtfile_.write(self.notepadtextarea.Value)
				self.Title=self.currentfile
				self.isnew=False
				self.isedited=False
		elif self.isedited:
			txtfilepath_=self.currentpath+self.currentfile
			txtfilepath_=txtfilepath_.replace('*','')
			with open(txtfilepath_,mode='w',encoding='utf-8') as txtfile_:
				txtfile_.write(self.notepadtextarea.Value)
			self.Title=self.currentfile
			self.isnew=False
			self.isedited=False			
		else:
			return
		pass

	def theExit( self, event ): #結束程式
		exit()
		pass

	def textchange( self, event ): #結束程式
		if self.isedited==False:
			self.Title='*'+self.Title
			self.isedited=True
		pass

	def msgAboutthis( self, event ):
		Msg_=dialog_aboutthis(self)
		Msg_.ShowModal()
		Msg_.Destroy()
		pass


###########################################################################
## Class dialog_aboutthis
###########################################################################

class dialog_aboutthis ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"關於本程式", pos = wx.DefaultPosition, size = wx.Size( 200,120 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		STRaboutthis="\nsvwriting(01蘇煜㭿)：\n毫無反應，就只是個筆記本。"
		self.msg_aboutthis = wx.richtext.RichTextCtrl( self, wx.ID_ANY, STRaboutthis, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		self.msg_aboutthis.Enable( False )
		bSizer2.Add( self.msg_aboutthis, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



###########################################################################
## 
###########################################################################

app = wx.App() 
main_win = MainFrame(None)
main_win.Show()
app.MainLoop()