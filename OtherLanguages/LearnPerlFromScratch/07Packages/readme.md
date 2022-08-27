# 1. Defining Packages

### Example snippet

```perl
package Shape;

sub new {     # constructor
   my $class = shift;
   my $self = {
   # member variables
      name  => shift,
      sides => shift,
   };

   bless $self, $class;
   return $self;
}

1;
```

### Adding methods to a package

```perl
package Shape;

sub new {     # constructor
   my $class = shift;
   my $self = {
   # member variables
      name  => shift,
      sides => shift,
   };

   bless $self, $class;
   return $self;
}


sub Description {
  my ($self) = @_;
  print "A $self->{name} has $self->{sides} sides.";
}

1;
```

### Creating multiple objects of a class

```perl
package Shape;

sub new {     # constructor
   my $class = shift;
   my $self = {
   # member variables
      name  => shift,
      sides => shift,
   };

   bless $self, $class;
   return $self;
}


sub Description {
  my ($self) = @_;
  print "A $self->{name} has $self->{sides} sides.\n";
}

1;

$Square = new Shape("Square", 4);
$Square->Description();

$Triangle = new Shape("Triangle", 3);
$Triangle->Description();

$Hexagon = new Shape("Hexagon", 6);
$Hexagon->Description();
```

# 2. Setters and Getters

### Setters

```perl
package Shape;

sub new {     # constructor
   my $class = shift;
   my $self = {
   # member variables
      name  => shift,
      sides => shift,
   };

   bless $self, $class;
   return $self;
}


sub Description {
  my ($self) = @_;
  print "A $self->{name} has $self->{sides} sides.\n";
}

sub setName {
   my ($self, $value) = @_;
   $self->{name} = $value;
   return $self->{name};
}

sub setSides {
   my ($self, $value) = @_;
   $self->{sides} = $value;
   return $self->{sides};
}

1;

$Square = new Shape("square", 4);
$Square->Description();

$Square->setName("Triangle");
$Square->setSides("3");
$Square->Description();
```

### Getters

```perl
package Shape;

sub new {     # constructor
   my $class = shift;
   my $self = {
   # member variables
      name  => shift,
      sides => shift,
   };

   bless $self, $class;
   return $self;
}


sub Description {
  my ($self) = @_;
  print "A $self->{name} has $self->{sides} sides.\n";
}

sub setName {
   my ($self, $value) = @_;
   $self->{name} = $value;
   return $self->{name};
}

sub setSides {
   my ($self, $value) = @_;
   $self->{sides} = $value;
   return $self->{sides};
}

sub getName {
   my ($self) = @_;
   return $self->{name};
}

sub getSides {
   my ($self) = @_;
   return $self->{sides};
}

1;

$Square = new Shape("square", 4);

$shapeName = $Square->getName();
$shapeSides = $Square->getSides();

print "Shape name : $shapeName and Shape Sides : $shapeSides";
```
