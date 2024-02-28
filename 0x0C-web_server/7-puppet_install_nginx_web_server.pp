# ensures that nginx is installed and with particular configuration
exec { 'apt update':
  command => '/usr/bin/apt-get update',
  before  => Package['nginx']
}
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt'
}
file { 'root content':
  ensure  => 'present',
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
  require => Package['nginx']
}
file { 'config':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  require => Package['nginx']
}
exec { 'listen to 80':
  command => '/usr/bin/sed -r -i \'s|^(\tlisten [^0-9]*)[0-9]+|\180|\' /etc/nginx/sites-enabled/default',
  require => File['config']
}
exec { 'redirection':
  command => '/usr/bin/sed -r -i \'s|^(\tlocation /).*$|&\n\n\t\1redirect_me {\n\t\t\treturn 301 https://linkedin.com/in/shaker-sharabi/;\n\t\t}|\' /etc/nginx/sites-enabled/default',
  unless  => "/usr/bin/grep -q 'location /redirect_me' /etc/nginx/sites-enabled/default",
  require => File['config']
}
exec { 'restart web server':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}
