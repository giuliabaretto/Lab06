import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler

    # creo funzione mostra automobili che trovo nel model -> get_auto
    def mostra_automobili(self, e):
        automobili = self._model.get_automobili() # lista oggetti automobili da trasformare in elementi di interfaccia -> lista automobili diventa list view di automobile
        self._view.mostra_lista_automobili(automobili)
        self._view.update()

    def cerca_per_modello(self, e):
        modello = self._view.input_modello_auto.value #valore preso dalla view
        automobili = self._model.cerca_automobili_per_modello(modello)
        self._view.mostra_lista_automobili_per_modello(automobili)

    # quando la View riceve l'evento del click (on_click = self.controller.cerca_per_modello, o nel caso precedente on_click = self.controller.mostra_automobili)
    # il Controller intercetta il click e chiama il Model per prendere i dati (prima riga della def)
    # poi il Controller dà alla View la lista delle automobili da mostrare nella pagina (seconda riga della def)

    # quindi devo definire mostra_lista_automobili() e mostra_lista_automobili_per_modello() nella View (fatto in fondo)