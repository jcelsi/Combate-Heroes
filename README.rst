Tarea Toku: Combate Heroes
==============================

Este proyecto simula una batalla entre dos equipos de heroes de miembros al azar. Los Heroes se enfrentan en combates uno a uno hasta que un equipo queda sin miembros para seguir combatiendo. En cada ronda se hacen parejas de heroes que se enfrentaran, pudiendo algunos quedar libres si no hay suficientes contrincantes en pie en el otro equipo. Los heroes atacan en turnos, donde el heroes con el stat de velocidad *speed* mas alto ataca primero.

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

Se deben instalar los requisitos del proyecto utilizando

``pip install -r requirements.txt``

Para ejecutar el proyecto se debe ejecutar:

``python main.py``

Existen los siguientes comandos opcionales:

``python main.py --colored``

``python main.py --mail {yourmail@gmail.com}``

Funcionamiento
--------------

Al ejecutar el codigo se ira imprimiendo en el terminal los distintos eventos de los combates, a continuacion se muestra un ejemplo del *output*:

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

Modulos
--------------
Main
_____

Contiene la logica para organizar el combate y ejecutar los turnos.

Hero
_____
Contiene a la clase Heroes que representa a cada personaje. 

Team
_____
Contiene a la clase Teams que representa a cada equipo de heroes.

cli_printer
___________
Contiene a la clasie CliPrinte, utilizada para dar formato al *output* del terminal. Tambien se encarga de almacenar el log de eventos de la batalla en formato *html* para ser enviador por mail.

fetcher
_______
Contiene funciones para hacer un *request* de la informacion de los heroes a la api https://www.superheroapi.com/

mail_sender
_______
Contiene la funcion para enviar un mail utilizando la api https://www.mailgun.com/
