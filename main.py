import wx
from wx.core import Size






if __name__=='__main__':
    app = wx.App()
    #Frame
    frm = wx.Frame(None,title='Pert 1',size = (400,400))
    panel=wx.Panel(frm)
    label = wx.StaticText(panel,label='Hello',pos=(170,100)) #Static (Absolute)
    frm.Show()
    app.MainLoop()