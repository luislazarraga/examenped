# Kata funcional -- rgg

def calcular_resultado(partida):
    return sum(valor_total(*bolas) for bolas in iterador(partida, antes=1, despues=2, relleno='0'))

def valor_total(anterior, bola, siguiente1, siguiente2):
    return valor(bola, valor(anterior)) + bonus(bola, siguiente1, siguiente2)

def valor(bola, anterior = 0):
    valores = {
        'X': lambda b,a: 10,
        '/': lambda b,a: 10-a,
    }
    calculador = valores.get(bola, lambda b,a: int(b))
    return calculador(bola, anterior)

def bonus(bola, siguiente1, siguiente2):
    extras = {
            'X': lambda s1,s2: valor(s1)+valor(s2),
            '/': lambda s1,s2: valor(s1),
    }
    calculador = extras.get(bola, lambda b1,b2: 0)
    return calculador(siguiente1, siguiente2)

def iterador(partida, antes=0, despues=0, relleno=None):
    recorrido = [relleno]*antes + list(partida) + [relleno]*despues
    for i, _ in enumerate(partida):
        yield recorrido[i : i+1 + antes+despues]
