#!/usr/bin/perl

$md_loc = $ARGV[0];


$pngfile = q|/root/ds4all/pages/images/newpngs/png.txt|;
open($f, "<$pngfile") || die "pngfile $pngfile";
my @pngs;
my @jpgs;
while (<$f>) { chomp;  push @pngs, $_; s/\.png/\.jpg/;  push @jpgs, $_; }
close ($f);

$/ = undef;
open($f, "<$md_loc") || die "md_loc $md_loc";
$content = <$f>;
close ($f);
for ($i = 0; $i <= $#pngs; $i++) {
   $jpg_ref = $jpgs[$i];
   $png_ref = $pngs[$i];

   $content =~ s/$jpg_ref/$png_ref/gs;
}

open($f, ">$md_loc") || die "md_loc $md_loc";
print $f $content;
close($f);
