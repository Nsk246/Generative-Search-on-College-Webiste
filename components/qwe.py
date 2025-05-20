import reflex as rx

from webui import styles
from webui.state import Statex as State


def navbar2():
    return rx.chakra.box(
        rx.chakra.hstack(
            rx.chakra.hstack(
                rx.chakra.icon(
                    tag="hamburger",
                    color="#fff",
                    mr=4,
                    opacity=0,
                    on_click=State.toggle_drawer,
                    cursor="pointer",
                ), 

                rx.chakra.breadcrumb(
                    rx.chakra.breadcrumb_item(
                        rx.chakra.heading("CAMPUS QUEST",font_family="Schibsted Grotesk",size="sm",color="#fff"),
                    ),
                    rx.chakra.breadcrumb_item(
                        rx.chakra.text(State.current_chat, size="sm", font_weight="normal",color="#fff",opacity=0),
                    ),
                ),
            ),
            rx.chakra.hstack(
                rx.chakra.button(
                    "New Search",
                    bg="#FAF9F6",
                    color="#211c1d",
                    px="4",
                    py="2",
                    h="auto",
                    on_click=State.toggle_modal,
                    opacity=0,
                    _hover={
     "background_color": "#D8D8D8",
 },
                ),margin_right="15px",
                spacing="8",
                
            ),
            justify="space-between", margin_left="15px",
        ),
        
        bg="#1C1B20",
        backdrop_filter="auto",
        backdrop_blur="lg",
        p="2",
        position="sticky",
        top="0",
        z_index="100",
    )