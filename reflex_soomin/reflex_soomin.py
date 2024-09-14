"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from reflex_soomin.state import State


def index() -> rx.Component:

    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        # Counter State example BEGIN ========
        rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="ruby",
                on_click=State.decrement,
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="grass",
                on_click=State.increment,
            ),
            spacing="4",
        ),
        # Counter State example ENDED ========
        rx.vstack(
            rx.heading("Welcome to Reflex! - 2", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.image("download.jpg"),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


app = rx.App()
app.add_page(index)
