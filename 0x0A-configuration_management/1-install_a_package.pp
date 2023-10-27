# Define a package resource to install Flask using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
