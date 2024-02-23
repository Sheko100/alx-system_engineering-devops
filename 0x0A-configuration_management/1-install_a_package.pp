# Ensures that Flask 2.1.0 is installed
package { 'Flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3'
}
package { 'Werkzeug':
  ensure   => '2.1.1',
  name     => '2.1.1',
  provider => 'pip3'
}
