import random
import time

# Función para simular el movimiento en dos dimensiones hacia una posición objetivo
def simulate_two_dimensional(target_position, max_jumps):
    start_time = time.time()  # Registra el tiempo de inicio de la simulación
    position = [0, 0]  # Inicializa la posición actual en [0, 0]

    for jump in range(max_jumps):
        step_x = random.choice([-1, 1])  # Salto aleatorio en la coordenada x
        step_y = random.choice([-1, 1])  # Salto aleatorio en la coordenada y

        position[0] += step_x  # Actualiza la posición en x
        position[1] += step_y  # Actualiza la posición en y

        # Verifica si la posición actual coincide con la posición objetivo
        if position == target_position:
            end_time = time.time()  # Registro del tiempo de finalización
            elapsed_time = end_time - start_time
            return jump + 1, elapsed_time

        # Verifica si la posición está cerca de la posición objetivo
        if (
                abs(position[0] - target_position[0]) <= 1 and
                abs(position[1] - target_position[1]) <= 1
        ):
            end_time = time.time()  # Registro del tiempo de finalización
            elapsed_time = end_time - start_time
            return jump + 1, elapsed_time

    # Si no se alcanza la posición objetivo, devuelve valores indicativos
    return -1, -1

target_position = [250, 300]  # Posición objetivo en dos dimensiones
max_jumps = 100000000  # Número máximo de saltos permitidos

# Llama a la función de simulación
num_jumps_to_target, elapsed_time = simulate_two_dimensional(target_position, max_jumps)

# Imprime los resultados de la simulación
if num_jumps_to_target != -1:
    print(f"Brincos necesarios para llegar a la posición {target_position}: {num_jumps_to_target}")
    print(f"Tiempo empleado: {elapsed_time} segundos")
else:
    print("La rana no llegó a la posición objetivo en los brincos máximos permitidos.")
