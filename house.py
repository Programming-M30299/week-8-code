from graphix import Window, Point, Rectangle, Polygon


def main():
    # `get_inputs` returns two values, so we need to receive them both
    door_colour, lights_on = get_inputs()
    draw_house(door_colour, lights_on)


def get_inputs():
    door_colour = input("Enter door colour: ")
    lights_yn = input("Are the lights on (y/n): ")
    # Check if the first character (index 0) of lights_yn is "y"
    if lights_yn[0] == "y":
        lights_on = True
    else:
        lights_on = False
    # We are returning two values (observe how we receive them in `main`)
    return door_colour, lights_on


def draw_house(door_colour, lights_on):
    win = Window("House", 200, 200)
    list_of_points = [Point(0, 60), Point(100, 0), Point(200, 60)]
    roof = Polygon(list_of_points)
    roof.fill_colour = "pink"
    roof.outline_colour = "pink"
    roof.draw(win)

    # draw wall and door
    draw_rectangle(win, Point(2, 60), Point(198, 198), "brown")
    draw_rectangle(win, Point(30, 110), Point(80, 198), door_colour)

    # draw window
    if lights_on:
        window_colour = "yellow"
    else:
        window_colour = "black"
    draw_rectangle(win, Point(110, 110), Point(170, 170), window_colour)


def draw_rectangle(win, point1, point2, colour):
    rectangle = Rectangle(point1, point2)
    rectangle.fill_colour = colour
    rectangle.outline_colour = colour
    rectangle.draw(win)


main()
