# Script that use resource type exec
exec { 'Kill a process' :
  command  => 'pkill killmenow',
  provider => shell
}
