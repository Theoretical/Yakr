#import multiprocessing
#import Queue
#import plugins
#import select
from yakr.network import simple_connect
#from yakr.plugin import Plugin
from yakr.util import set_procname
from yakr.bot import Bot
set_procname("yakr")

b = Bot(simple_connect(("localhost", 6667)))
#b.load("fortune")
#b.load("repeater")
b.load("pluginTest")
b.load("myPlugins.plugin1")
b.load("myPlugins.plugin2")
b.run()


#p = Plugin("fortune")
#write, read = network.simple_connect(("localhost", 6667))
#write.put("NICK Dot")
#write.put("USER Dot localhost localhost :foo bar")
#while True:
#    readable, _, _ = select.select([p.reader(), read._reader],[],[])
#    if read._reader in readable: #network has data
#        data = read.get()
#        if data.startswith("PING"):
#            write.put("PONG" + data[4:])
#
#        if data.startswith(":Dot MODE"):
#            p.put("::STATE:READY")
#
#        if data is None:
#            print "End from net"
#            break
#
#        print ">", data
#        p.put(data)
#
#    if p.reader() in readable: # plugin has data
#        data = p.get()
#        if data is None:
#            print "End from plugin"
#            break
#        print "<", data
#        write.put(data)
#
#p.stop()
