"""
Using a fake robot as the receiver of messages.
"""

# Doe: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# Done: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time

class DelegateThatReceives(object):

    def Forward(self, leftspeed,rightspeed):
        print("Forward",leftspeed,rightspeed)
    def Backward(self, leftspeed,rightspeed):
        print("Backward",leftspeed,rightspeed)
    def Arm_Up(self):
        print("Arm Up")
    def Arm_Down(self):
        print("Arm Down")
    def Left(self):
        print("Left 0 600")
    def Right(self):
        print("Right 0 600")
    def Stop(self):
        print('Stop')
    def Quit(self):
        print("Quit")
def get_left(left_speed_entry):
    contents_of_entry_box = left_speed_entry.get()
    return contents_of_entry_box
def get_right(right_speed_entry):
    contents_of_entry_box = right_speed_entry.get()
    return contents_of_entry_box


def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()


    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column


    #Entry Box
    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=1)
    left_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.LEFT)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=1)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=3)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=3)


    #Buttons:
    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=2)
    forward_button['command'] = lambda: mqtt_client.send_message("Forward", [get_left(left_speed_entry),get_right(right_speed_entry)])
    root.bind('<Up>', lambda event: print("Forward key"))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=1)
    left_button['command'] = lambda: mqtt_client.send_message("Left")
    root.bind('<Left>', lambda event: print("Left key"))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=2)
    stop_button['command'] = lambda: mqtt_client.send_message("Stop")
    root.bind('<space>', lambda event: print("Stop key"))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=3)
    right_button['command'] = lambda: mqtt_client.send_message("Right")
    root.bind('<Right>', lambda event: print("Right key"))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=2)
    back_button['command'] = lambda: mqtt_client.send_message("Backward", [get_left(left_speed_entry),get_right(right_speed_entry)])
    root.bind('<Down>', lambda event: print("Back key"))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=1)
    up_button['command'] = lambda: mqtt_client.send_message("Arm_Up")
    root.bind('<u>', lambda event: print("Up key"))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=1)
    down_button['command'] = lambda: mqtt_client.send_message("Arm_Down")
    root.bind('<j>', lambda event: print("Down key"))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=3)
    q_button['command'] = lambda: mqtt_client.send_message("Quit")
    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=3)
    e_button['command'] = lambda: exit()
    root.mainloop()










main()