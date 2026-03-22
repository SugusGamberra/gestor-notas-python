# Importación de las librerías instaladas
import sys

from rich.console import Console
from rich.panel import Panel

# Creación de la consola de rich
consola = Console()

# Menú
def mostrar_menu():
    #para que no me mueva los caracteres uso r"""
    cinnamoroll = r"""
⠀⠀⡠⠂⠉⠉⠐⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀
⠀⠸⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠃⠀⠀⠀⢄⠀⠀
⠀⠇⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠈⡆⠀
⢀⡃⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⢰⠄
⠈⢡⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠸⠄
⠀⠀⠡⡀⠀⠀⠀⠀⠀⠀⠑⠦⡤⠖⠊⠉⠀⠀⠀⠀⠀⠉⠑⠢⣄⣀⡠⠴⠃⠀⠀⠀⠀⠀⢀⠇⠀
⠀⠀⠀⠁⢀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⠀⠀⢀⡘⠀⠀
⠀⠀⠀⠀⠀⠁⠢⠄⣀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⡀⠀⠀⠀⢀⠀⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⠀⢠⢶⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢦⠀⠀⠙⡒⠒⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⠀⠈⠉⠁⠀⠀⠰⠤⠤⡴⠀⠀⠀⠈⠙⠀⠀⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⣼⠋⢳⠀⠀⠀⠀⠈⠒⠀⠀⠀⠀⢠⠊⠙⣤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠑⠒⠒⠒⠒⠒⠒⠒⠒⠒⠋⡀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
    #imprimo al chili morron con color azulito
    consola.print(cinnamoroll, style="bold light_cyan3")
    
    #Menú principal
    menu_texto = (
        "[bold pink1]1. [/bold pink1] Añadir una nota\n"
        "[bold pink1]2. [/bold pink1] Ver todas las notas\n"
        "[bold pink1]3. [/bold pink1] Buscar una nota por palabra clave\n"
        "[bold pink1]4. [/bold pink1] Eliminar una nota\n"
        "[bold pink1]5. [/bold pink1] Salir\n"
    )
    consola.print(Panel(menu_texto, title="☁️Menú Principal☁️", border_style="pink1", expand=False))

def main():
    #Bucle principal para que llame al resto de ufnciones
    notas = []
    
    while True:
        mostrar_menu()
        #Uso el input para recoger la opcion
        opcion = consola.input("[bold light_cyan3]Elige una opción (1 a 5 o prueba suerte con el comando secreto): [/bold light_cyan3]").strip().lower()
        
        if opcion == '1':
            consola.print("[yellow]Has elegido añadir una nota (WiP)[/yellow]")
        elif opcion == '2':
            consola.print("[yellow]Has elegido ver todas las notas (WiP)[/yellow]")
        elif opcion == '3':
            consola.print("[yellow]Has elegido buscar una nota (WiP)[/yellow]")
        elif opcion == '4':
            consola.print("[yellow]Has elegido eliminar una nota (WiP)[/yellow]")
        elif opcion == '5':
            consola.print("[yellow]Cerrando el gestor de notas... (WiP)[/yellow]")
            break
        elif opcion == 'pokemon':
            consola.print("[bold yellow]Abriendo la Pokedex... (Wip)[/bold yellow]")
        elif opcion == 'suerte':
            consola.print("[bold purple]Buscando en la Jesubiblia si hoy tendrás suerte o no... (WiP)[/bold purple]")
        else:
            consola.print("[bold red]Opción no válida, inténtalo de nuevo![/bold red]")
            
if __name__ == "__main__":
    main()