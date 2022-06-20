import sys
import gi,os
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
import os.path


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(520, 260)
        a=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        b=Adw.Carousel()
        d1=Gtk.Box(css_classes=["card"],margin_top=20,margin_start=20,margin_bottom=20,margin_end=20,orientation=Gtk.Orientation.VERTICAL)
        d1.append(Gtk.Image(icon_name="weather-overcast-symbolic",icon_size=Gtk.IconSize.LARGE,margin_top=30,margin_start=120,margin_bottom=10,margin_end=120))
        d1.append(Gtk.Label(label="Carousel",margin_start=120,margin_bottom=30,margin_end=120))
        b.append(d1)
        d2=Gtk.Box(css_classes=["card"],margin_top=20,margin_start=20,margin_bottom=20,margin_end=20,orientation=Gtk.Orientation.VERTICAL)
        d2.append(Gtk.Image(icon_name="location-services-active-symbolic",icon_size=Gtk.IconSize.LARGE,margin_top=30,margin_start=120,margin_bottom=10,margin_end=120))
        d2.append(Gtk.Label(label="LibAdwaita",margin_start=120,margin_bottom=30,margin_end=120))
        b.append(d2)
        d3=Gtk.Box(css_classes=["card"],margin_top=20,margin_start=20,margin_bottom=20,margin_end=20,orientation=Gtk.Orientation.VERTICAL)
        d3.append(Gtk.Image(icon_name="emoji-people-symbolic",icon_size=Gtk.IconSize.LARGE,margin_top=30,margin_start=120,margin_bottom=10,margin_end=120))
        d3.append(Gtk.Label(label="Python",margin_start=120,margin_bottom=30,margin_end=120))
        b.append(d3)
        d4=Gtk.Box(css_classes=["card"],margin_top=20,margin_start=20,margin_bottom=20,margin_end=20,orientation=Gtk.Orientation.VERTICAL)
        d4.append(Gtk.Image(icon_name="emblem-favorite-symbolic",icon_size=Gtk.IconSize.LARGE,margin_top=30,margin_start=120,margin_bottom=10,margin_end=120))
        d4.append(Gtk.Label(label="Example",margin_start=120,margin_bottom=30,margin_end=120))
        b.append(d4)

        a.append(b)
        c=Adw.CarouselIndicatorDots()
        a.append(c)
        c.set_carousel(b)

        e=Adw.CarouselIndicatorLines()
        a.append(e)
        e.set_carousel(b)

        self.set_child(a)

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
