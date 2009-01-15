#!/usr/bin/ruby

now = Time.now.strftime('%Y/%m/%d %H:%M:%S')
me = `whoami`.strip

`git pull --strategy ours origin master`
`git add .`
`git commit -m "syncing by #{me} on #{now}"`
`git push origin master`
