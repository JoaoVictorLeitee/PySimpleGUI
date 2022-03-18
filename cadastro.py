from PySimpleGUI import PySimpleGUI as sg
from numpy import size

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(25, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(25, 1))],
    [sg.Checkbox('Salvar Login')],
    [sg.Button('Entrar')]
]

# Janela
janela = sg.Window('Tela de Login', layout)

# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'victor' and valores['senha'] == '1234':
            print('Bem Vindo Victor')
