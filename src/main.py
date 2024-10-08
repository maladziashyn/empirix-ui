import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Adw, Gio, Gtk

from os import getcwd
from os.path import join, dirname


@Gtk.Template(filename=join(dirname(__file__), "window.ui"))
class AppWindow(Adw.ApplicationWindow):
    __gtype_name__ = "AppWindow"

    er_mc_target_dir = Gtk.Template.Child()  # entry row
    btn_target_dir = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback("btn_callback_01")
    def pick_target_dir(self, *args):
        # self.en_directory.set_text(c.PROJ_SRC)
        # print(self.er_mc_target_dir.get_text())
        native = Gtk.FileDialog()
        native.select_folder(self, None, self._on_select_folder_complete)

    def _on_select_folder_complete(self, dialog, result):
        folder = dialog.select_folder_finish(result)
        if folder:
            print(folder.get_path())
            self.er_mc_target_dir.set_text(folder.get_path())



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
