# creates a school in the /tmp directory with the content "I love Puppet"
# with "www-data" as the group and owner, and with 0744 permissions
file {'/tmp/school':
  ensure  => 'present',
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data'
}
