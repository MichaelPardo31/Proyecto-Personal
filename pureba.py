import tkinter as tk
import math

# Configuración de la ventana
window = tk.Tk()
window.title("Triángulo Girando con Pelota Rebotando")
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.pack()

# Configuración del triángulo
triangle_size = 150
triangle_points = [
    200, 100,  # Punto superior
    100, 300,  # Punto inferior izquierdo
    300, 300   # Punto inferior derecho
]
triangle = canvas.create_polygon(triangle_points, outline="white", fill="black")

# Configuración de la pelota
ball_radius = 20
ball = canvas.create_oval(200 - ball_radius, 200 - ball_radius, 200 + ball_radius, 200 + ball_radius, fill="yellow")
ball_speed = [3, 3]  # Velocidad en x e y

# Ángulo de rotación del triángulo
angle = 0

def rotate_triangle():
    global angle
    angle += 1  # Incrementa el ángulo de rotación
    if angle >= 360:
        angle = 0
    
    # Calcula las nuevas coordenadas del triángulo
    new_points = []
    for i in range(0, len(triangle_points), 2):
        x = triangle_points[i] - 200
        y = triangle_points[i+1] - 200
        new_x = x * math.cos(math.radians(angle)) - y * math.sin(math.radians(angle))
        new_y = x * math.sin(math.radians(angle)) + y * math.cos(math.radians(angle))
        new_points.append(new_x + 200)
        new_points.append(new_y + 200)
    
    # Actualiza las coordenadas del triángulo
    canvas.coords(triangle, *new_points)
    
    # Programa la próxima rotación
    window.after(20, rotate_triangle)

def move_ball():
    # Mueve la pelota
    canvas.move(ball, ball_speed[0], ball_speed[1])
    
    # Obtiene las coordenadas actuales de la pelota
    x1, y1, x2, y2 = canvas.coords(ball)
    
    # Rebotar en los bordes del triángulo
    # Para simplificar, rebota en los bordes de la ventana
    if x1 <= 0 or x2 >= 400:
        ball_speed[0] = -ball_speed[0]
    if y1 <= 0 or y2 >= 400:
        ball_speed[1] = -ball_speed[1]
    
    # Programa el próximo movimiento
    window.after(20, move_ball)

# Inicia la rotación del triángulo y el movimiento de la pelota
rotate_triangle()
move_ball()

# Inicia el bucle principal de la ventana
window.mainloop()
