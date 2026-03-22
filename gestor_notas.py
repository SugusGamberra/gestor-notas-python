# Importación de las librerías instaladas
import sys

from rich.console import Console #para la consola
from rich.panel import Panel #para el menu
from rich.table import Table #para las tablas

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

# IMPLEMENTACIÓN DE OPCIONES DEL MENÚ
# Ver notas:

def ver_notas(notas):
    """Muestra todas las notas guardadas en formato tabla y estadísticas."""
    
    # Si la lista está vacía, avisamos y salimos de la función
    if not notas:
        consola.print("[bold yellow]Aún no tienes ninguna nota guardada. ¡Anímate a escribir la primera![/bold yellow]\n")
        return

    # Si hay notas, creamos una tabla chulísima
    tabla = Table(title="🌸 Tus Notas 🌸", border_style="pink1", header_style="bold light_cyan3")
    
    # Definimos las columnas
    tabla.add_column("Nº", justify="center", style="cyan")
    tabla.add_column("Título", style="bold magenta")
    tabla.add_column("Categoría", justify="center", style="pink1")
    tabla.add_column("Contenido", style="white")

    # Variable para calcular la longitud media
    total_longitud = 0

    # Rellenamos la tabla recorriendo la lista con un for
    for i, nota in enumerate(notas, start=1):
        tabla.add_row(
            str(i), 
            nota["titulo"], 
            nota.get("categoria", "General"), 
            nota["contenido"]
        )
        total_longitud += len(nota["contenido"])

    # Imprimimos la tabla
    consola.print(tabla)

    # Estadísticas
    media = total_longitud / len(notas)
    consola.print(f"[italic pink1]Estadísticas: {len(notas)} notas guardadas | Longitud media: {media:.0f} caracteres[/italic pink1]\n")
    
# Añadir notas:
def add_nota(notas):
    consola.print("\n[bold pink1]🗒️ Nueva Nota 🗒️[/bold pink1]")
    
    # Pedimos los datos al usuario
    titulo = consola.input("[light_cyan3]Título de la nota:[/light_cyan3] ").strip()
    categoria = consola.input("[light_cyan3]Categoría (ej: DAW, Poryectos, Tareas, Compras...):[/light_cyan3] ").strip()
    contenido = consola.input("[light_cyan3]Contenido:[/light_cyan3] ").strip()

    # Filtro de validación antiborrachines HAHAHHA
    if "cubata" in contenido.lower() or "cubata" in titulo.lower():
        consola.print("\n[bold red]⚠️  ¡ALERTA DE BORRACHÍN/A! ⚠️[/bold red]")
        alerta = consola.input("[bold red]¿Estás intentando salir de fiesteo con la de cosas que tienes que hacer? ¿Seguro/a que quieres guardar esta nota? (s/n): [/bold red]").strip().lower()
        if alerta != 's':
            consola.print("[yellow]Has hecho bien. Nota descartada, las fiestas cuando termine el curso 👀[/yellow]\n")
            return

    # Comprobar si el título ya existe
    for nota in notas:
        if nota["titulo"].lower() == titulo.lower():
            sobreescribir = consola.input(f"\n[bold yellow]⚠️ Ya existe una nota con el título '{titulo}'. ¿Quieres sobreescribirla? (s/n): [/bold yellow]").strip().lower()
            if sobreescribir == 's':
                nota["categoria"] = categoria
                nota["contenido"] = contenido
                consola.print("[bold green]¡Nota actualizada con éxito! 🌸[/bold green]\n")
            else:
                consola.print("[yellow]Operación cancelada. La nota original sigue intacta.[/yellow]\n")
            return # Salimos de la función porque ya hemos gestionado el duplicado

    # confirmación final antes de guardar
    confirmacion = consola.input("\n[bold light_cyan3]¿Guardar esta nota definitivamente? (s/n): [/bold light_cyan3]").strip().lower()
    if confirmacion == 's':
        # Creamos el diccionario y lo metemos en la lista
        nueva_nota = {
            "titulo": titulo,
            "categoria": categoria,
            "contenido": contenido
        }
        notas.append(nueva_nota)
        consola.print("[bold green]¡Nota guardada con éxito! 🌸[/bold green]\n")
    else:
        consola.print("[yellow]Operación cancelada. No se ha guardado nada.[/yellow]\n")

#MAIN
def main():
    #Bucle principal para que llame al resto de ufnciones
    notas = []
    
    #voy a hardcodear para ver el resultado, lo dejare todo comentado en el futuro para q veas el proceso jeje
    #notas = [
    #    {"titulo": "Prueba nota 1", "categoria": "Proyectos", "contenido": "Probando como se visualiza en la terminal"},
    #    {"titulo": "hola mundo", "categoria": "Ocio", "contenido": "hello wordl"}
    #]
    
    while True:
        mostrar_menu()
        #Uso el input para recoger la opcion
        opcion = consola.input("[bold light_cyan3]Elige una opción (1 a 5 o prueba suerte con el comando secreto): [/bold light_cyan3]").strip().lower()
        
        if opcion == '1':
            add_nota(notas)
        elif opcion == '2':
            ver_notas(notas)
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
            
        #frenar bucle hasta que el usuario pulse enter
        #se me hacia muy molesto q saltara el menu mientras revisaba como se veian las notas
        consola.input("\n[italic cyan]Presiona Enter para continuar...[/italic cyan]")
        
if __name__ == "__main__":
    main()