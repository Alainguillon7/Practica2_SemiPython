def inicializar(players):
    dic = {}
    for player in players:
        dic[player] = {}
        dic[player]["kills"] = 0
        dic[player]["assists"] = 0
        dic[player]["deaths"] = 0
        dic[player]["MVP"] = 0
        dic[player]["points"] = 0
    return dic


def getPoints(datos):
    points = 0
    points += datos["kills"] * 3
    points += datos["assists"]
    if datos["deaths"]:
        points -= 1
    return points


def getMVP(round):
    mvp = None
    max_points = -1

    for player, datos in round.items():
        points = getPoints(datos)
        if points > max_points:
            mvp = player
            max_points = points

    return mvp


def getFormat(dato):
    aux = 16 - len((dato))
    aux = aux // 2
    if len(dato) % 2 == 0:
        return " " * aux + dato + " " * aux + "|"
    else:
        return " " * aux + dato + " " * (aux + 1) + "|"


def print_round(partida, num):
    print(f"\nRanking Ronda {num}")
    print(
        "    Jugador     |       Kills     |   Asistencias   |     Muertes     |       MVPs      |   Puntos"
    )
    print("-" * 100)
    for player, datos in partida.items():
        print(
            getFormat(player),
            getFormat(str(datos["kills"])),
            getFormat(str(datos["assists"])),
            getFormat(str(datos["deaths"])),
            getFormat(str(datos["MVP"])),
            getFormat(str(datos["points"])),
        )
    print("-" * 100)
