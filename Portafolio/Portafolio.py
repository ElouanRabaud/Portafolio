import reflex as rx
import Portafolio.styles.styles as styles


def index() -> rx.Component:
    return rx.box(

    )

app = rx.App(
    stylesheets=styles.STYLE_SHEETS,
    style=styles.BASE_STYLE
)

app.add_page(
    index,
    title="Portafolio Elouan Rabaud | Ingeniero Informático",
    description="Este es mi portafolio actual. Contiene todos mis conocimientos y proyectos realizados hasta la fecha"
)




