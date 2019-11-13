from DataControll import Data

from confapp import conf
import pyforms
from pyforms_gui.basewidget import BaseWidget
from pyforms_gui.controls.control_button import ControlButton
from pyforms_gui.controls.control_text import ControlText



class Gui(BaseWidget):
    def __init__(self):
        super(Gui, self).__init__('CocktailMaker3000')
        self._text1 = ControlText('FilePath', 'drinks.json')
        self._text2 = ControlText()
        self._text2.label_visible = False
        self._text2.readonly = True
        self._button = ControlButton('LoadCocktails')
        self._button.value = self.__buttonAction

    def __buttonAction(self):
        out = ""

        for x in Data.load_drinks(str(self._text1.value)):
            out += str(x)

        print(out)
        self._text2.value = out


if __name__ == "__main__": pyforms.start_app(Gui)
