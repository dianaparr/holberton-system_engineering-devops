# Script that configure an Nginx server
exec { 'update' :
  command  => 'sudo apt-get -y update',
  provider => shell
}

package { 'nginx' :
  ensure => 'installed',
}

exec { 'header' :
  provider => shell,
  command  => "sudo sed -i '/rewrite/ a \\\n\tadd_header X-Served-By $hostname;' /etc/nginx/sites-available/default;"
}

service { 'nginx' :
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}
