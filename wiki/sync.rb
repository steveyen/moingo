#!/usr/bin/ruby

now = Time.now.strftime('%Y/%m/%d %H:%M:%S')
usr = `whoami`.strip
msg = ARGV[0]
msg = "- #{msg}" if msg

# Dumb, always "works" merge strategy of local changes win.
#
`git pull --strategy ours origin master`
`git add .`
`git commit -m "syncing by #{usr} on #{now} #{msg}"`
`git push origin master`
