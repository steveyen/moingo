#!/usr/bin/ruby

# Dumb, always "works" merge strategy of local changes win.
#
`git pull --strategy ours origin master`
`git add .`
`git commit -m "#{ARGV[0]}"`
`git push origin master`
