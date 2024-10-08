import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, Gtk

from os import getcwd
from os.path import join


@Gtk.Template(filename=join(getcwd(), "window.ui"))
class AppWindow(Adw.ApplicationWindow):
    __gtype_name__ = "AppWindow"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp(Adw.Application):
    """The main application singleton class."""

    def __init__(self):
        super().__init__(application_id="com.github.maladziashyn.EmpirixUI",
                         flags=Gio.ApplicationFlags.DEFAULT_FLAGS)

    def do_activate(self):
        """Called when the application is activated.
        We raise the application's main window, creating it if necessary."""

        win = self.props.active_window
        if not win:
            win = AppWindow(application=self)
        win.present()


def main():
    """The application's entry point."""

    app = MyApp()
    app.run(None)


if __name__ == "__main__":
    main()
