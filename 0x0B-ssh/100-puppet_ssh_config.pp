# Changes in the configuration file
# Resource Type: file_line; properties: ensure, path, line, match
#include stdlib  OJO install module
file_line { 'Config file use private key' :
  ensure => 'present',
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
}
