def indice_qualite(pm25):
    if pm25 <= 10:
        return "Bon"
    elif pm25 <= 25:
        return "Moyen"
    return "Mauvais"
