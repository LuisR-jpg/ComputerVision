# Computer vision 

*```Los villanos de los comics son doctores en ciencia.```*

###### [For more information on the topic](https://github.com/LuisR-jpg/School/tree/master/Image%20Processing)

[Final project](https://drive.google.com/file/d/1RJHjradJVPG70s0Zr6BbIAi_LNlGYxEQ/view?usp=sharing)

--- 
## January 14th

### Raspberry Pi 

Surgio como un proyecto con ideas de darle una mejor comprension a los alumnos de computacion.

Es una plataforma abierta (open hardware) que permite desarrollar muchas aplicaciones a un costo muy reducido y con una gran portabilidad.

#### [Operative System](https://www.raspberrypi.com/software/)

Tiene un sistema operativo diseniado especificamente para la tarjeta llamado: *Raspbian*. Hecho con `python`.

#### GPIO

General purpose input output port. It's a set of pins designed to read sensors, send signals, etc.

#### Credentials

Username: pi

Default Password: raspberry

My Password: lRaspberry

---
## January 21st

### Projects

#### Face recognition vs face detection

- Detection is capable of telling whether a photo contains a face or not.

- Recognition is telling *who* is on the photo.

### Raspberry Pi OS

- **Terminal**.

    - The current line says: `user@device`.

        - My pc says `lalitor@lalitor-IdeaPad`.

        - My pi says `pi@raspberrypi`.

    - `history`

        Shows all the previous commands on the terminal.

    - `sudo raspi-config` 

        Advanced settings

    - Update the OS

        - `sudo apt update`. Recommended every time the PI is used. 

        - `sudo apt ugrade`. Every 3 months.


---
## January 28th

### Neat raspberry pi apps

- CoinOPS Legends.

    STEM lab's own project. 

- LibreOffice

- Browsers

    - Chromium

    - Firefox

    - Vivaldi

    - Midori. Lite browser, kinda ugly

- Evince

    Document reader

- Thonny

    Es un IDE profesional desarrollado para Raspberry.

### Python

Un lenguaje de alto nivel es legible para los humanos.

#### Temas

- Comentarios

- Variables

- PEP

    Reglas establecidas para el buen uso de la programacion en python.

- Operadores aritmeticos
---
## Resources

**[Teacher's tiktok](https://www.tiktok.com/@vitoremorleone)**

---

## February 11th

### Collections

|Attribute  |Listas |Tuplas |Sets           |Diccionarios   |
|---        |:---:  |:---:  |:---:          |:---:          |
|Ordenada   |[x]    |[x]    |[ ] No indices |[ ]            |
|Mutable    |[x]    |[ ]    |[x]            |[ ]            |

---
## February 25th

### Protoboard

Cables:

Rojo/Blanco/Naranja - 3.3/5 volts
Azul/Negro/Cafe     - 0 volts

### GPIO

General Purpose Input Output

---
## March 18th

### Install OpenCV

``` bash
sudo pip3 install opencv-contrib-python==4.4.0.46

# Verify installation
python
import cv2
cv2.__version__
```

### Black box

It's a term used in science. Machine Learning algorithm are usually seen as black boxes, since the series of steps within are very complex and not completely understood. 
So, a black box insight is just understanding something that takes an input and provides an output.

### Digital images

Sizes:

Name        |   Size
---         |---
VGA         |640 x 480
HD          |1280 x 720
FHD         |1920 x 1080
4K          |2160 x 3840