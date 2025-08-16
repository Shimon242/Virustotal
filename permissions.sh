sudo chown -R www-data:www-data /var/www/html/upload_app /var/www/html/uploads
sudo chmod -R 755 /var/www/html/upload_app /var/www/html/uploads
sudo a2dissite 000-default
sudo a2ensite upload_app
sudo systemctl reload apache2
sudo systemctl restart apache2  
