import event_capture as evt_c


def system_errors():
    dump_file = str(evt_c.file_path + "\\system_events.dmp")
    cmd_arguments = "Get-EventLog -LogName System -EntryType Error | Format-Table -AutoSize -wrap | Out-File " + "'" + dump_file + "'"
    print(cmd_arguments)
    evt_c.powershell_command(cmd_arguments)


system_errors()