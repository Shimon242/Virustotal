sudo chown -R www-data:www-data /var/www/html/upload_app /var/www/html/uploads
sudo chmod -R 755 /var/www/html/upload_app /var/www/html/uploads
sudo systemctl restart apache2  
