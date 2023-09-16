import random
import time


def simulate_three_dimensional(target_position, max_jumps):
    # Registra el tiempo de inicio de la simulación
    start_time = time.time()

    # Inicializa la posición actual en [0, 0, 0]
    position = [0, 0, 0]

    # Bucle que representa los saltos
    for jump in range(max_jumps):
        # Genera saltos aleatorios en las tres dimensiones
        step_x = random.choice([-1, 1])
        step_y = random.choice([-1, 1])
        step_z = random.choice([-1, 1])

        # Actualiza la posición actual en las tres dimensiones
        position[0] += step_x
        position[1] += step_y
        position[2] += step_z

        # Verifica si la posición está cerca de la posición objetivo
        if (
                abs(position[0] - target_position[0]) <= 1 and
                abs(position[1] - target_position[1]) <= 1 and
                abs(position[2] - target_position[2]) <= 1
        ):
            # Registra el tiempo transcurrido
            end_time = time.time()
            elapsed_time = end_time - start_time

            # Devuelve el número de saltos necesarios y el tiempo transcurrido
            return jump + 1, elapsed_time

    # Si no se alcanza la posición objetivo, registra el tiempo transcurrido
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Devuelve -1 para indicar que no se alcanzó la posición objetivo y el tiempo transcurrido
    return -1, elapsed_time


target_position = [45, 23, 17]
max_jumps = 1000000000

# Llama a la función de simulación
num_jumps_to_target, elapsed_time = simulate_three_dimensional(target_position, max_jumps)

# Imprime los resultados de la simulación
if num_jumps_to_target != -1:
    print(f"Brincos necesarios para llegar a la posición {target_position}: {num_jumps_to_target}")
    print(f"Tiempo empleado: {elapsed_time} segundos")
else:
    print("La rana no llegó cerca a la posición objetivo en los brincos máximos permitidos.")
    print(f"Tiempo empleado: {elapsed_time} segundos")
