# Configures /etc/ssh/ssh_config
exec { "Disable passwd auth":
  command => "sed -i 's/#*\s*PasswordAuthentication yes/    PasswordAuthentication no/' /etc/ssh/ssh_config",
  path    => "/usr/bin"
}
exec { 'Declare identity file':
  command => "echo '    IdentityFile ~/.ssh/school' >> /etc/ssh/ssh_config",
  path    => "/usr/bin"
}
