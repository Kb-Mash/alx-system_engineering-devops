#Executes pkill command to kill bashscript file killmenow
exec {'kill killmenow':
  command => '/usr/bin/pkill killmenow',
}
