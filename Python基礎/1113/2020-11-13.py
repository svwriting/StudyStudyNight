import wx
import wx.xrc
import mywindows2
import codecs

class mywin2(mywindows2.MyFrame7):
	# status=False
	i=2
	def xxx( self, event ):
		self.i=(self.i%2)+1
		print(self.i)
		with codecs.open(str(self.i)+".ico","rb") as f:
			self.m_bitmap2.SetBitmap(wx.Bitmap(wx.Image(f,wx.BITMAP_TYPE_ICO)))
	
	def click1( self, event ):
		file=wx.FileSelector(
			"請選擇檔案",
			wildcard="Python檔案|*.py",
			flags=wx.FD_OPEN
		)
		self.m_textCtrl2.SetValue(file)
		# global w2
		# self.m_timer2.Start(3000)
		# self.m_textCtrl2.Enabled=False
		# wx.MessageBox("test")
		# self.m_staticText2.SetLabel("123")
		# wx.MessageBox(str(self.m_checkBox2.GetValue()))
		# self.m_choice2.Clear()
		# wx.MessageBox(str(self.m_choice2.GetSelection()))
		# wx.MessageBox(str(self.m_filePicker2.GetPath()))
		# self.m_hyperlink2.SetURL("https://www.google.com/")

		# self.m_grid4.AppendCols(7)
		# self.m_grid4.AppendRows(7)
		# self.m_grid4.SetColLabelValue(0,"ABC")
		# self.m_grid4.SetRowLabelValue(1,"999")
		# self.m_grid4.SetCellValue(0,0,"zzzzz")
		# self.m_grid4.SetSize(500,300)
		# if self.status==False:
		# 	w2.Show()
		# 	self.status=True
		# else:
		# 	w2.Hide()
		# 	self.status=False

p=wx.App()
w=mywin2(None)
w.Show()
w.SetTitle("123")
# w2=mywindows2.MyFrame8(None)
# for i in range(1,10,1):
# 	w.m_choice2.Append(str(i))
	

p.MainLoop()
