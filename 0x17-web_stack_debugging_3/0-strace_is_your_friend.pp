# syntax error in wp-settings file
exec { 'fix_syntax' :
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => 'shell',
  command  => 'sudo sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
}

exec { 'reload' :
  path     => '/usr/bin:/usr/sbin:/bin',
  provider => 'shell',
  command  => 'sudo /etc/init.d/apache2 restart'
}
