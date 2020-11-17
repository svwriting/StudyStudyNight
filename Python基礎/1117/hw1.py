# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"記事本", pos = wx.DefaultPosition, size = wx.Size( 475,270 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"建立檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"開啟檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"儲存檔案", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"關閉程式", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem4 )

		self.m_menubar1.Append( self.m_menu1, u"檔案" )

		self.m_menu2 = wx.Menu()
		self.m_menuItem5 = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"作者介紹", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.m_menuItem5 )

		self.m_menubar1.Append( self.m_menu2, u"關於" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 99999,99999 ), wx.TE_MULTILINE )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.createFile, id = self.m_menuItem1.GetId() )
		self.Bind( wx.EVT_MENU, self.openFile, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.saveFile, id = self.m_menuItem3.GetId() )
		self.Bind( wx.EVT_MENU, self.closeWindows, id = self.m_menuItem4.GetId() )
		self.Bind( wx.EVT_MENU, self.authorIntro, id = self.m_menuItem5.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def createFile( self, event ):
		event.Skip()

	def openFile( self, event ):
		event.Skip()

	def saveFile( self, event ):
		event.Skip()

	def closeWindows( self, event ):
		event.Skip()

	def authorIntro( self, event ):
		event.Skip()


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 243,105 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"作者介紹....", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


