# Installs nginx and configures it
exec {'Updating the apt repos':
  command => 'apt-get update',
  path    => '/usr/bin/'
}

package {'nginx':
  ensure   => installed,
  name     => nginx,
  provider => apt,
}

exec {'Starting Nginx server':
  command => '/usr/sbin/service nginx start'
}

exec {'listening on 80':
  command => "sed -i -E 's/^\tlisten [0-9]+/\tlisten 80/' /etc/nginx/sites-enabled/default",
  path    => '/usr/bin/'
}

exec {'Initializing root page':
  command => "echo 'Hello World!' > /var/www/html/index.nginx-debian.html",
  path    => '/usr/bin/'
}

exec {'Redirect with 301':
  command => "sed -i -E 's|^\tlocation / \{|&\n\n\t\tlocation /redirect_me {\n\t\t\treturn 301 https://linkedin.com/in/shaker-sharabi/;\n\t\t}\n|' /etc/nginx/sites-enabled/default",
  path    => '/usr/bin/'
}

exec {'Reloading Nginx':
  command => "/usr/sbin/nginx -s reload",
}

