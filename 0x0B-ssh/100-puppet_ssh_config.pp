# myserver configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host 52.72.12.97
    HostName 52.72.12.97
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
