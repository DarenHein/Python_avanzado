
import tqdm as tq

# Decide cuántas iteraciones tendrá tu proceso
iteraciones = 100
barra = tq.tqdm(total=iteraciones, desc="Proceso")

for i in range(iteraciones):
    # Simula el trabajo de tu proceso aquí
    # Puedes reemplazar esta línea con tu propia lógica
    import time
    time.sleep(0.1)  # Simulación de trabajo durante 0.1 segundos

    # Actualiza la barra de progreso
    barra.update(1)
    barra.set_description(f"Proceso ({i + 1}/{iteraciones})")

barra.close()
print("Proceso completado")

