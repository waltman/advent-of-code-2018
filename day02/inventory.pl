#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.24);
use experimental qw(signatures);

my ($num2, $num3) = (0, 0);
my @ids;

while (<>) {
    chomp;
    push @ids, $_;
    my ($has2, $has3) = count_appear($_);
    $num2++ if $has2;
    $num3++ if $has3;
}

say "checksum = ", $num2 * $num3;

my $target_len = length($ids[0]) - 1;
for my $i (0..$#ids - 1) {
    for my $j ($i+1..$#ids) {
	my $common = letters_in_common($ids[$i], $ids[$j]);
	say $common if length($common) == $target_len;
    }
}

sub count_appear($s) {
    my %h;
    for my $c (split //, $s) {
	$h{$c}++;
    }

    my ($has2, $has3) = (0, 0);
    for my $cnt (values %h) {
	$has2 = 1 if $cnt == 2;
	$has3 = 1 if $cnt == 3;
    }

    return ($has2, $has3);
}

sub letters_in_common($s, $t) {
    my $res = '';
    my @s = split //, $s;
    my @t = split //, $t;
    for my $i (0..$#s) {
	$res .= $s[$i] if $s[$i] eq $t[$i];
    }
    return $res;
}
