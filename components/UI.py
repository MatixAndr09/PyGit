from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.binding import Binding

class Main(App):

    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="i", action="open_input_menu", description="Open the interactive menu")
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

    def on_mount(self) -> None:
        self.title = "PyGit > Better Github Desktop"
        self.sub_title = "v0.0.1"


def run():
    app = Main()
    app.run()
