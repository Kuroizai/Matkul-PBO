import wx





class Log(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self,None,title='Login First!',size=(400,400))
        self.auth = False

        id_sizer = wx.BoxSizer(wx.VERTICAL)
        id_label = wx.StaticText(self,label = 'ID')
        self.id = wx.TextCtrl(self)
        id_sizer.Add(id_label,5,wx.ALL|wx.Center,5)
        id_sizer.Add(self.id,0,wx.ALL,5)


        pw_sizer = wx.BoxSizer(wx.VERTICAL)
        pw_label = wx.StaticText(self,label = 'PW')
        self.pw = wx.TextCtrl(self,style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        self.pw.Bind(wx.EVT_TEXT_ENTER,self.Login)
        pw_sizer.Add(pw_label,0,wx.ALL|wx.Center,5)
        pw_sizer.Add(self.pw,0,wx.ALL,5)


        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(id_sizer, 0, wx.ALL, 5)
        main_sizer.Add(pw_sizer, 0, wx.ALL, 5)
 
        btn = wx.Button(self, label="Login")
        btn.Bind(wx.EVT_BUTTON, self.Login)
        main_sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
 
        self.SetSizer(main_sizer)


    def Login(self,event):
        true_pw = 'admin'
        u_pass = self.pw.GetValue()
        if u_pass == true_pw:
            self.auth=True
            self.Close()

class Panel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent)


class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,title='SIAP V3',size=(800,800))
        panel = Panel(self)

        #Login Command

        log = Log()
        log.ShowModal()
        auth=log.auth
        if auth == False:
            self.Close()


        self.Show()


if __name__=="__main__":
    app = wx.App()
    frm = Main()
    app.MainLoop()