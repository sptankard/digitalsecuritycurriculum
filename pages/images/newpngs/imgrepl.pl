#!/usr/bin/perl

$md_loc = $ARGV[0];

$num = $#ARGV;
print "yoyoy $md_loc $num" . @ARGV . "\n";



$pngfile = q|/root/ds4all/pages/images/newpngs/png.txt|;
open($f, "<$pngfile") || die "pngfile $pngfile";
my @pngs;
my @jpgs;
while (<>) { chomp;  push @pngs, $_; s/\.png/\.jpg/;  push @jpgs, $_; }
close ($f);

$/ = undef;;
open($f, "<$md_loc") || die "md_loc $md_loc";
$content = <>;

for ($i = 0; $i <= $#pngs; $i++) {
   $jpg_ref = $jpg[$i];
   $png_ref = $png[$i];
   $content =~ s/$jpg_ref/$png_ref/gs;
}

print $content;
