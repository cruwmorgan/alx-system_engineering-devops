#using Puppet to make changes to our configuration file
file { '/etc/ssh/ssh_config':
  ensure => present,
}->
file_line { 'To disable password login':
  path => '~/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
file_line { 'to add path to find the keys':
  path => '~/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
