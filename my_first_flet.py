import flet as ft

def main(page: ft.Page):
    page.title = "Flet Hello World"
    page.theme_mode = ft.ThemeMode.SYSTEM
    #ALINEAR CONTENIDO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    #ALERTA
    dlg = ft.AlertDialog(
        title=ft.Text("¡Hola, Mundo!")
    )
    
    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()
    
    page.appbar = ft.AppBar(
        title=ft.Text("Hello World my name is Jhair7")
    )

    page.add(
        ft.Text("END"),
        ft.Row(
        [
            ft.Text("Hello World"),
            ft.ElevatedButton(text="Show Hello World", on_click=open_dlg)
        ]
        )
    )

ft.app(target = main)