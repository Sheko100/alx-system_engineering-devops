#!/usr/bin/env ruby
# Script to match a 10 digits phone number

puts ARGV[0].scan(/^[0-9]{10}$/).join
