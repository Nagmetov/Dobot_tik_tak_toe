import time

dType.SetPTPCommonParams(api, 50, 50)


def getRid():
    dType.SetPTPCommonParams(api, 250, 250)
    dType.SetPTPCmd(api, 1, 130, -145, 73, 0, 1)
    dType.SetPTPCmd(api, 1, 0, -220, 75, 0, 1)
    dType.SetPTPCmd(api, 1, -3, -190, -30, 0, 1)
    dType.SetPTPCmd(api, 1, -3, -128, -30, 0, 1)
    dType.SetPTPCmd(api, 1, -3, -220, 0, 0, 1)
    dType.SetPTPCmd(api, 1, 0, -215, 75, 0, 1)
    dType.SetPTPCommonParams(api, 50, 50)


def Home_move():
    dType.SetPTPCmd(api, 1, 0, 240, 0, 0)
    dType.SetPTPCmd(api, 1, 0, 240, -100, 0)


def move_to_1():
    dType.SetPTPCmd(api, 1, 150, 0, 0, 0)
    dType.SetPTPCmd(api, 1, 150, 100, 0, 0, 1)
    dType.SetPTPCommonParams(api, 250, 250)
    dType.SetPTPCmd(api, 1, 280, 160, -20, 0)
    dType.SetPTPCmd(api, 1, 270, 180, -20, 0)
    dType.SetPTPCmd(api, 1, 150, 160, 0, 0, 1)
    dType.SetPTPCommonParams(api, 250, 250)
    getRid()


def move_to_2():
    dType.SetPTPCmd(api, 1, 150, 0, 0, 0)
    dType.SetPTPCmd(api, 1, 145, 30, 0, 0, 1)
    dType.SetPTPCmd(api, 1, 277, 90, -30, 0)
    dType.SetPTPCmd(api, 1, 275, 95, -30, 0)
    dType.SetPTPCmd(api, 1, 150, 30, 0, 0, 1)
    getRid()


def move_to_3():
    dType.SetPTPCmd(api, 1, 150, 0, 0, 0)
    dType.SetPTPCmd(api, 1, 150, 0, 0, 0, 1)
    dType.SetPTPCmd(api, 1, 275, 0, -30, 0)
    dType.SetPTPCmd(api, 1, 150, 0, 0, 0, 1)
    getRid()


def move_to_4():
    dType.SetPTPCmd(api, 1, 150, 0, 0, 0)
    dType.SetPTPCmd(api, 1, 150, -50, 0, 0, 1)
    dType.SetPTPCmd(api, 1, 280, -95, -10, 0)
    dType.SetPTPCmd(api, 1, 150, -50, 0, 0, 1)
    getRid()


def move_to_5():
    dType.SetPTPCmd(api, 1, 150, 0, 0, 0)
    dType.SetPTPCmd(api, 1, 150, -90, 0, 0, 1)
    dType.SetPTPCmd(api, 1, 280, -155, -30, 0)
    dType.SetPTPCmd(api, 1, 270, -145, -30, 0)
    dType.SetPTPCmd(api, 1, 200, -155, -30, 0)
    dType.SetPTPCmd(api, 1, 150, -90, 0, 0, 1)
    getRid()


def move_to_6():
    dType.SetPTPCmd(api, 1, 150, 0, 0, 0)
    dType.SetPTPCmd(api, 1, 150, -50, 0, 0, 1)
    dType.SetPTPCmd(api, 1, 265, -65, 145, 0)
    dType.SetPTPCmd(api, 1, -110, -200, 145, 0)


Home_move()

file_path = 'C:\\Users\\ADMIN\\PycharmProjects\\DOBOT\\sort_machine\\numbers.txt'  # Path to the file
check_interval = 1  # Interval for checking the file (in seconds)
last_content = None

while True:
    try:
        with open(file_path, 'r') as file:
            s = file.read().strip()
            if s:  # Check if the file is not empty
                print(123123123123)
                contents = [int(num) for num in s.split(',')]
                if contents != last_content:
                    last_content = contents
                    for content in contents:
                        if content == 1:
                            move_to_1()
                        elif content == 2:
                            move_to_2()
                        elif content == 3:
                            move_to_3()
                        elif content == 4:
                            move_to_4()
                        elif content == 5:
                            move_to_5()
                        elif content == 6:
                            move_to_6()
                    print("Current content:", contents)
            else:
                print("File is empty.")
        time.sleep(check_interval)
    except FileNotFoundError:
        print("File not found. Retrying in", check_interval, "seconds.")
        time.sleep(check_interval)
    except KeyboardInterrupt:
        print("Stopping file monitoring.")
        break