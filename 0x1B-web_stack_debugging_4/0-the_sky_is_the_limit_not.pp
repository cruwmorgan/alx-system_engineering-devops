# puppet code for increasing NGINX page opening limit
exec {'increase max open files limit':
  command => 'sed -i "s|15|15000|g" /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}

exec { 'restart NGINX':
  require => Exec['increase max open files limit'],
  path    => '/usr/bin/',
  command => 'service nginx restart',
}
