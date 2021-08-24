# Script that configure an Nginx server
exec { 'update' :
  command  => 'sudo apt-get -y update',
  provider => shell,
}

package { 'nginx' :
  ensure  => 'installed',
  require => Exec['update'],
}

file_line { 'redirect' :
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => '\trewrite ^/redirect_me https://www.nginx.com/resources/library/complete-nginx-cookbook/ permanent;',
  require => Package['nginx'],
}

file_line { 'header' :
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => '\trewrite ^/redirect_me https://www.nginx.com/resources/library/complete-nginx-cookbook/ permanent;',
  line    => '\tadd_header X-Served-By $hostname;',
  require => Package['nginx'],
}

file { '/var/www/html/index.nginx-debian.html' :
  ensure  => 'file',
  content => 'Holberton School',
  require => Package['nginx'],
}

service { 'nginx' :
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
