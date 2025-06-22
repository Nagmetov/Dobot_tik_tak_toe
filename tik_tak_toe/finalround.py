#Magician
import time

dType.SetPTPCommonParams(api, 250, 250)  # SpeedALL
dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final

moveToFlag = -26  # 5 tower moveToFlag

def decrement_moveToFlag():
    global moveToFlag
    moveToFlag -= 6

def move_to_1():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 191, -51, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 191, -51, -55, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 191, -51, 0, 0, 6)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def move_to_2():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 191, 0, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 191, 0, -55, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 191, 0, 0, 0, 6)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def move_to_3():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 191, 51, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 191, 51, -55, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 191, 51, 0, 0, 6)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def move_to_4():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 255, -55, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 255, -55, -55, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 255, -55, 0, 0, 6)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def move_to_5():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 255, 0, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 255, 0, -55, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 255, 0, 0, 0, 8)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def move_to_6():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 255, 60, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 255, 60, -55, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 255, 60, 0, 0, 6)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def move_to_7():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 314, -50, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 314, -50, -45, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 314, -50, 0, 0, 6)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def move_to_8():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 314, 0, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 314, 0, -55, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 314, 0, 0, 0, 6)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def move_to_9():
    dType.SetPTPCmd(api, 1, 263, -140, 0, 0, 1)  # AboveStock
    dType.SetPTPCmd(api, 1, 263, -140, moveToFlag, 0, 2)  # ComeSuck
    dType.SetEndEffectorSuctionCup(api, 1, 1, 3)  # SuctOn
    dType.SetPTPCmd(api, 1, 260, -140, 0, 0, 4)  # SuctUp
    dType.SetPTPCmd(api, 1, 314, 60, 0, 0, 5)  # UpOnEnd
    dType.SetPTPCmd(api, 1, 314, 60, -55, 0, 6)  # Down
    dType.SetEndEffectorSuctionCup(api, 0, 1, 7)  # SuctOff
    dType.SetPTPCmd(api, 1, 314, 60, 0, 0, 6)  # EndUp
    dType.SetPTPCmd(api, 1, -15, -200, 0, 0, 6)  # Final
    decrement_moveToFlag()

def loose():
	dType.SetPTPCommonParams(api, 50, 50)
	dType.SetPTPCmd(api, 1, 255, 50, 50, 0, 1)
	dType.SetPTPCmd(api, 1, 255, -50, 50, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 50, 50, 0, 1)
	dType.SetPTPCmd(api, 1, 255, -50, 50, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 50, 50, 0, 1)
	dType.SetWAITCmd(api, 800, 1)
	dType.SetPTPCmd(api, 1, 200, 0, 0, 0, 1)
	dType.SetPTPCommonParams(api, 500, 500)

def win():
	dType.SetPTPCommonParams(api, 500, 500)
	dType.SetPTPCmd(api, 1, 255, 0, 100, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 75, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 100, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 75, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 100, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 75, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 100, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 75, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 100, 0, 1)
	dType.SetPTPCmd(api, 1, 255, 0, 75, 0, 1)
	dType.SetPTPCommonParams(api, 250, 250)

file_path = 'C:\\Users\\ADMIN\\PycharmProjects\\DOBOT\\tik_tak_toe\\step.txt'  # Path to the file
check_interval = 1  # Interval for checking the file (in seconds)
last_content = ""
data = []
move_number = 0

print("Initial move_number:", move_number)

while True:
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if content != last_content:
                last_content = content
                data = [int(num.strip()) for num in content.split(',') if num.strip().isdigit()]
                if data:  # Check if the data list is not empty
                    move_number = data[0]  # Update move_number with the first element of data
                    if move_number == 1:
                        move_to_1()
                    elif move_number == 2:
                        move_to_2()
                    elif move_number == 3:
                        move_to_3()
                    elif move_number == 4:
                        move_to_4()
                    elif move_number == 5:
                        move_to_5()
                    elif move_number == 6:
                        move_to_6()
                    elif move_number == 7:
                        move_to_7()
                    elif move_number == 8:
                        move_to_8()
                    elif move_number == 9:
                        move_to_9()
                    elif move_number == 11:
                        loose()
                    elif move_number == 10:
                        win()
                print("Current data:", data)
                print("Updated move_number:", move_number)
        time.sleep(check_interval)
    except FileNotFoundError:
        print("File not found. Retrying in", check_interval, "seconds.")
        time.sleep(check_interval)
    except KeyboardInterrupt:
        print("Stopping file monitoring.")
        break
