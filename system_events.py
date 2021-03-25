import event_capture as evt_c


def system_errors():
    dump_file = str(evt_c.file_path + "\\system_errors.dmp")
    cmd_arguments = "Get-EventLog -LogName System -EntryType Error | Format-Table -AutoSize -wrap | Out-File " + "'" + dump_file + "'"
    print(cmd_arguments)
    evt_c.powershell_command(cmd_arguments)


def system_warnings():
    dump_file = str(evt_c.file_path + "\\system_warnings.dmp")
    cmd_arguments = "Get-EventLog -LogName System -EntryType Warning | Format-Table -AutoSize -wrap | Out-File " + "'" + dump_file + "'"
    print(cmd_arguments)
    evt_c.powershell_command(cmd_arguments)


def system_information():
    dump_file = str(evt_c.file_path + "\\system_info.dmp")
    cmd_arguments = "Get-EventLog -LogName System -EntryType Information | Format-Table -AutoSize -wrap | Out-File " + "'" + dump_file + "'"
    evt_c.powershell_command(cmd_arguments)
