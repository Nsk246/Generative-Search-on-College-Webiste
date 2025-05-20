"""The main Chat app."""

import reflex as rx

from webui import styles
from webui.components import chat, modal, navbar, sidebar, qwe
from webui.state import Statex
from webui import LandingPage

def new() -> rx.Component:
    """The main app."""
    return rx.chakra.vstack(
        navbar(),
        chat.chat(),
        chat.action_bar(),
        sidebar(),
        modal(),
        background="radial-gradient(circle, rgba(255,255,255,0.09) 1px, transparent 1px)",
        background_size="25px 25px",
        style=LandingPage.dots,
        color="#0C0C0C",
        min_h="100vh",
        align_items="stretch",
        spacing="0",
    )

def index() -> rx.Component:
    header : object =LandingPage.Header().build()
    main : object=LandingPage.Main().build()

    return rx.vstack(
        
        header,
        main,
        
         _light={
            "background":"radial-gradient(circle,rgba(0,0,0,0.35) 1px,transparent 1px)",
            "background_size":"25px 25px",
        },

        background="radial-gradient(circle, rgba(255,255,255,0.09) 1px, transparent 1px)",
        background_size="25px 25px",
        style=LandingPage.dots

    )

# Add state and page to the app.
app = rx.App(style=styles.base_style,stylesheets=[
        "https://fonts.googleapis.com/css2?family=Schibsted+Grotesk",
    ],theme=rx.theme(
        appearance="dark"  # Sets the default theme to dark mode
    ))
app.add_page(index)
app.add_page(new,route='/search')
app.compile()
