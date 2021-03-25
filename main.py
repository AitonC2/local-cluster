import system_events as se


def save_event_dumpfile():
    print("1- System Errors\n"
          "2- System Information\n"
          "3- System Warnings:\n")

    choice = int(input(":"))

    if choice == 1:
        se.system_errors()
    elif choice == 2:
        se.system_information()
    else:
        se.system_warnings()


save_event_dumpfile()
