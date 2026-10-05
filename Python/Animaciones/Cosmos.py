import tkinter as tk 
import random
import math

root = tk.Tk()
root.title('[+] Violet Galaxy')
root.geometry('800x600')

canvas = tk.Canvas(root,
    width = 800,
    height= 600,
    bg = '#080018')

canvas.pack()
stars = []

for _ in range(250):
    stars.append([
        random.uniform(0, math.pi * 2),
        random.uniform(20, 350),
        random.uniform(0.5, 2)
    ])

angle = 0

def animate():
    global angle

    angle += 0.008
    canvas.create_rectangle(
        0, 0, 800, 600,
        fill = '#080018',
        outline = ''
    )

    for r in range(100, 40, -20):
        canvas.create_oval(
            400 - r * 1.5,
            300 - r * 0.5,
            400 + r * 1.5,
            300 + r * 0.5,
            outline = '#35105c'
        )

    for a, radius, size in stars:

        x = 400 + math.cos(a + angle) * radius
        y = 300 + math.sin(a + angle) * radius

        canvas.create_oval(
            x - size, y - size,
            x + size, y + size,
            fill = '#e8c7ff',
            outline = ''
        )

    canvas.create_oval(
        380, 280, 420, 320,
        fill = '#ffffff',
        outline = ''
    )

    root.after(30, animate)

animate()
root.mainloop()