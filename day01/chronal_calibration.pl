#!/usr/bin/env perl
use strict;
use warnings;
use feature 'say';

my $freq = 0;
my @deltas;
while (<>) {
    chomp;
    $freq += $_;
    push @deltas, $_;
}

say "resulting frequency = $freq";

$freq = 0;
my %seen;
my $i = 0;
while (1) {
    $freq += $deltas[$i];
    if (defined $seen{$freq}) {
	say "$freq is first seen twice";
	last;
    }
    $seen{$freq} = 1;
    $i = ($i + 1) % @deltas;
}
