# Fixes the WordPress file by fixing a typo
exec { 'fix-wordpress':
  command => '/bin/sed -i s/phpp/php/ /var/www/html/wp-settings.php'
}
