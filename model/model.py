from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        automobili = []
        connection = get_connection()
        if connection is None:
            print("Connection failed")
            return None
        else:
            cursor = connection.cursor(dictionary=True) #come visto a lezione 3/11
            query = """SELECT *
                        FROM automobile"""
            cursor.execute(query)
            for row in cursor:
                # creo oggetto auto
                auto = Automobile(row["codice"], row["marca"], row["modello"], row["anno"], row["posti"], row["disponibile"])
                automobili.append(auto)

            cursor.close()
            connection.close()
            return automobili


    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        automobili_cercate = []
        connection = get_connection()
        if connection is None:
            print("Connection failed")
            return None
        else:
            cursor = connection.cursor(dictionary=True)
            query = """ SELECT *
                        FROM automobile
                        WHERE modello = %s"""
            cursor.execute(query, (modello,))
            for row in cursor:
                auto = Automobile(row["codice"], row["marca"], row["modello"], row["anno"], row["posti"], row["disponibile"])
                automobili_cercate.append(auto)

            cursor.close()
            connection.close()
            return automobili_cercate

