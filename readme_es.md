# Generador de Contraseñas

Un script de Python para generar contraseñas aleatorias con opciones personalizadas.

## Versiones de Idioma
[![Inglés](https://img.shields.io/badge/Inglés-Inglés-blue)](readme.md)
[![Alemán](https://img.shields.io/badge/Alemán-Alemán-blue)](readme_de.md)
[![Español](https://img.shields.io/badge/Español-Español-blue)](readme_es.md)

## Introducción

Este script de Python te permite generar contraseñas aleatorias con opciones específicas, como la longitud de la contraseña y la inclusión de conjuntos de caracteres extendidos. Puedes utilizar esta herramienta para crear contraseñas fuertes y seguras para tus aplicaciones o cuentas.

## Características

- Generar contraseñas aleatorias con una longitud especificada.
- Incluir conjuntos de caracteres extendidos para contraseñas más seguras.
- Personalizar conjuntos de caracteres para satisfacer tus necesidades.

## Empezando

### Requisitos Previos

Para utilizar este script, debes tener Python instalado en tu sistema. Puedes descargar e instalar Python desde el sitio web oficial: [Descargas de Python](https://www.python.org/downloads/).

### Instalación

1. Clona el repositorio en tu máquina local utilizando el siguiente comando:

    ```bash
    git clone https://github.com/david-star-git/keyshuffler.git
    ```

2. Cambia el directorio de trabajo a la carpeta del proyecto:

    ```bash
    cd KeyShuffler
    ```

3. Ejecuta el script con las opciones deseadas (consulta [Uso](#uso)).

## Uso

Para generar una contraseña, ejecuta el script con el siguiente comando:

```bash
python password_generator.py
```

Por defecto, esto generará una contraseña de 50 caracteres con solo caracteres ASCII estándar. Puedes personalizar la longitud de la contraseña y el conjunto de caracteres utilizando las siguientes opciones:

- **-l** o **--longitud**: Especifica la longitud de la contraseña.
- **-e** o **--extendido**: Incluye un conjunto de caracteres extendido para contraseñas más seguras.

Ejemplos de uso:

- Generar una contraseña de 12 caracteres con caracteres extendidos:

```bash
python password_generator.py -l 12 -e
```

## Personalización

Puedes personalizar los conjuntos de caracteres utilizados para caracteres normales y extendidos editando las variables `normal_chars` y `extended_chars` dentro del script. Los valores predeterminados proporcionan un conjunto razonable de caracteres para generar contraseñas, pero puedes modificarlos según tus necesidades.

```py
normal_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{}|;:'\"<>,.?/~"
extended_chars = " ¡⅛£¤⅜⅝⅞™±°¿˛¯˘˚ÞØı↑¥Ŧ®€§ΩÆẞÐªŊĦ ̇&Ł ̣ˇ—÷×º’‘‚©‹›ˍ|»«¢„“”µ·…–^˝łĸ ̣ħŋđðſæ@ſ€¶ŧ←↓→øþ¨’¸\}][{¬½¼³²¹⁴⁵⁶⁷⁸⁹⁰}]"
```

## Licencia

Este proyecto está bajo la [Licencia Pública General de GNU, versión 3.0](LICENSE). Puedes encontrar el texto completo de la licencia [aquí](https://www.gnu.org/licenses/gpl-3.0.html).