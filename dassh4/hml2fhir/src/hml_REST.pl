#!/usr/bin/env perl
 
# 1. sudo port install p5.28-mozilla-ca
# 2. sudo port install p5.28-lwp-protocol-https
# 3. /opt/local/bin/perl5.28.3 hml_REST.pl <hml_file_name>

use strict;
use warnings;
 
use HTTP::Request ();
use LWP;
 
my $file_name = $ARGV[0];

if (!$file_name) {
	print "Usage: perl hml_REST.pl <hml_file_name>";
	exit;
}
 
local $/;

my $url = 'https://qa-api.nmdp.org/hml_gw/v1/submit';
my $access_token = '';
my $param = '?testSubmit=false';

my $headers = [
'Authorization' => 'Bearer '.$access_token,
'Connection' => 'close',
'Content-Type' => 'application/xml; charset=UTF-8',
'cache-control' => 'no_cache'
];

my $data;
{
    local $/;
    open my $fh, '<', $file_name or die "can't open $file_name: $!";
    $data = <$fh>;
}

my $r = HTTP::Request->new('POST', $url.$param, $headers, $data); 
my $ua = LWP::UserAgent->new();
my $res = $ua->request($r);

print $res->decoded_content;
