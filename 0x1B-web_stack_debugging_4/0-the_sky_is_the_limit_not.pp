# Fix the stack so that there is not failed requests, by
#  increases the amount of traffic an Nginx server can handle

# Increase the ULIMIT of the default file.
exec { 'Set nginx_limit':
  command => '/usr/bin/sudo -S sed -i "s/15/4096/g" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx.
exec { 'nginx-restart':
  command => '/usr/bin/sudo service nginx restart',
  path    => '/etc/init.d/'
}
