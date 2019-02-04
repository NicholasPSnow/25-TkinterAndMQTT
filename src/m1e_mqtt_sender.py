""" A simple example of using MQTT for SENDING messages. """

import mqtt_remote_method_calls as com
import time


def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    my_delegate = DelegateThatReceives()
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        mystr = input("Enter a string: ")
        myint = input("Enter a number: ")
        myname = input("Enter your name: ")
        mqtt_client.send_message("say_it", [mystr,myint,myname])


class DelegateThatReceives(object):

    def say_it(self, message,message2,message3):
        print("Message received!",message,message2,message3 )


main()
