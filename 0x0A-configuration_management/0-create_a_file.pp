# Creates a file with particular specifications
file { 'school':
  ensure  => present,
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744'
}
