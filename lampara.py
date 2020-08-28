# -*- coding: utf-8 -*-

class Lamp:  #declarar la clase en mayúscula
    _LAMPS = [''' 
            .
       .    |    .
        \   '   /
       `  .-. '
     --- (   ) ---
          \ /
         _|=|_
        |_____|
    ''',
    '''
          .-.
         (   )
          \ /
         _|=|_
        |_____|
    ''']

    def __init__(self, is_turned_on): # esta recibiendo como primer parametro si la lampara esta encendida o apagada y la esta guardando en una instancia
        self._is_turned_on = False

    def turn_on(self):
        self._is_turned_on = True
        self._display_imagen()

    def turn_off(self):
        self._is_turned_on = False
        self._display_imagen()

    def _display_imagen(self): # métodos privado
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])    

def run():
    lamp = Lamp(is_turned_on = False)

    while True:
        command = str(input(''' 
            ¿Qué deseas hacer?
            
            [p]render
            [a]pagar
            [s]alir         
         '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()