import hw1
import wx
import codecs
import os

class MyWindows(hw1.MyFrame1):
	fn=""
	def createFile( self, event ):
		self.fn=""
		self.m_textCtrl1.SetValue("")
		self.SetTitle("記事本")

	def openFile( self, event ):
		self.fn=wx.FileSelector(
			"請選擇要開啟的檔案",
			wildcard="文字檔|*.txt",
			flags=wx.FD_OPEN
		)
		if self.fn!="":
			with codecs.open(self.fn,"r","utf8") as f:
				self.m_textCtrl1.SetValue(f.read())
			self.SetTitle("記事本 - "+os.path.basename(self.fn))

	def saveFile( self, event ):
		if self.fn=="":
			self.fn=wx.FileSelector(
				"請選擇要儲存的檔案",
				wildcard="文字檔|*.txt",
				flags=wx.FD_SAVE
			)
		if self.fn!="":
			with codecs.open(self.fn,"w","utf8") as f:
				f.write(self.m_textCtrl1.GetValue())
			self.SetTitle("記事本 - "+os.path.basename(self.fn))

	def closeWindows( self, event ):
		wx.Exit()

	def authorIntro( self, event ):
		w1=hw1.MyDialog1(None)
		w1.Show()


p=wx.App()
w=MyWindows(None)
w.Show()
p.MainLoop()
