import sys
import gi,os
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
import os.path


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.a=Adw.Leaflet(fold_threshold_policy=True,can_navigate_back=True,can_navigate_forward=True)
        self.set_titlebar(Gtk.Box())
        #Left Box
        self.l=Gtk.Box(hexpand_set=True)
        self.b=Gtk.Separator()
        self.lp=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,hexpand=True)
        self.lh=Adw.HeaderBar()
        self.lp.append(self.lh)
        self.l.append(self.lp)
        self.l.append(self.b)
        #Right Box
        self.r=Gtk.Box(orientation=Gtk.Orientation.VERTICAL,hexpand=True)
        self.rh=Adw.HeaderBar()
        self.r.append(self.rh)
        #Append
        self.set_child(self.a)
        self.a.append(self.l)
        self.a.append(self.r)
        #Connect
        self.a.connect("notify::folded",self.e)
        self.e()
    def e(self,*data):
        if(self.a.get_folded()):
            self.lh.set_show_end_title_buttons(True)
            self.rh.set_show_start_title_buttons(True)
            self.b.set_visible(False)
        else:
            self.lh.set_show_end_title_buttons(False)
            self.rh.set_show_start_title_buttons(False)
            self.b.set_visible(True)

class Main(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=self)
        self.win.present()

def main(version):
    app = Main()
    app.run(sys.argv)

if __name__ == '__main__':
    main(None)
