#!/usr/bin/env ruby
# escape square brackets with backslash
# .: any one character except newline
# *?: 0 or more times
puts ARGV[0].scan(/\[from:.*?\] \[to:.*?\] \[flags:.*?\]/).join
