# Script that configure an Nginx server
package { 'get nginx' :
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt',
}

service { 'nginx':
  ensure  => running,
  enabled => true,
}

exec { 'command one: to redirect' :
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/ a \\\trewrite ^/redirect_me https://www.nginx.com/resources/library/complete-nginx-cookbook/ permanent;" /etc/nginx/sites-available/default',
}

exec { 'command two: index' :
  provider => shell,
  command  => 'echo "Holberton School" > /var/www/html/index.nginx-debian.html',
}
