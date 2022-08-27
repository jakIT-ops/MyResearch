package Triangle;   # class name

sub new {
  my $class = shift;
  my $self = {
      _length => shift,
      _height => shift,
  };



  # Print all the values just for clarification.
  print "Length is $self->{_length}\n";
  print "Height is $self->{_height}\n";
  bless $self, $class;
  return $self;
}

sub area{
    my ($self) = @_;
    return ($self->{_length} * $self->{_height}) / 2;
  }

1;

$object = new Triangle( 4, 5);
print "Area of Triangle: " . $object->area();
