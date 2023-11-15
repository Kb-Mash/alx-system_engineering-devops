# increase the ULIMIT of the default file
file_line { 'replace_line':
  path => '/etc/default/nginx',
  line => 'ULIMIT="-n 10000"',
  match => '^ULIMIT',
}
-> exec { 'restart_nginx':
  command => 'service nginx restart',
  provider => 'shell',
}
