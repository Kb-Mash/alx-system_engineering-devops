# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`

file_line { 'fix_typo':
        path  => '/var/www/html/wp-settings.php',
        line  => 'php',
        match => 'phpp',
}
