# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 11:13:29 2024

@author: jorge
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# Parámetros iniciales
L_total = 0.8  # Longitud inicial del tubo (8 segmentos de 0.1 m cada uno)
c = 343  # Velocidad del sonido (m/s)
frecuencia = 500  # Frecuencia inicial (Hz)
omega = 2 * np.pi * frecuencia  # Frecuencia angular
k = omega / c  # Número de onda
fps = 30  # Cuadros por segundo
t_max = 0.02  # Duración de la animación
x = np.linspace(0, L_total, 500)  # Dominio espacial
t = np.linspace(0, t_max, fps)  # Dominio temporal

# Configuración de la figura
fig, ax = plt.subplots(figsize=(12, 6))
plt.subplots_adjust(bottom=0.3)  # Espacio para sliders
linea, = ax.plot([], [], lw=3, color="blue")
ax.set_xlim(0, L_total)
ax.set_ylim(-2, 2)
ax.set_title("Onda estacionaria interactiva en un tubo")
ax.set_xlabel("Posición (x) [m]")
ax.set_ylabel("Amplitud")
ax.grid(True, linestyle="--", alpha=0.7)

# Añadir sliders para frecuencia y longitud del tubo
eje_frecuencia = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor="lightgoldenrodyellow")
eje_longitud = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor="lightgoldenrodyellow")
slider_frecuencia = Slider(eje_frecuencia, "Frecuencia (Hz)", 100, 1000, valinit=frecuencia, valstep=10)
slider_longitud = Slider(eje_longitud, "Longitud del tubo (m)", 0.1, 2.0, valinit=L_total, valstep=0.1)

# Función de inicialización
def inicializar():
    linea.set_data([], [])
    return linea,

# Función de actualización para la animación
def actualizar(i):
    global omega, k
    omega = 2 * np.pi * slider_frecuencia.val  # Actualizar la frecuencia angular
    k = omega / c  # Actualizar el número de onda
    x_nuevo = np.linspace(0, slider_longitud.val, 500)  # Ajustar el dominio espacial
    y = 2 * np.sin(k * x_nuevo) * np.cos(omega * t[i])  # Ecuación de onda estacionaria
    linea.set_data(x_nuevo, y)
    ax.set_xlim(0, slider_longitud.val)  # Ajustar los límites del eje x
    return linea,

# Crear la animación
ani = FuncAnimation(fig, actualizar, init_func=inicializar, frames=len(t), interval=1000/fps, blit=True)

# Mostrar el gráfico interactivo
plt.show()
