# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.combo
import wx.html
import wx.richtext
import wx.adv
import wx.grid

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,471 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_splitter1 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_splitter1.Bind( wx.EVT_IDLE, self.m_splitter1OnIdle )

		self.m_panel2 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self.m_panel2, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button3, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer1 )
		self.m_panel2.Layout()
		bSizer1.Fit( self.m_panel2 )
		self.m_panel3 = wx.Panel( self.m_splitter1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_button4 = wx.Button( self.m_panel3, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer2 )
		self.m_panel3.Layout()
		bSizer2.Fit( self.m_panel3 )
		self.m_splitter1.SplitVertically( self.m_panel2, self.m_panel3, 0 )
		gSizer1.Add( self.m_splitter1, 1, wx.EXPAND, 5 )

		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_button14 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button14, 0, wx.ALL, 5 )

		self.m_button15 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button15, 0, wx.ALL, 5 )

		self.m_button16 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button16, 0, wx.ALL, 5 )

		self.m_button17 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button17, 0, wx.ALL, 5 )

		self.m_button18 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button18, 0, wx.ALL, 5 )

		self.m_button19 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button19, 0, wx.ALL, 5 )

		self.m_button20 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button20, 0, wx.ALL, 5 )

		self.m_button21 = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button21, 0, wx.ALL, 5 )


		self.m_scrolledWindow1.SetSizer( bSizer9 )
		self.m_scrolledWindow1.Layout()
		bSizer9.Fit( self.m_scrolledWindow1 )
		gSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( gSizer1 )
		self.Layout()
		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"New", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem1 )

		self.m_menu1.AppendSeparator()

		self.m_menu1.AppendSeparator()

		self.m_menuItem2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem2 )

		self.m_menu11 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem3 )

		self.m_menuItem4 = wx.MenuItem( self.m_menu11, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu11.Append( self.m_menuItem4 )

		self.m_menu1.AppendSubMenu( self.m_menu11, u"Help" )

		self.m_menubar1.Append( self.m_menu1, u"File" )

		self.m_menu2 = wx.Menu()
		self.m_menubar1.Append( self.m_menu2, u"About" )

		self.SetMenuBar( self.m_menubar1 )

		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_tool1 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"1.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.AddSeparator()

		self.m_tool2 = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"tool", wx.Bitmap( u"2.ico", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None )

		self.m_toolBar1.Realize()


		self.Centre( wx.BOTH )

	def __del__( self ):
		pass

	def m_splitter1OnIdle( self, event ):
		self.m_splitter1.SetSashPosition( 0 )
		self.m_splitter1.Unbind( wx.EVT_IDLE )


###########################################################################
## Class MyPanel1
###########################################################################

class MyPanel1 ( wx.Panel ):

	def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
		wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel10 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook2.AddPage( self.m_panel10, u"a page", False )
		self.m_panel11 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook2.AddPage( self.m_panel11, u"a page", False )
		self.m_panel12 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		self.m_button23 = wx.Button( self.m_panel12, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button23, 0, wx.ALL, 5 )


		self.m_panel12.SetSizer( bSizer11 )
		self.m_panel12.Layout()
		bSizer11.Fit( self.m_panel12 )
		self.m_notebook2.AddPage( self.m_panel12, u"a page", False )

		gSizer3.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_panel13 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		self.m_button24 = wx.Button( self.m_panel13, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button24, 0, wx.ALL, 5 )


		self.m_panel13.SetSizer( bSizer12 )
		self.m_panel13.Layout()
		bSizer12.Fit( self.m_panel13 )
		self.m_auinotebook1.AddPage( self.m_panel13, u"a page", False, wx.NullBitmap )
		self.m_panel14 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.m_panel14, u"a page", False, wx.NullBitmap )
		self.m_panel15 = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_auinotebook1.AddPage( self.m_panel15, u"a page", False, wx.NullBitmap )

		gSizer3.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_listbook1 = wx.Listbook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LB_DEFAULT )
		self.m_panel16 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_button25 = wx.Button( self.m_panel16, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer13.Add( self.m_button25, 0, wx.ALL, 5 )


		self.m_panel16.SetSizer( bSizer13 )
		self.m_panel16.Layout()
		bSizer13.Fit( self.m_panel16 )
		self.m_listbook1.AddPage( self.m_panel16, u"a page", True )
		self.m_panel17 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.m_panel17, u"a page", False )
		self.m_panel18 = wx.Panel( self.m_listbook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_listbook1.AddPage( self.m_panel18, u"a page", False )

		gSizer3.Add( self.m_listbook1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_choicebook1 = wx.Choicebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.CHB_DEFAULT )
		self.m_panel19 = wx.Panel( self.m_choicebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_choicebook1.AddPage( self.m_panel19, u"a page", False )
		self.m_panel20 = wx.Panel( self.m_choicebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		self.m_button26 = wx.Button( self.m_panel20, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button26, 0, wx.ALL, 5 )


		self.m_panel20.SetSizer( bSizer14 )
		self.m_panel20.Layout()
		bSizer14.Fit( self.m_panel20 )
		self.m_choicebook1.AddPage( self.m_panel20, u"a page", True )
		self.m_panel21 = wx.Panel( self.m_choicebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_choicebook1.AddPage( self.m_panel21, u"a page", False )
		gSizer3.Add( self.m_choicebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( gSizer3 )
		self.Layout()

	def __del__( self ):
		pass


###########################################################################
## Class MyDialog1
###########################################################################

class MyDialog1 ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer15 = wx.BoxSizer( wx.VERTICAL )


		self.SetSizer( bSizer15 )
		self.Layout()
		bSizer15.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,545 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_button27 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_button27, 0, wx.ALL, 5 )

		self.m_bpButton1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.m_bpButton1.SetBitmap( wx.Bitmap( u"1.ico", wx.BITMAP_TYPE_ANY ) )
		gSizer4.Add( self.m_bpButton1, 0, wx.ALL, 5 )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		gSizer4.Add( self.m_staticText1, 0, wx.ALL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"1.ico", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_bitmap1, 0, wx.ALL, 5 )

		m_comboBox1Choices = [ u"AAA", u"BBB", u"CCC" ]
		self.m_comboBox1 = wx.ComboBox( self, wx.ID_ANY, u"123", wx.DefaultPosition, wx.DefaultSize, m_comboBox1Choices, 0 )
		gSizer4.Add( self.m_comboBox1, 0, wx.ALL, 5 )

		self.m_bcomboBox1 = wx.combo.BitmapComboBox( self, wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, "", 0 )
		gSizer4.Add( self.m_bcomboBox1, 0, wx.ALL, 5 )

		m_choice1Choices = [ u"AAA", u"BBB" ]
		self.m_choice1 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0 )
		self.m_choice1.SetSelection( 0 )
		gSizer4.Add( self.m_choice1, 0, wx.ALL, 5 )

		m_listBox1Choices = [ u"aaa", u"bbb", u"ccc" ]
		self.m_listBox1 = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBox1Choices, 0 )
		gSizer4.Add( self.m_listBox1, 0, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_checkBox1, 0, wx.ALL, 5 )

		m_radioBox1Choices = [ u"AAAA", u"BBB", u"CCC", wx.EmptyString ]
		self.m_radioBox1 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox1.SetSelection( 0 )
		gSizer4.Add( self.m_radioBox1, 0, wx.ALL, 5 )


		self.SetSizer( gSizer4 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame3
###########################################################################

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_radioBtn2 = wx.RadioButton( self, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

		self.m_radioBtn3 = wx.RadioButton( self, wx.ID_ANY, u"RadioBtn", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_radioBtn3, 0, wx.ALL, 5 )

		m_radioBox3Choices = [ u"Radio Button" ]
		self.m_radioBox3 = wx.RadioBox( self, wx.ID_ANY, u"wxRadioBox", wx.DefaultPosition, wx.DefaultSize, m_radioBox3Choices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox3.SetSelection( 0 )
		fgSizer1.Add( self.m_radioBox3, 0, wx.ALL, 5 )

		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_slider1 = wx.Slider( self, wx.ID_ANY, 0, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		fgSizer1.Add( self.m_slider1, 0, wx.ALL, 5 )

		self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.m_gauge1.SetValue( 80 )
		fgSizer1.Add( self.m_gauge1, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,516 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_htmlWin1 = wx.html.HtmlWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.html.HW_SCROLLBAR_AUTO )
		gSizer5.Add( self.m_htmlWin1, 0, wx.ALL, 5 )

		self.m_richText1 = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
		gSizer5.Add( self.m_richText1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_toggleBtn1 = wx.ToggleButton( self, wx.ID_ANY, u"Toggle me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_toggleBtn1, 0, wx.ALL, 5 )

		self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_searchCtrl1.ShowSearchButton( True )
		self.m_searchCtrl1.ShowCancelButton( True )
		gSizer5.Add( self.m_searchCtrl1, 0, wx.ALL, 5 )

		self.m_colourPicker1 = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.Colour( 100, 239, 92 ), wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gSizer5.Add( self.m_colourPicker1, 0, wx.ALL, 5 )

		self.m_fontPicker1 = wx.FontPickerCtrl( self, wx.ID_ANY, wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微軟正黑體" ), wx.DefaultPosition, wx.DefaultSize, wx.FNTP_DEFAULT_STYLE )
		self.m_fontPicker1.SetMaxPointSize( 100 )
		gSizer5.Add( self.m_fontPicker1, 0, wx.ALL, 5 )

		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, u"C:\\Users\\user\\Documents\\python\\2020-11-05.py", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		gSizer5.Add( self.m_filePicker1, 0, wx.ALL, 5 )

		self.m_dirPicker1 = wx.DirPickerCtrl( self, wx.ID_ANY, u"C:\\Users\\user\\Documents\\python\\hw", u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gSizer5.Add( self.m_dirPicker1, 0, wx.ALL, 5 )

		self.m_datePicker1 = wx.adv.DatePickerCtrl( self, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT )
		gSizer5.Add( self.m_datePicker1, 0, wx.ALL, 5 )


		self.SetSizer( gSizer5 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame5
###########################################################################

class MyFrame5 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_scrollBar1 = wx.ScrollBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_HORIZONTAL )
		gSizer6.Add( self.m_scrollBar1, 0, wx.ALL, 5 )

		self.m_spinCtrl1 = wx.SpinCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 8 )
		gSizer6.Add( self.m_spinCtrl1, 0, wx.ALL, 5 )

		self.m_spinCtrlDouble1 = wx.SpinCtrlDouble( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 3.000000, 1 )
		self.m_spinCtrlDouble1.SetDigits( 0 )
		gSizer6.Add( self.m_spinCtrlDouble1, 0, wx.ALL, 5 )

		self.m_spinBtn1 = wx.SpinButton( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_spinBtn1, 0, wx.ALL, 5 )

		self.m_hyperlink1 = wx.adv.HyperlinkCtrl( self, wx.ID_ANY, u"test", u"http://teaching.bo-yuan.net/", wx.DefaultPosition, wx.DefaultSize, wx.adv.HL_DEFAULT_STYLE )
		gSizer6.Add( self.m_hyperlink1, 0, wx.ALL, 5 )

		self.m_genericDirCtrl1 = wx.GenericDirCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.DIRCTRL_3D_INTERNAL|wx.SUNKEN_BORDER, wx.EmptyString, 0 )

		self.m_genericDirCtrl1.ShowHidden( False )
		gSizer6.Add( self.m_genericDirCtrl1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_treeCtrl1 = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
		gSizer6.Add( self.m_treeCtrl1, 0, wx.ALL, 5 )

		self.m_grid1 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid1.CreateGrid( 5, 5 )
		self.m_grid1.EnableEditing( True )
		self.m_grid1.EnableGridLines( True )
		self.m_grid1.EnableDragGridSize( False )
		self.m_grid1.SetMargins( 0, 0 )

		# Columns
		self.m_grid1.EnableDragColMove( False )
		self.m_grid1.EnableDragColSize( True )
		self.m_grid1.SetColLabelSize( 30 )
		self.m_grid1.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid1.EnableDragRowSize( True )
		self.m_grid1.SetRowLabelSize( 80 )
		self.m_grid1.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid1.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		gSizer6.Add( self.m_grid1, 0, wx.ALL, 5 )


		self.SetSizer( gSizer6 )
		self.Layout()
		self.m_timer1 = wx.Timer()
		self.m_timer1.SetOwner( self, wx.ID_ANY )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class MyFrame6
###########################################################################

class MyFrame6 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer16 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid3 = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 5, 5 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer16.Add( self.m_grid3, 0, wx.ALL, 5 )

		m_checkList2Choices = [u"aaa", u"bbb", u"ccc"]
		self.m_checkList2 = wx.CheckListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList2Choices, 0 )
		bSizer16.Add( self.m_checkList2, 0, wx.ALL, 5 )


		self.SetSizer( bSizer16 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


