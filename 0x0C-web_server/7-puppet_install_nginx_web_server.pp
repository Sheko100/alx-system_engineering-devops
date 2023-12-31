# Installs nginx and configures it
exec {'Updates the apt repos':
  command => 'apt-get update',
  path    => '/usr/bin/'
}

package {'nginx':
  ensure   => installed,
  name     => nginx,
  provider => apt,
}

exec {'listening on 80':
  command => "sed -i -E 's/^\tlisten [0-9]+/\tlisten 80/' /etc/nginx/sites-enabled/default",
  path    => '/usr/bin/'
}

exec {'Initializing root page':
  command => "echo 'Hello World!' > /var/www/html/index.nginx-debian.html",
  path    => '/usr/bin/'
}
