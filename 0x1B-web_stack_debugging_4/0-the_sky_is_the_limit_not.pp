#icreases the limit of the opening files, thefore the http requests
exec { 'fix-nginx':
  command => "/bin/sed -i 's/15/4096/' /etc/default/nginx;\
/usr/sbin/service nginx restart"
}
