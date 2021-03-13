import wx
from wx.core import HORIZONTAL

class Panel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent)

        nama_sizer = wx.BoxSizer(wx.HORIZONTAL)
        nama_label = wx.StaticText(self,label = 'Nama : ')
        self.nama = wx.StaticText(self,label = 'Adwitya Sadhu Prayastita')
        nama_sizer.Add(nama_label,5,wx.ALL|wx.Center,5)
        nama_sizer.Add(self.nama,0,wx.ALL,5)

        nim_sizer = wx.BoxSizer(wx.HORIZONTAL)
        nim_label = wx.StaticText(self,label = 'NIM : ')
        self.nim = wx.StaticText(self,label = '192410101054')
        nim_sizer.Add(nim_label,5,wx.ALL|wx.Center,5)
        nim_sizer.Add(self.nim,0,wx.ALL,5)

        greet_sizer = wx.BoxSizer(wx.HORIZONTAL)
        greet_label = wx.StaticText(self,label = 'HELLO WX!!!')
        greet_sizer.Add(greet_label,5,wx.ALL|wx.Center,5)

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(nama_sizer, 0, wx.ALL, 5)
        main_sizer.Add(nim_sizer, 0, wx.ALL, 5)
        main_sizer.Add(greet_sizer, 0, wx.ALL, 5)


        self.SetSizer(main_sizer)


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None, title = 'Tugas 1 PBO II',size = (400,400))
        panel = Panel(self)
        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    app.MainLoop()