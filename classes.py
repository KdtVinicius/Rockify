from os import system
import json

class Musica:
    def __init__ (self, id, nome, album, banda):
        self.id = id
        self.nome = nome
        self.album = album
        self.banda = banda
    
    def __str__(self):
        return f'{self.nome} - {self.banda} | {self.album}'

# -------------------------------------------------------------------------------------------------------------

class NMusica:
    musicas = []
    
    @classmethod
    def inserir (cls, musica):
        cls.musicas.append(musica)
    
    @classmethod
    def listar (cls):
        return cls.musicas
        
    @classmethod
    def excluir (cls, m):
        removeu = False
        for musica in cls.musicas:
            if (m.id == musica.id):
                cls.musicas.remove(musica)
                removeu = True
        
        return removeu
    
    @classmethod
    def salvar(cls):
        with open('./musicas.json', mode="w") as arquivo:
            json.dump(cls.musicas, arquivo, default=lambda m: m.__dict__)

    @classmethod
    def abrir(cls):
        cls.musicas = []
        with open('./musicas.json', mode="r") as arquivo:
            musicas_json = json.load(arquivo)
            for m in musicas_json:
                musica = Musica(m['id'], m['nome'], m['album'], m['banda'])
                cls.musicas.append(musica)

# -------------------------------------------------------------------------------------------------------------

class PlayListItem:
    def __init__(self, id, musicaId, playlistId):
        self.id = id
        self.musicaId = musicaId
        self.playlistId = playlistId

# -------------------------------------------------------------------------------------------------------------

class NPlayListItems:
    items = []
    
    @classmethod
    def inserir_musica_playlist(cls, musica, playlist):
        if (len(cls.items) == 0): id = 0
        else: id = len(cls.items) + 1
        item = PlayListItem(id, musica.id, playlist.id)
        cls.items.append(item)

    @classmethod
    def remover_musica_playlist(cls, musica, playlist):
        removeu = False
        for item in cls.items:
            if (musica.id == item.musicaId and playlist.id == item.playlistId):
                removeu = True
                cls.items.remove(item)
        
        return removeu

# -------------------------------------------------------------------------------------------------------------

class Playlist:
    def __init__ (self, id, nome):
        self.id = id
        self.nome = nome
        self.idUsuario = 0
        
    def __str__ (self):
        return f'{self.nome}'
        
# -------------------------------------------------------------------------------------------------------------

class NPlaylist:
    playlists = []
    
    @classmethod
    def inserir (cls, playlist):
        cls.playlists.append(playlist)
    
    @classmethod
    def listar (cls):
        return cls.playlists
        
    @classmethod
    def excluir (cls, p):
        removeu = False
        for playlist in cls.playlists:
            if (p.id == playlist.id):
                cls.playlists.remove(playlist)
                removeu = True
        
        return removeu
    
    @classmethod
    def salvar(cls):
        with open('./playlists.json', mode="w") as arquivo:
            json.dump(cls.playlists, arquivo, default=lambda p: p.__dict__)

    @classmethod
    def abrir(cls):
        cls.playlists = []
        with open('./playlists.json', mode="r") as arquivo:
            playlists_json = json.load(arquivo)
            for p in playlists_json:
                playlist = Playlist(p['id'], p['nome'])
                cls.playlists.append(playlist)

# -------------------------------------------------------------------------------------------------------------
   
class Usuario:
    def __init__ (self, id, nome):
        self.id = id
        self.nome = nome
        self.idUsuario = 0
        
    def __str__ (self):
        return f'{self.nome}'

# -------------------------------------------------------------------------------------------------------------

class NUsuario:
    usuarios = []
    
    @classmethod
    def inserir (cls, usuario):
        cls.usuarios.append(usuario)
    
    @classmethod
    def listar (cls):
        return cls.usuarios
        
    @classmethod
    def excluir (cls, u):
        removeu = False
        for usuario in cls.usuarios:
            if (u.id == usuario.id):
                cls.usuarios.remove(usuario)
                removeu = True
        
        return removeu

    @classmethod
    def salvar(cls):
        with open('./usuarios.json', mode="w") as arquivo:
            json.dump(cls.usuarios, arquivo, default=lambda u: u.__dict__)

    @classmethod
    def abrir(cls):
        cls.usuarios = []
        with open('./usuarios.json', mode="r") as arquivo:
            usuarios_json = json.load(arquivo)
            for p in usuarios_json:
                usuario = Usuario(p['id'], p['nome'])
                cls.usuarios.append(usuario)

# -------------------------------------------------------------------------------------------------------------

class Admin (Usuario):
    def __init__ (self, id, nome):
        super().init(id, nome)

# -------------------------------------------------------------------------------------------------------------

class Menu:
    def __init__ (self):
        pass
    
    def exibir (self):
        system('cls')
        print('''
Bom dia! Bem vindo ao Rockify.
Escolha uma opção abaixo:
1 - Adicionar musica no app
2 - Remover musica do app
3 - Listar musicas do app
4 - Adicionar playlist no app
5 - Remover playlist do app
6 - Listar playlists do app
7 - Adicionar usuario no app
8 - Remover usuario do app
9 - Listar usuarios do app
10 - Adicionar musica em uma playlist
11 - Remover musica de uma playlist
0 - Sair
        ''')
        return int(input())
    
    def addMusica (self):
        system('cls')
        print('Digite, respectivamente: id, nome, album e banda da musica: ')
        m = Musica(int(input()), input(), input(), input())
        NMusica.inserir(m)
        NMusica.salvar()
        print('Musica inserida com sucesso!')
        
    def removeMusica (self):
        system('cls')
        print('Escolha uma musica para remover: ')
        musicas = NMusica.listar()
        for i in range(len(musicas)):
            print(f'{i+1} - {musicas[i]}')
        opc = int(input())
        removeu = NMusica.excluir(musicas[opc-1])
        if (removeu):
            print('Musica removida com sucesso!')
        else:
            print('ERRO: Musica não removida')
        
    def listMusica (self):
        system('cls')
        print('Lista de musicas: ')
        musicas = NMusica.listar()
        for i in range(len(musicas)):
            print(f'{i+1} - {musicas[i]}')
        input('Press qqr tecla')
        
    def addPlaylist (self):
        system('cls')
        print('Digite, respectivamente: id e nome da playlist: ')
        p = Playlist(int(input()), input())
        NPlaylist.inserir(p)
        NPlaylist.salvar()
        print('Playlist inserida com sucesso!')
        
    def removePlaylist (self):
        system('cls')
        print('Escolha uma playlist para remover: ')
        playlists = NPlaylist.listar()
        for i in range(len(playlists)):
            print(f'{i+1} - {playlists[i]}')
        opc = int(input())
        removeu = NPlaylist.excluir(playlists[opc-1])
        if (removeu):
            print('Playlist removida com sucesso!')
        else:
            print('ERRO: Playlist não removida')
        
    def listPlaylist (self):
        system('cls')
        print('Lista de playlists: ')
        playlists = NPlaylist.listar()
        for i in range(len(playlists)):
            print(f'{i+1} - {playlists[i]}')
        input('Press qqr tecla')
            
    def addUsuario (self):
        print('Digite, respectivamente: id e nome do usuario: ')
        u = Usuario(int(input()), input())
        NUsuario.inserir(u)
        NUsuario.salvar()
        print('Usuario inserido com sucesso!')
        
    def removeUsuario (self):
        system('cls')
        print('Escolha um usuario para remover: ')
        usuarios = NUsuario.listar()
        for i in range(len(usuarios)):
            print(f'{i+1} - {usuarios[i]}')
        opc = int(input())
        removeu = NUsuario.excluir(usuarios[opc-1])
        if (removeu):
            print('Usuario removido com sucesso!')
        else:
            print('ERRO: Usuario não removido')
        
    def listUsuario (self):
        system('cls')
        print('Lista de usuarios: ')
        usuarios = NUsuario.listar()
        for i in range(len(usuarios)):
            print(f'{i+1} - {usuarios[i]}')
        input('Press qqr tecla')
            
    def addMusicaPlay (self):
        system('cls')
        musicas = NMusica.listar()
        playlists = NPlaylist.listar()
        self.listMusica()
        opc = int(input('Escolha uma musica acima: '))
        system('cls')
        self.listPlaylist()
        opc2 = int(input('Escolha uma playlist acima: '))
        NPlayListItems.inserir_musica_playlist(musicas[opc-1], playlists[opc2-1])
        print(f'{musicas[opc-1].nome} foi adicionada com sucesso a {playlists[opc2-1].nome}!')
        
    def removeMusicaPlay (self):
        system('cls')
        musicas = NMusica.listar()
        playlists = NPlaylist.listar()
        self.listMusica()
        opc = int(input('Escolha uma musica acima: '))
        system('cls')
        self.listPlaylist()
        opc2 = int(input('Escolha uma playlist acima: '))
        NPlayListItems.remover_musica_playlist(musicas[opc-1], playlists[opc2-1])
        print(f'{musicas[opc-1].nome} foi adicionada com sucesso a {playlists[opc2-1].nome}!')