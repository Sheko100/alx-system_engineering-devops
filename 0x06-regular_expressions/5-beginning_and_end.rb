#!/usr/bin/env ruby
# Script to match a string starts with 'h' and ends with 'n' and has
# any one character between them

puts ARGV[0].scan(/h\wn/).join
