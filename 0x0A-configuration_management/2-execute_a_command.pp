#Using Puppet, create a manifest that kills a process named killmenow
exec { 'process killer':
  command => '/usr/bin/pkill -x killmenow',
}
