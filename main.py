from classes import *

m = Menu()

while True:
    opc = m.exibir()

    match opc:
        case 1:
            m.addMusica()
        case 2:
            m.removeMusica()
        case 3:
            m.listMusica()
        case 4:
            m.addPlaylist()
        case 5:
            m.removePlaylist()
        case 6:
            m.listPlaylist()
        case 7:
            m.addUsuario()
        case 8:
            m.removeUsuario()
        case 9:
            m.listUsuario
        case 10:
            m.addMusicaPlay()
        case 11:
            m.removeMusicaPlay()
        case 0:
            break