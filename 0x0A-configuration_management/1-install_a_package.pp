# Installs flask version 2.1.0 using pip3
package {'flask':
  ensure   => '2.1.0',
  name     => 'flask',
  provider => 'pip3',
  source   => 'pip3'
}
