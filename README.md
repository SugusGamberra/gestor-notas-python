# GESTOR DE NOTAS
<div align="center">
  <img src="" alt="WiP del logo" width="120" />

  # Gestor de Notas Chili Morrón
  
  <p>
    Gestor de notas inspirado en el personaje de Sanrio <strong>Cinnamoroll</strong>.<br>
    Estética <em>dreamy & ethereal</em>, lógica robusta en Python.
  </p>

  ![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=plastic)
  ![Rich Badge](https://img.shields.io/badge/Rich-FFB6C1?logo=python&logoColor=white&style=plastic)
  ![Requests Badge](https://img.shields.io/badge/Requests-ADD8E6?logo=python&logoColor=white&style=plastic)
</div>


> Quiero hacer este proyecto con ciertas ideas que tengo en mente.
* **Arte ASCII**: Quiero incluir en `mostrar_menu()` un dibujillo de Cinnamoroll (pj de Sanrio que me encanta)
* **Colores**: Usando la libreria `rich` y con códigos `ANSI` crearé una paleta de colores bonitas y temática con la estética que busco :P Así puedo incluir el uso de markdown que lo domino y me gusta mucho :3
* **Categorías**: Siguiendo las ideas que das en el pdf, categorizar las notas por contenido! Incluiré también que muestre cuántas notas hay guardadas en total y la media de cuántos caracteres se usan para escribirlas~
* **Notion**: Como hice un proyecto de un widget de escritorio hace tiempo que lo tengo conectado a la bbdd de notion, me gustaría hacer lo mismo para este! Cada vez que meta una nota en la terminal que vaya directamente a notion
* **Easter egg**: Comandos secretos, dentro del menú poner royo una sección oculta por ejemplo Pokemon y que añadas ahí los pokemon que vayas capturando en algun juego.
* **Filtros**: Una función de limpieza que cada vez que escribas, por ejemplo, cubata, se detenga y muestre una alerta en plan "Alerta por borrachin/borrachina, ¿deseas continuar? (s/n)" o alguna cosa random HAHAHAH 

---

## Creación del archivo

Inicio creando el archivo `gestor_notas.py` en VSC.

Empiezo buscando el **arte ascii** de [cinnamoroll](https://emojicombos.com/cinnamoroll-ascii-art).

```bash
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
```

Ahora voy a instalar en la terminal las librerías usando:

```bash
pip install colorama rich requests
```

* **rich**: En los requisitos se especifica usar `colorama` pero yo quiero algo muy adorable y claro, colores pastel y tal, he bicheado por internet alternativas y me topé con esta de [rich](https://www.reddit.com/r/Python/comments/jyi8ku/better_python_console_apps_with_rich/?tl=es-es). Te permite hacer cosas brutales muy facilmente como el `Panel` jeje
* **requests**: Como quiero conectarla a la api de notion... Hace tiempo hice un proyectillo personal como puse arriba. Me mola mucho usar apis jeje y el resultado es una gozada, me facilita mucho la vida jeje Así que me gustaría trasladarlo aquí para que las notas se suban solas. Buscando cómo hacerlo y hacer peticiones http para python vi que el estandar es [`requests`](https://j2logo.com/python/python-requests-peticiones-http/) por ser sencilla :3

Una vez instaladas las llamo dentro del proyecto usando `import` arribita del todo!

Con `rich` importado me monto una consola para poder imprimirlo todo así kawaii en vez de usar el `print` clásico de siempre, por ende usaré `consola.print()`.

## Diseño del `mostrar_menu()`

Aquí meto a mi cinnamoroll. Para no romper el dibujo en la terminal lo guardo en una variable usando `r"""..."""` (para que lea los caracteres tal cual) y le doy un color azul pastel con las etiquetas de `rich` (`[bold light_cyan3]`) <3

Después creo el menú de opciones. En lugar de texto plano uso un `Panel` de `rich` para que me haga un cuadrado rosita con bordes redondeados (se rompe un poco a la derecha, no sé si hice algo mal x.x)

## `main()`

Me creo la lista vacía de `notas = []` donde irán guardándose los diccionarios y abro un bucle `while true` para que el menú se repita hasta que el usuario decida salirse.

Teniendo en cuenta la [Jesubiblia](https://github.com/SugusGamberra/JesubibliaDePython) en el **Versículo 3:1** para hacer el menú. El cuerpo me pedía usar `match-case` pero sigo al dedillo la sabiduría de Jesús Deidad y no acometer al pecado 👀 ya que también en los requisitos del proyecto se pide usar estos condicionales, así que he sido buena cristiana 🙂‍

Para los easter eggs (que claro, trampuchis porque verás el código y sabrás cuáles son 😢) en la validación del menú he colocado 2 comandos secretos. Si en vez de número escribes otra palabra, se abre un "portal" oculto 🫢

Por el momento se ve así:

<img src="./public/img/capturas/1.png" width="300" style="border-radius: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);">

> Por hoy lo dejo aquí, seguiré poquito a poco en próximos días

---

## Implementación de las opciones

### Ver notas

Para visualizar las notas voy a usar de la librería `rich`las tablas, así que la importo arriba del todo!

Ahora crearé la función antes del `main()` ya que **python** es un lenguaje interpretado que lee el código de forma secuencial, de arriba a abajo. Si se llama `ver_notas()` o `mostrar_menu()` dentro del bucle principal antes de haberlas creado tiraria un error. Al definirlas primero cuando el programa llega al `if __name__ == "__main__":` y ejecuta el `main()`, tiene ahi guardadas en memoria todas las instrucciones que encesita usar jeje:

1. Para evitar que el programa se rompa ni haga cosas raras, si el usuario pide ver las notas y aún no hay ninguna creo un condicional en el que `if not notas` (si la lista está vacía) imprime un mensaje animando a escribir y usa un `return` para salir de la función.
2. En vez de imprimir los diccionarios en texto plano, con `Table` he configurado las columnas `nº`, `titulo`, `categoria` y `contenido` siguiendo la estética adorable en toda la terminal :3
3. Para rellenar la tabla, el proyecto pedía que las notas se mostraran numeradas. En vez de crear una variable contador (tipo `i = 1`) e ir sumando en cada vuelta, he usado un bucle `for` apoyado en la funcion nativa `enumerate(notas, start=1)`. Esto saca automáticamente el índice para la columna de `nº` como el propio diccionario de l anota.
4. He ampliado aquí con la idea de las estadísticas de las notas creando una varibale `total_longitud = 0` antes del bucle. Dentro de este en cada pasada le voy sumando la longitud del contenido de la nota (`len(nota["contenido"])`) y cuando termina el bucle se calcula la media dividiendo el total entre el número de notas (`len(notas)`)

Ahora para poder sacarla la conecto al `main()` en la opción 2.

He hardcodeado 2 notas para poder ver el resultado:
```py
notas = [
        {"titulo": "Prueba nota 1", "categoria": "Proyectos", "contenido": "Probando como se visualiza en la terminal"},
        {"titulo": "hola mundo", "categoria": "Ocio", "contenido": "hello wordl"}
    ]
```

Y además he añadido al final del bucle un `input` que me permita pulsar enter para continuar, era muy molesto intentar ver las notas y que saltara el menú de nuevo...

Por ahora se ve así:

<img src="./public/img/capturas/2.png" width="300" style="border-radius: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);">

### Añadir notas

Ahora vamos a crear la función de `add_nota(notas)` para quitar lo hardcodeado!

Con esta opción alimentamos la lista de diccionarios. Para hacerla super completa:

1. **Recogida de datos:** Usando `consola.input()` pido el título, la categoría y el contenido. Les aplico `.strip()` al final para limpiar los espacios en blanco accidentales que pueda dejar el usuario al principio o al final de la frase.
2. **Filtro de Validación (Easter Egg):** Antes de procesar nada, he metido mi función de limpieza. Usando el operador `in`, compruebo si cierta palabra que no queremos que exista este en el contenido o en el título (usando `.lower()` para que no importe si lo escriben en mayúsculas). Si es así, freno la ejecución y lanzo un `input` de alerta. Si el usuario elige 'n', uso un `return` para abortar la función al instante.
3. **Control de duplicados:** El PDF exige que si un título ya existe, el programa pregunte si queremos sobreescribirlo. Para ello, recorro la lista actual con un `for nota in notas`. Si encuentro una coincidencia de títulos, pregunto. Si la respuesta es afirmativa, actualizo las claves `categoria` y `contenido` de ese diccionario directamente y salgo con un `return`.
4. **Confirmación y Guardado:** Si el título es nuevo y ha pasado los filtros, cumplo con el último requisito del PDF pidiendo confirmación final (`¿Guardar esta nota? (s/n)`). Si es un sí, meto las tres variables en un diccionario nuevo `{...}` y uso el método `.append()` para inyectarlo al final de la lista `notas`.

Ahora, para ver como funciona en terminal:

- Creación de una nota normal y corriente

<img src="./public/img/capturas/3.png" width="500" style="border-radius: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);">

- Creación de una nota con la palabra del filtro en título y cuerpo. En la primera imagen acepto el guardar la nota y en la segunda rechazo:

<img src="./public/img/capturas/4.png" width="500" style="border-radius: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);">
<img src="./public/img/capturas/5.png" width="500" style="border-radius: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);">

- Visualización de que las notas se han guardado correctamente:

<img src="./public/img/capturas/6.png" width="500" style="border-radius: 15px; box-shadow: 5px 5px 15px rgba(0,0,0,0.4);">

> Por hoy desconecto! Mañana sigo :3 (Quiero dejar super bien especificado absolutamente todo, así que sorry por ser tan transparente HAHAHAH mi vena de laboratorio me anima a apuntar absolutamente TODO)