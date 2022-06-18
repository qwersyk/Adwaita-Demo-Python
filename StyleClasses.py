import sys
import gi,os
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw
import os.path


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_default_size(520, 720)
        
        a=Gtk.ScrolledWindow()
        a.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)


        b=Gtk.Box()
        b.append(Gtk.Button(label="None",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["text-button"]))
        b.append(Gtk.Button(label="flat",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["text-button","flat"]))
        b.append(Gtk.Button(label="suggested",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["text-button","suggested-action"]))
        b.append(Gtk.Button(label="destructive",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["text-button","destructive-action"]))

        c=Gtk.Box()
        c.append(Gtk.Button(label="pill",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["text-button","pill"]))
        c.append(Gtk.Button(label="circular",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["text-button","circular"]))
        c.append(Gtk.Button(label="osd",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["text-button","osd"]))

        e=Gtk.Box()
        e.append(Gtk.Entry(margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,text="regular",visibility=False))
        e.append(Gtk.Entry(margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["success"],text="success",show_emoji_icon=True))
        e.append(Gtk.Entry(margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["warning"],text="warning",secondary_icon_name="edit-copy-symbolic"))
        e.append(Gtk.Entry(margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["error"],text="error"))

        f=Gtk.Box(css_classes=["linked"],halign=Gtk.Align.CENTER)
        for i in "linked":
            f.append(Gtk.Button(label=i))
        
        o=Gtk.Box(css_classes=["linked","vertical"],orientation=Gtk.Orientation.VERTICAL,margin_top=10,margin_start=10,margin_bottom=10,margin_end=10)
        for i in "Cts":
            o.append(Gtk.Button(label=i))

        p=Gtk.Box(css_classes=["card"],margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,valign=Gtk.Align.START,halign=Gtk.Align.CENTER)
        p.append(Gtk.Label(label="card",margin_top=50,margin_start=50,margin_bottom=50,margin_end=50))

        q=Gtk.Box()
        q.append(Gtk.CheckButton(label="",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,active=True))
        q.append(Gtk.CheckButton(label="",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10))
        q.append(Gtk.CheckButton(label="",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["selection-mode"],active=True))
        q.append(Gtk.CheckButton(label="",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["selection-mode"]))

        w=Gtk.Box(css_classes=["toolbar"],margin_top=10,margin_start=10,margin_bottom=10)
        w.append(Gtk.Button(icon_name="tab-new-symbolic",css_classes=["image-button"]))
        w.append(Gtk.Entry(hexpand=True))
        w.append(Gtk.Button(icon_name="window-close-symbolic",css_classes=["image-button"]))

        l=Gtk.Box(css_classes=["toolbar","osd"],margin_top=10,margin_start=10,margin_bottom=10)
        l.append(Gtk.Button(icon_name="media-playback-start-symbolic",css_classes=["image-button"]))
        l.append(Gtk.ProgressBar(hexpand=True,valign=Gtk.Align.CENTER))
        l.append(Gtk.Button(icon_name="media-record-symbolic",css_classes=["image-button"]))

        d=Gtk.ListBox(css_classes=["boxed-list"],margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,valign=Gtk.Align.START,halign=Gtk.Align.CENTER,selection_mode=Gtk.SelectionMode.NONE)
        d.append(Gtk.Label(label="Buttons",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["heading"]))
        d.append(b)
        d.append(c)
        d.append(Gtk.Label(label="Entries",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["heading"]))
        d.append(e)
        d.append(Gtk.Label(label="Linked controls",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["heading"]))
        d.append(f)
        d.append(o)
        d.append(Gtk.Label(label="Labels",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["heading"]))
        d.append(Gtk.Label(label="large-title",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["large-title"]))
        d.append(Gtk.Label(label="title-1",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["title-1"]))
        d.append(Gtk.Label(label="title-2",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["title-2"]))
        d.append(Gtk.Label(label="title-3",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["title-3"]))
        d.append(Gtk.Label(label="heading",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["heading"]))
        d.append(Gtk.Label(label="monospace",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["monospace"]))
        d.append(Gtk.Label(label="numeric(0123456789)",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["numeric"]))
        d.append(Gtk.Label(label="accent",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["accent"]))
        d.append(Gtk.Label(label="success",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["success"]))
        d.append(Gtk.Label(label="warning",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["warning"]))
        d.append(Gtk.Label(label="error",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["error"]))
        d.append(Gtk.Label(label="caption-heading",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["caption-heading"]))
        d.append(Gtk.Label(label="body",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["body"]))
        d.append(Gtk.Label(label="link",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["link"]))
        d.append(Gtk.Label(label="caption",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["caption"]))
        d.append(Gtk.Label(label="Card",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["heading"]))
        d.append(p)
        d.append(Gtk.Label(label="Check Buttons",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["heading"]))
        d.append(q)
        d.append(Gtk.Label(label="Toolbar",margin_top=10,margin_start=10,margin_bottom=10,margin_end=10,css_classes=["heading"]))
        d.append(w)
        d.append(l)

        a.set_child(d)
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
