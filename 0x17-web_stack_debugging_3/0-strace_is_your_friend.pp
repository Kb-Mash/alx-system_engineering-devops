# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`
exec { 'fix_typo':
        command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}
