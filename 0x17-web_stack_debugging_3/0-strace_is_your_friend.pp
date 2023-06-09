# Puppet code to solve error 500 returned by Apache
exec {'E500fix':
  command => 'sed -i "s|require_once( ABSPATH . WPINC . \'/class-wp-locale.phpp\' );\
|require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );|g" /var/www/html/wp-settings.php',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}
