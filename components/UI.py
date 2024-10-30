from rich.text import Text
from textual.binding import Binding
from textual.screen import ModalScreen
from textual.app import ComposeResult, App
from textual.containers import Center, VerticalScroll
from textual.widgets import Markdown, Footer, Header, Static

WELCOME_MD = """

# Welcome Back!

This is a commandline style better Github Desktop app. It has all the features that the desktop app has and more.

## Features

- View all your repositories
- View all your commits
- View all your branches
- View all your pull requests
- View all your issues
- View all your releases
- View all your tags
- View all your stashes
- View all your settings
- View all your actions
- View all your workflows
- View all your projects
- View all your wikis
- View all your discussions
- View all your packages

## How to use

- Press `i` to open the interactive menu
- Press `q` to quit the app 

"""

TITLE_MAIN = '''
                                               
                                    ,,         
`7MM"""Mq.              .g8"""bgd   db   mm    
  MM   `MM.           .dP'     `M        MM    
  MM   ,M9 `7M'   `MF'dM'       ` `7MM mmMMmm  
  MMmmdM9    VA   ,V  MM            MM   MM    
  MM          VA ,V   MM.    `7MMF' MM   MM    
  MM           VVV    `Mb.     MM   MM   MM    
.JMML.         ,V       `"bmmmdPY .JMML. `Mbmo 
              ,V                               
           OOb"                                
'''

COLORS_MAIN = ['#092819', '#125032', '#1c794c', '#38875e', '#549670', '#71a482', '#8db394', '#a9c2a6', '#c6d0b8', '#e2dfca', '#ffeedc']


class WelcomeScreen(ModalScreen):
    CSS = """
        WelcomeScreen VerticalScroll {
            background: $surface;
            margin: 4 8;        
            border: heavy #1c794c;        
            height: 1fr;        
            .title {
                width: auto;
                # background: #1c794c; /* Dodajemy tło dla tytułu */
                padding: 1 0; /* Dodajemy trochę odstępu wokół tytułu */
            }
            scrollbar-gutter: stable;
            scrollbar-color: #1c794c; /* Kolor paska przewijania */
            Markdown {
                margin:0 2;
            }        
            Markdown .code_inline {
                background: $panel;
                text-style: bold;
            }
        }    
        
        WelcomeScreen Footer {
            background: #1c794c; /* Kolor tła stopki */
        }
        """

    BINDINGS = [
        ("escape", "dismiss"),
    ]

    def __init__(self):
        super().__init__()
        self.TITLE = TITLE_MAIN
        self.COLORS = COLORS_MAIN

    def get_title(self) -> Text:
        lines = self.TITLE.splitlines(keepends=True)
        return Text.assemble(*zip(lines, self.COLORS))

    def compose(self) -> ComposeResult:
        yield Footer()
        with VerticalScroll() as vertical_scroll:
            with Center():
                yield Static(self.get_title(), classes="title")
            yield Markdown(WELCOME_MD)
        vertical_scroll.border_title = "Welcome Back!"
        vertical_scroll.border_subtitle = "ESCAPE to close"
class InteractiveMenu(ModalScreen):
    BINDINGS = [
        ("escape", "dismiss"),
    ]

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Footer()

        InteractiveMenu.border_title = "Interactive Menu"
        InteractiveMenu.border_subtitle = "ESCAPE to close"


class Main(App):
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="i", action="open_input_menu", description="Open the interactive menu"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()

    def on_mount(self) -> None:
        self.title = "PyGit > Better Github Desktop"
        self.sub_title = "v0.0.3"
        self.action_welcome()

    def action_welcome(self) -> None:
        self.app.push_screen(WelcomeScreen())

    def open_input_menu(self) -> None:
        self.app.push_screen(InteractiveMenu())


def run():
    app = Main()
    app.run()
