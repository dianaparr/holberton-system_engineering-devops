# Script that configure an Nginx server
exec { 'header' :
  provider => shell,
  command  => "sudo apt-get -y update;
               sudo apt-get -y install nginx;
               sudo sed -i '/rewrite/ a \\\n\tadd_header X-Served-By ${hostname};' /etc/nginx/sites-available/default;
               sudo /etc/init.d/nginx restart",
}
