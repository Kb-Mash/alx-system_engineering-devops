# Install and configure nginx
exec { 'exec_0':
  command => 'sudo apt-get -y update',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'exec_1':
  require => Exec['exec_0'],
  command => 'sudo apt-get -y install nginx',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'exec_2':
  require => Exec['exec_1'],
  command => 'sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By \$hostname;/" /etc/nginx/sites-enabled/default',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'exec_3':
  require => Exec['exec_2'],
  command => 'sudo service nginx restart',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
  returns => [0,1]
}
