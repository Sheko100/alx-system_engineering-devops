#!/usr/bin/env ruby
# Script to match the repetation of letter "t" in "hbtn"

puts ARGV[0].scan(/hbt{2,5}n/).join
