#!/usr/bin/env ruby
# Script to match patterns from texting log file

sendreg = /(?<=from:)\+?\w*\b/
recreg = /(?<=to:)\+?\w*\b/
flagreg = /(?<=flags:)(?:-?\d:?)?{5}/
puts ARGV[0].scan(Regexp.union(sendreg, recreg, flagreg)).join(',')
