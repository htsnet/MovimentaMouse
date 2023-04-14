import streamlit as st
import pyautogui
import time
import random

st.title("Movimento Aleatório do Mouse")

# returns the monitor size
screenWidth, screenHeight = pyautogui.size()

# Define as opções de configuração do movimento
x_range = st.slider("Faixa de Movimento Horizontal",
                    1, screenWidth, screenWidth * 0.9)
y_range = st.slider("Faixa de Movimento Vertical", 1,
                    screenHeight, screenHeight * 0.9)
interval = st.slider(
    "Intervalo de Tempo entre os Movimentos (segundos)", 1, 10, 4)

processo = False

# Cria um espaço vazio para mostrar as coordenadas
coordenadas_texto = st.empty()

# Divide a tela em duas colunas
col1, col2 = st.columns(2)

# Adiciona um botão na primeira coluna
with col1:
    start_movement = st.button("Iniciar Movimento")

# Adiciona um segundo botão na segunda coluna
with col2:
    stop_movement = st.button("Parar")

if stop_movement:
    processo = False

# Inicia o movimento
if start_movement:
    processo = True
    while processo:
        x_offset, y_offset = pyautogui.position()
        x_offset = abs(random.randint(-x_range, x_range))
        y_offset = abs(random.randint(-y_range, y_range))
        # st.write(f"Mouse Movido para ({x_offset}, {y_offset})")
        # Atualiza o espaço vazio com as novas coordenadas
        coordenadas_texto.text(f"Movendo para ({x_offset}, {y_offset})")
        pyautogui.moveTo(x_offset, y_offset, duration=0.5)
        time.sleep(interval)
