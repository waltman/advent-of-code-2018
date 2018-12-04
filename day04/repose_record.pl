#!/usr/bin/env perl
use strict;
use warnings;
use feature qw(:5.24);

my @records;
while (<>) {
    chomp;
    push @records, $_;
}

my %tot_asleep;
my %min_asleep;
my %guard_asleep;
my ($guard, $asleep, $wake);
for my $record (sort @records) {
    if ($record =~ /Guard #(\d+)/) {
        $guard = $1;
    } elsif ($record =~ /falls asleep/) {
        $asleep = substr($record, 15, 2);
    } else {
        $wake = substr($record, 15, 2);
        $tot_asleep{$guard} += $wake - $asleep;
        for my $minute ($asleep..$wake-1) {
            $min_asleep{$guard}{$minute}++;
            $guard_asleep{$minute}{$guard}++;
        }
    }
}

# find best guard
my $best_guard = -1;
my $best_time = -1;
while (my ($guard, $asleep) = each %tot_asleep) {
    if ($asleep > $best_time) {
        $best_guard = $guard;
        $best_time = $asleep;
    }
}

# find best time for best guard
my $best_min = -1;
$best_time = -1;
while (my ($minute, $asleep) = each %{$min_asleep{$best_guard}}) {
    if ($asleep > $best_time) {
        $best_min = $minute;
        $best_time = $asleep;
    }
}
say "part 1: ", $best_guard * $best_min;

# find best minute across all guards
$best_min = -1;
$best_time = -1;
$best_guard = -1;
for my $minute (keys %guard_asleep) {
    while (my ($guard, $asleep) = each %{$guard_asleep{$minute}}) {
        if ($asleep > $best_time) {
            $best_min = $minute;
            $best_time = $asleep;
            $best_guard = $guard;
        }
    }
}
say "part2: ", $best_guard * $best_min;
