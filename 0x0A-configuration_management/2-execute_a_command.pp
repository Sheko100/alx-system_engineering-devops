# Kills a process named killmenow
exec { 'killer':
  command => 'pkill -15 killmenow',
  onlyif  => 'pgrep killmenow && echo $?',
  path    => '/usr/bin'
}
