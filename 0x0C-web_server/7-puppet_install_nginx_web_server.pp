# Script that configure an Nginx server
package { 'nginx' :
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt',
}

# Verificated if nginx have been install
service { 'nginx':
  ensure  => running,
  enable => true,
}

# Command to redirect page
exec { 'redirect' :
  provider => shell,
  command  => 'sudo sed -i "/server_name _;/ a \\\trewrite ^/redirect_me https://www.nginx.com/resources/library/complete-nginx-cookbook/ permanent;" /etc/nginx/sites-available/default',
}

# Command to show Holberton School in index
exec { 'index' :
  provider => shell,
  command  => 'echo "Holberton School" > /var/www/html/index.nginx-debian.html',
}
