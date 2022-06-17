import gi
import sys

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hb=Adw.HeaderBar()
        self.set_titlebar(self.hb)

        a=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        b=Adw.ViewStack(vexpand=True)
        a.append(b)

        b.add_titled(Gtk.Label(label="XOX"),"xox","Xox")
        b.add_titled(Gtk.Label(label="LOL"),"lol","Lol")

        self.d.set_stack(b)
        self.d.set_title("LOL")
        self.hb.set_title_widget(self.d)

        self.c=Adw.ViewSwitcherBar()
        self.c.set_stack(b)
        self.c.set_reveal(True)
        a.append(self.c)

        self.set_child(a)
        self.d.connect("notify::title-visible",self.f)

    def f(self,*data):
        if self.d.get_title_visible():
            self.c.set_reveal(True)
        else:
            self.c.set_reveal(False)
class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


def main(version):
    app = MyApp()
    return app.run(sys.argv)

if __name__=='__main__':
    main(None)
