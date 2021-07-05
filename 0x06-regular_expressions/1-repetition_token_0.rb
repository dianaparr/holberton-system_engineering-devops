#!/usr/bin/env ruby
# {m,n} (m <= n)  at least m but no more than n times,
# t is repeated at least two times and a maximum of five times
puts ARGV[0].scan(/hbt{2,5}n/).join
