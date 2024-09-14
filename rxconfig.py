import reflex as rx

config = rx.Config(
    app_name="reflex_soomin",
)

def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",  
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            text_align="left",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
