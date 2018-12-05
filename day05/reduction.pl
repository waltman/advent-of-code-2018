#!/usr/bin/env perl
use strict;
use warnings;
use feature 'say';

my @re;
push @re, $_ . uc $_ for 'a'..'z';
push @re, $_ . lc $_ for 'A'..'Z';
my $re = join '|', @re;

while (<>) {
    chomp;
    my $polymer = $_;
    my $s = $polymer;
    while (1) {
	my $t = $s;
	$s =~ s/$re//g;
	if ($s eq $t) {
	    say "part1: ", length($s);
	    last;
	}
    }

    my $best = 1e100;
    for my $c ('a'..'z') {
	my $re2 = $c . '|' . uc $c;
	$s = $polymer;
	$s =~ s/$re2//g;
	while (1) {
	    my $t = $s;
	    $s =~ s/$re//g;
	    if ($s eq $t) {
		if (length($s) < $best) {
		    $best = length($s);
		    say "$c ", $best;
		}
		last;
	    }
	}
    }
    say "part2: ", $best;
}
