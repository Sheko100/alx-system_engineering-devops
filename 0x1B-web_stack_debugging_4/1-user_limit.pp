# Increases the limit of openning files for holberton user

exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/80000/" \
/etc/security/limits.conf; sed -i "/holberton soft/s/4/40000/" \
/etc/security/limits.conf',
  path    => ['/bin']
}
