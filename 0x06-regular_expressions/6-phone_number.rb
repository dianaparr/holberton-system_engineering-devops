#!/usr/bin/env ruby
# \d matches any digit and must be 10 digits
# no space, starts with a number
puts ARGV[0].scan(/^\d{10}/).join
