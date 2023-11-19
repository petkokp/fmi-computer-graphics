import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from shapely.geometry import Point
import time

def draw_circle(ax, center, radius, color):
    circle = Circle(center, radius, edgecolor=color, facecolor='none')
    ax.add_patch(circle)

def fill_recursive(ax, polygon, fill_color, alpha):
    if polygon.geom_type == 'Polygon':
        x, y = polygon.exterior.xy
        ax.fill(x, y, fill_color, alpha=alpha)
        plt.draw()
        time.sleep(0.5)
       
    elif polygon.geom_type == 'MultiPolygon':
        for part in polygon:
            if part.geom_type == 'Polygon':
                fill_recursive(ax, part, fill_color, alpha)
            
def fill_circle_symmetric_difference(ax, center1, radius1, center2, radius2, fill_color):
    circle1 = Point(center1).buffer(radius1)
    circle2 = Point(center2).buffer(radius2)

    symmetric_difference_polygon = circle1.symmetric_difference(circle2)
    
    draw_circle(ax, center1, radius1, color='blue')

    draw_circle(ax, center2, radius2, color='orange')
    
    fill_recursive(ax, symmetric_difference_polygon, fill_color='green', alpha=0.5)

    plt.show()
    
    try:
        print("Click on a point to check if it's in the symmetric difference area:")
        point_x, point_y = plt.ginput(1)[0]

        point = Point(point_x, point_y)

        # Change point validation code to verify whether the Point is within circle1 and circle2 or not.
        if point.within(symmetric_difference_polygon):
            print(f"The point ({point_x}, {point_y}) is within the symmetric difference area.")
            print("Filling the symmetric difference area gradually in red...")

            # Gradually fill the symmetric difference area in red using recursion
            fill_recursive(ax, symmetric_difference_polygon, fill_color='red', alpha=1)

            print("Filling completed.")
            plt.show()
        else:
            print(f"The point ({point_x}, {point_y}) is not within the symmetric difference area.")
    except ValueError:
        print("Невалиден вход.")
    except KeyboardInterrupt:
        print("\nПроцесът е прекъснат.")

def fill_circle_difference(ax, center1, radius1, center2, radius2, fill_color):
    # Create Shapely circles
    circle1 = Point(center1).buffer(radius1)
    circle2 = Point(center2).buffer(radius2)

    # Find difference of two circles
    difference_polygon = circle1.difference(circle2)

    # Plot the first circle
    draw_circle(ax, center1, radius1, color='blue')

    # Plot the second circle
    draw_circle(ax, center2, radius2, color='orange')

    # Plot the filled difference area in green
    fill_recursive(ax, difference_polygon, fill_color='green', alpha=0.5)

    # Show the plot
    plt.show()

    # Get a point from the user
    try:
        print("Избери точка в областта на разликата:")
        point_x, point_y = plt.ginput(1)[0]

        point = Point(point_x, point_y)

        # Change point validation code to verify whether the Point is within circle1 but not in circle2
        if point.within(circle1) and not point.within(circle2):
            print(f"Точката ({point_x}, {point_y}) е в областта на разликата.")
            print("Запълване...")

            # Gradually fill the difference area in red using recursion
            fill_recursive(ax, difference_polygon, fill_color='red', alpha=1)

            print("Запълнено.")
            plt.show()
        else:
            print(f"Точката ({point_x}, {point_y}) не е в областта на разликата..")
    except ValueError:
        print("Невалиден вход.")
    except KeyboardInterrupt:
        print("\nПроцесът е прекъснат.")

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Define circles
center1 = []
radius1 = 0
center2 = []
radius2 = 0

# Set constant x and y axis limits
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

def onclick(event):
    global center1, center2, radius1, radius2

    if not center1:
        center1 = [event.xdata, event.ydata]
        print("Избери радиус 1:")
    elif radius1 == 0:
        radius1 = abs(event.xdata - center1[0])
        draw_circle(ax, center1, radius1, color='blue')
        print("Избери център 2:")
    elif not center2:
        center2 = [event.xdata, event.ydata]
        print("Избери радиус 2:")
    elif radius2 == 0:
        radius2 = abs(event.xdata - center2[0])
        draw_circle(ax, center2, radius2, color='orange')

        # fill_circle_symmetric_difference(ax, center1, radius1, center2, radius2, fill_color='green')
        fill_circle_difference(ax, center1, radius1, center2, radius2, fill_color='green')

# Connect the event handler
fig.canvas.mpl_connect('button_press_event', onclick)

print("Избери център 1:")

plt.show()