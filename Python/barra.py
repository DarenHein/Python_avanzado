import time
from tqdm import tqdm

# Número total de elementos que deseas procesar
total_elements = 100

# Crear un objeto tqdm para la barra de carga
progress_bar = tqdm(total=total_elements, desc="Procesando")

# Simular algún proceso que toma tiempo
for _ in range(total_elements):
    # Simula el trabajo de tu proceso aquí
    time.sleep(0.1)  # Simulación de trabajo durante 0.1 segundos
    # Actualiza la barra de carga
    progress_bar.update(1)

# Cierra la barra de carga al finalizar
progress_bar.close()

print("Proceso completado")
