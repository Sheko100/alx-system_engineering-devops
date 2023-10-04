#!/usr/bin/env ruby
# Script to match the presence of letter 't' one time or more in "hbtn"

puts ARGV[0].scan(/hbt+n/).join
