$process = $args[0]
Get-WmiObject Win32_Process -Filter "name = '$process'" | Format-Table -Property ProcessId, CommandLine