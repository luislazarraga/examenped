class Bolos():
    def error(self, juego):
        for i in range(0, len(juego)):
            ronda = juego[i]
            if ronda[0] or ronda[1] > 10 or ronda[0][1] < 0 or sum(ronda) > 10:
                raise ExcepcionBolos

    def calcularResultado(self, juego):
        suma = 0
        for i in range(0, len(juego)):
            if (i < 10):
                ronda = juego[i]
                if (sum(ronda) <= 9): # Tratamiento de rondas sin strike ni spare
                    suma = suma + sum(ronda)
                elif ronda[0] == 10:  # Tratamiento Strikes
                    proxima_ronda = juego[i + 1]
                    if (proxima_ronda[0] == 10):  # Tratamiento Strikes seguidos
                        siguiente_a_prox = juego[i + 2][0]
                        suma = suma + sum(ronda) + sum(proxima_ronda) + siguiente_a_prox
                    else:  # Tratamiento Strike único
                        suma = sum(ronda) + suma + sum(proxima_ronda)
                elif ronda[0] != 10 and sum(ronda) == 10:  # Tratamiento spare
                    proxima_tirada = juego[i + 1][0]
                    suma = suma + sum(ronda) + proxima_tirada
            elif (i == 9):  # Tratamiento ronda 10
                ronda = juego[i]
                if ronda[0] == 10:  # Ronda 10 es Strike
                    proxima_ronda = juego[i + 1]
                    if (proxima_ronda[0] == 10):
                        ultima_tirada = juego[i + 2][0]
                        suma = suma + sum(ronda) + sum(proxima_ronda) + ultima_tirada
                    else:
                        suma = suma + sum(ronda) + sum(proxima_ronda)
                elif sum(ronda) == 10 and ronda[0] != 10:  # Ronda 10 es spare
                    proxima_tirada = juego[i + 1][0]
                    suma = sum(ronda) + proxima_tirada
        return suma


class ExcepcionBolos(Exception):
    pass