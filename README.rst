Tarea Toku: Combate Heroes
==============================

Este proyecto simula una batalla entre dos equipos de héroes de miembros al azar. Los Héroes se enfrentan en combates uno a uno hasta que un equipo queda sin miembros para seguir combatiendo. En cada ronda se hacen parejas de héroes que se enfrentaran, pudiendo algunos quedar libres si no hay suficientes contrincantes en pie en el otro equipo. Los héroes atacan en turnos, donde el héroes con el stat de velocidad *speed* más alto ataca primero.

Tabla de contenidos
-------------------

.. contents:: 

Estructura del proyecto
-----------------------

.. code-block:: raw
   
   TareaToku
   ├── modules
   │   ├── __init__.py
   │   ├── hero.py
   │   └── team.py
   ├── utils
   |   ├── __init__.py
   |   ├── cli_printer.py
   |   ├── fetcher.py
   │   └── mail_sender.py
   ├── .gitignore
   ├── README.rst
   ├── requirements.txt
   └── main.py

Ejecución
-----------

Normal
______

1.- Se requiere instalar Python 3.10 o superior

2.- Se deben instalar los requisitos del proyecto utilizando

``$ pip install -r requirements.txt``

3.- Para ejecutar el proyecto se debe ejecutar:

``$ python main.py``

Existen los siguientes comandos opcionales:

.. code-block:: raw

   $ python main.py --colored 
   'mejora la redibilidad del output del terminal agregando color a distintos elementos'
   
   $ python main.py --mail {yourmail@gmail.com}
   'envia un mail con el log completo de los eventos de la batalla a la dirección de correo ingresada'

*Nota 1: la función de output con color puede no verse correctamente en ciertos terminales.*

*Nota 2: Para enviar un mail se utiliza la versión gratuita de mailgun. La que requiere que las direcciones de correo sean autorizadas. Actualmente, se tiene autorizada el correo 'enzo@trytoku.com', pero si se quiere utilizar otro correo para la revisión, es necesario que me contacten para agregarlo a las direcciones autorizadas.*

Funcionamiento
--------------

Al ejecutar el código se irá imprimiendo en el terminal los distintos eventos de los combates, a continuación se muestra un ejemplo del *output*:

.. code-block:: raw

  ####################################################################################################

  Team 1                                                                                        Team 2
  King Kong                                                                                   Stargirl
  Beast                                                                                       Catwoman
  X Lady Deathstrike                                                                         JJ Powell
  X Luke Cage                                                                              X Luke Cage
  X Living Tribunal                                                                  X Living Tribunal

  ----------------------------------------------------------------------------------------------------

  Battle 1:

  King Kong (540/540)                              vs                               Stargirl (383/383)

  > King Kong attacked Stargirl with a strong attack, dealing 634 of damage
  > Stargirl hp: (0/383)

  >> King Kong defeated Stargirl

  Battle 2:

  Beast (548/548)                                  vs                               Catwoman (552/552)

  > Catwoman attacked Beast with a strong attack, dealing 4262 of damage
  > Beast hp: (0/548)

  >> Catwoman defeated Beast

Para cada ronda se imprimen los miembros de cada equipo, marcando con una X antes del nombre los héroes fuera de combate. 

Luego se imprime cada batalla de la ronda, detallando cada ataque ejecutado, el daño realizado y el hp de héroe que recibe el ataque. Los valores de hp se imprimen como ( valor actual / valor base).

Módulos
--------------
Main
_____

Contiene la lógica para organizar el combate y ejecutar los turnos.

Hero
_____
Contiene a la clase Héroes que representa a cada personaje. 

Team
_____
Contiene a la clase Teams que representa a cada equipo de héroes.

cli_printer
___________
Contiene a la clase CliPrinte, utilizada para dar formato al *output* del terminal. También se encarga de almacenar el log de eventos de la batalla en formato *html* para ser enviador por mail.

fetcher
_______
Contiene funciones para hacer un *request* de la información de los héroes a la api https://www.superheroapi.com/

mail_sender
_______
Contiene la función para enviar un mail utilizando la api https://www.mailgun.com/

