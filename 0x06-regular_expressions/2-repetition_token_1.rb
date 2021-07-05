#!/usr/bin/env ruby
# {m,n} (m <= n)  at least m but no more than n times.
puts ARGV[0].scan(/hb{0,1}tn/).join
