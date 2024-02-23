# kills the process called killmenow
exec {'hitman':
  command => 'pkill killmenow',
  onlyif  => 'test `pgrep killmenow`',
  path    => '/usr/bin/'
}
