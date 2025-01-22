"""The main application."""

# TODO(#1): directory tree so user can select path

from textual import on
from textual.binding import Binding
from textual.app import App, ComposeResult, ScreenError
from textual.containers import Center, Container, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label, ListItem, ListView, Select, Static, TabbedContent, TabPane, TextArea
from .factory import query, FactoryError
from .license import License, LICENSES
from . import parser


def twice[T](value: T) -> tuple[T, T]:
    return (value, value)


class Form(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Back"), ("enter", "app.create_license", "Create license")]

    def __init__(self, license: License) -> None:
        super().__init__()
        self.license = license
        self.replacements: dict[str, str] = {}
        self.file_name: str | None = None
        
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        content = self.license.content
        with Horizontal():
            yield TextArea(content, read_only=True)
            with Vertical():
                for field in parser.substitutions(content):
                    # TODO: add suggester that suggest values used previously; implies history
                    try:
                        default = query(field)
                    except FactoryError as e:
                        self.notify(f"An error occured while querying defaults: {e.stderr}", title="Error", severity="error")
                        default = None
                    yield Input(placeholder=field, name=field, value=default)
                yield Select([
                    twice("LICENSE.txt"),
                    twice("LICENSE"),
                    twice(f"LICENSE-{self.license.short_name}.txt"),
                    twice(f"LICENSE-{self.license.short_name}"),
                ], prompt="File name", value="LICENSE.txt")
                yield Center(Button.success("Create license"))

    @on(Input.Changed)
    def update_content(self, event: Input.Changed) -> None:
        assert event.input.name is not None
        if event.value:
            self.replacements[event.input.name] = event.value
        else:
            del self.replacements[event.input.name]
        self.query_one(TextArea).text = parser.replace(self.license.content, **self.replacements)

    @on(Select.Changed)
    def update_file_name(self, event: Select.Changed) -> None:
        self.file_name = str(event.value)

    @on(Button.Pressed)
    def create_license(self):
        text = self.query_one(TextArea).text
        with open(self.file_name, "w") as f:
            f.write(text)
        self.app.exit()


class MkLicense(App):
    BINDINGS = [("enter", "select_license()", "Select license")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with TabbedContent():
            for license in LICENSES:
                with TabPane(license.short_name, id=f"tab-{hash(license.spdx)}"):
                    with Horizontal():
                        with Vertical():
                            with Container() as c:
                                c.styles.border = ("solid", "#3dc637")
                                c.border_title = "Permissions"
                                for permission in license.permissions:
                                    yield Static(str(permission), classes="box")
                            with Container() as c:
                                c.styles.border = ("solid", "#0099d6")
                                c.border_title = "Conditions"
                                for condition in license.conditions:
                                    yield Static(str(condition), classes="box")
                            with Container() as c:
                                c.styles.border = ("solid", "#c6403d")
                                c.border_title = "Limitations"
                                for limitation in license.limitations:
                                    yield Static(str(limitation), classes="box")
                        text_area = TextArea(license.content)
                        text_area.styles.width = "85"
                        yield text_area

    def action_select_license(self) -> None:
        # TODOOO: don't trigger when form screen is opened
        selected_tab = self.query_one(TabbedContent).active
        selected_license = [license for license in LICENSES if f"tab-{hash(license.spdx)}" == selected_tab][0]
        screen_id = f"form-{selected_license.spdx}"
        try:
            self.install_screen(Form(selected_license), name=screen_id)
        except ScreenError:
            pass
        self.push_screen(screen_id)


def run():
    app = MkLicense()
    app.run()
