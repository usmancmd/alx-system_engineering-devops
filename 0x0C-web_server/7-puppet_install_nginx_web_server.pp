# Install and configure an Nginx server using Puppet instead of Bash

exec {'install nginx':
  command  => 'sudo apt-get update;
		sudo apt-get install nginx -y;
		echo "Hello World!" | sudo tee /var/www/html/index.html;
		new_configuration="server_name _;\n\trewrite ^\/redirect_me https:\/\/www.google.com permanent;"
		sudo sed -i "s/server_name _;/$new_configuration/" /etc/nginx/sites-enabled/default
		sudo service nginx restart',
  provider => shell,
}
