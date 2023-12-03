import matplotlib.pyplot as plt

def liang_barsky(x_min, y_min, x_max, y_max, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    p = [-dx, dx, -dy, dy]
    q = [x1 - x_min, x_max - x1, y1 - y_min, y_max - y1]
    t_enter = 0.0
    t_exit = 1.0

    for i in range(4):
        if p[i] == 0:  # Check if line is parallel to the clipping boundary
            if q[i] < 0:
                return None  # Line is outside and parallel, so completely discarded
        else:
            t = q[i] / p[i]
            if p[i] < 0:
                if t > t_enter:
                    t_enter = t
            else:
                if t < t_exit:
                    t_exit = t

    if t_enter > t_exit:
        return None  # Line is completely outside

    x1_clip = x1 + t_enter * dx
    y1_clip = y1 + t_enter * dy
    x2_clip = x1 + t_exit * dx
    y2_clip = y1 + t_exit * dy

    return x1_clip, y1_clip, x2_clip, y2_clip

points = []

def onclick(event):
    x, y = event.xdata, event.ydata
    points.append((x, y))
    if len(points) == 2:
        x1, y1 = points[0]
        x2, y2 = points[1]
        clipped_line = liang_barsky(x_min, y_min, x_max, y_max, x1, y1, x2, y2)
        if clipped_line is not None:
            x1_clip, y1_clip, x2_clip, y2_clip = clipped_line
            plt.plot([x1, x2], [y1, y2], 'r', label='Original Line')
            plt.plot([x1_clip, x2_clip], [y1_clip, y2_clip], 'yellow', label='Clipped Line')
            plt.title('Liang-Barsky Line Clipping Algorithm')
            plt.legend()
        else:
            plt.title('Line is outside the clipping window')
        plt.show()
        points.clear()

x_min, y_min = 20, 20
x_max, y_max = 80, 80

plt.figure(figsize=(8, 6))

plt.plot([x_min, x_max, x_max, x_min, x_min], [y_min, y_min, y_max, y_max, y_min], 'b', label='Clipping Window')

plt.title('Left click to select points. Select two points.')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.axis('equal')

plt.gcf().canvas.mpl_connect('button_press_event', onclick)
plt.show()