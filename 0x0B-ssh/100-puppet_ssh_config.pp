# Puppet manifest to Configure SSH Configuration file
# So that you can connect to a server without typing a password

exec { 'Configure file':
  command => '/bin/echo -e "IdentityFile ~/.ssh/school\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
  path => '/etc/ssh/ssh_config',
}
