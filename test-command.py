import os

commands = "curl https://gosuslugi.ru", "lsblk -f","ps -aux"
test_strings = "Портал государственных услуг", "ext4", "cpuhp"


def Search_string(command, string):
    print("Command - " + command)
    print("Find string - " + string)
    result = os.popen(command).read()
    if (string in result):
        print("True")
    else:
        print("False")





for command in commands:
    for test_string in test_strings:
        Search_string(command, test_string)