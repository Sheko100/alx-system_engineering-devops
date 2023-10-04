#!/usr/bin/env ruby
# Script to match the presence of letter "b" one time or not in "hbtn"

puts ARGV[0].scan(/hb?tn/).join
