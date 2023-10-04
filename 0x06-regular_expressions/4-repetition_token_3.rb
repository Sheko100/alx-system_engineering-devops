#!/usr/bin/env ruby
# Script to match any number of letter 't' presences or
# not at all in "hbtn"

puts ARGV[0].scan(/hbt*n/).join
