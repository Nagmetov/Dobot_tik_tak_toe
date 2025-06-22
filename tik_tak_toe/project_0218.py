#Magician
import time

Z_UP = 10
Z_DOWN = -5
print(1)

def move_to(x, y, z):
    dType.SetPTPCmd(api, 1, x, y, z, 0, 1)
    time.sleep(0.5)

def read_contour_coordinates(filename="contour_coordinates.txt"):
    print(2)
    contours = []
    current_contour = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip() == "---":
                if current_contour:
                    contours.append(current_contour)
                    current_contour = []
            else:
                x, y = map(float, line.strip().split(","))
                current_contour.append((x, y))
    return contours

def draw_contours(api):
    print(3)
    contours = read_contour_coordinates()
    for contour in contours:
        if not contour:
            continue
        
        move_to(contour[0][0], contour[0][1], Z_UP)
        move_to(contour[0][0], contour[0][1], Z_DOWN)
        
        for point in contour[1:]:
            move_to(point[0], point[1], Z_DOWN)

        move_to(point[0], point[1], Z_UP)

x = 1
if x:
    print(4)
    dType.SetPTPCommonParams(api, 250, 250)
    
    while True:
        try:
            with open("contour_coordinates.txt", "r"):
                break
        except FileNotFoundError:
            print("пипи")
            time.sleep(1)
    
    draw_contours(api)
    
    dType.SetPTPCmd(api, 1, 0, 0, Z_UP, 0, 1)
    print("сосичка.")