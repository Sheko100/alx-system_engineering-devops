# ensures that nginx is installed and with particular configuration
exec { 'apt update':
  command => '/usr/bin/apt-get update',
  before  => Package['nginx']
}
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt'
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
exec { 'custom header':
  command => 'sed -r -i \'s|^server.*|&\n\tadd_header X-Served-By \$hostname;|\' /etc/nginx/sites-enabled/default',
  unless  => "/usr/bin/grep -q 'X-Served-By' /etc/nginx/sites-enabled/default",
  require => File['config']
}
exec { 'restart web server':
  command => '/usr/sbin/service nginx restart',
  require => Package['nginx']
}
