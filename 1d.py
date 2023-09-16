import random
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

positionFinal = 0

# Función para realizar un salto aleatorio
def jump(position):
    direction = random.randint(0, 1)
    if direction == 0:
        return position + 1
    else:
        return position - 1

# Función para simular una serie de saltos
def simulate(n):
    position = 0
    positions = []
    for i in range(n):
        position = jump(position)
        positions.append(position)

    global positionFinal
    positionFinal = positions[-1]

    return positions

# Función para graficar las posiciones y mostrar la posición final y el tiempo transcurrido
def plot_positions(root, positions, start_time):
    fig, ax = plt.subplots()
    ax.plot(positions)
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Posición')
    ax.set_title('Posición de la rana a lo largo del tiempo')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    end_time = time.time()
    elapsed_time = end_time - start_time

    position_final_label = Label(root, text="Posición final: {} Tiempo transcurrido: {:.2f} segundos".format(positionFinal, elapsed_time))
    position_final_label.pack()

# Función principal
def main():
    root = Tk()
    root.title("Simulación de Salto de Rana")
    label = Label(root, text="Simulación para saber la posición final de la rana en el millonésimo salto")
    label.pack()

    button2 = Button(root, text="Simulate", command=lambda: simulate_and_plot(root))
    button2.pack()

    root.mainloop()

# Función para realizar la simulación y graficar
def simulate_and_plot(root):
    start_time = time.time()
    positions = simulate(int(1000000))
    plot_positions(root, positions, start_time)

if __name__ == "__main__":
    main()
