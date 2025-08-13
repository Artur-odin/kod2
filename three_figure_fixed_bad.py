import turtle

turtle.colormode(255)
scale = 50
fixed_distance = 100  # постоянное расстояние между фигурами

# Данные фигур: [углы поворота], [длины сторон], цвет, смещение по Y
rectangle = [[90, 90, 90, 90], [scale * 0.5, scale, scale * 0.5, scale], (245, 122, 31), 0]
rhomb = [[60, 120, 60, 120], [scale * 0.56, scale * 0.56, scale * 0.56, scale * 0.56], (245, 41, 22), scale * 0.25]
trapezoid = [[110, 70, 70, 110], [scale * 0.53, scale * 0.64, scale * 0.53, scale], (245, 188, 42), 0]

figures = [rectangle, rhomb, trapezoid]

turtle.penup()
for i, figure in enumerate(figures):
    angles, sides, color, y_offset = figure
    
    # Позиционирование с постоянным расстоянием
    turtle.goto(i * fixed_distance, y_offset)
    turtle.setheading(0)
    
    # Рисование фигуры
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    
    for angle, side in zip(angles, sides):
        turtle.left(angle)
        turtle.forward(side)
    
    turtle.end_fill()
    turtle.penup()

turtle.done()