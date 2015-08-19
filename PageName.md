# Introduction #

Add your content here.


# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages


import sys
if sys.hexversion < 0x02070000:
> print "Python 2.7 required"
> print "Try: /python-2.7.3/bin/python", " ".join(sys.argv)
> sys.exit(1)

import re, argparse, subprocess
from xml.parsers import expat

argp = argparse.ArgumentParser(description = "List difference in JIRAs between path1 and path2 since branch\_name creation");
argp.add\_argument('-since', dest='branch\_name', metavar='branch\_name', required=True, help="")
argp.add\_argument('path1', help="")
argp.add\_argument('path2', nargs="?", help="")
args = argp.parse\_args()

class Entry:
> def init(self):
> > self.jira = "undefined"
> > self.msg = ""
> > self.path = set()
> > self.rev = ""
> > self.auth = ""
> > self.date = ""


> def str(self):
> > out = self.rev + " " + self.msg + '\n'
> > for p in self.path:
> > > out += p + '\n'

> > return out

def makePath(name):

> if name.find("rapid\_release") != -1 and name.find("branches") == -1:
> > return "//branches/" + name

> else:
> > return "//" + name

target1 = makePath(args.path1)
target2 = ""
if args.path2:

> target2 = makePath(args.path2)

stop\_branch = "//branches/" + args.branch\_name.strip()
regp = re.compile("(.**)(JIRA-[0-9]+)(.**)")
jiras1 = {}
jiras2 = {}
elem = ""
elem\_attr = ""
stop = False
inTarget1 = False
inTarget2 = False
entry = Entry()

def start(name, attr):
> global elem, elem\_attr
> elem = name
> elem\_attr = attr
> if elem == "logentry":
> > entry.rev = elem\_attr.setdefault("revision", "")
  1. rint ">>", name, attr

def end(name):

> global elem, entry, inTarget1, inTarget2
> if name == "logentry":
> > if inTarget1:
> > > jiras1.setdefault(entry.jira, [.md](.md)).append(entry)

> > if inTarget2:
> > > jiras2.setdefault(entry.jira, [.md](.md)).append(entry)
    1. rint entry.jira, entry

> > entry = Entry()
> > inTarget1 = False
> > inTarget2 = False

> elem = ""
  1. rint "<<", name

def data(text):
> global entry, jiras1, stop, inTarget1, inTarget2
  1. rint "text:",text
> if elem == "path":
> > action = elem\_attr["action"]
> > entry.path.add(action + " " + text)
> > if action == 'A' and text == stop\_branch:
> > > stop = True

> > elif text.find(target1) != -1:
> > > inTarget1 = True

> > if target2 and text.find(target2) != -1:
> > > inTarget2 = True


> elif elem == "msg":
> > m = regp.match(text)
> > if m:
> > > entry.jira = m.group(2)
> > > entry.msg = (m.group(1) + m.group(3)).strip()

> > pass

> elif elem == "author":
> > entry.auth = text

> elif elem == "date":
> > entry.date = text

p = expat.ParserCreate()
p.StartElementHandler = start
p.EndElementHandler = end
p.CharacterDataHandler = data

def execShell(cmd):

> p = subprocess.Popen(cmd, shell = True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
> while(True):
> > retcode = p.poll() #returns None while subprocess is running
> > line = p.stdout.readline()
> > yield line
> > if(retcode is not None):
> > > break

command = "/usr/bin/env svn log -v --xml svn://root"
for line in execShell(command):

> p.Parse(line)
> if stop: break

diff = jiras1.viewkeys() - jiras2.viewkeys()

url = "http://JIRA/issues/?filter=-1&jql=issue%20in%20%28"
csj = "%2C".join(filter(lambda x: x.find("JIRA\_TO\_FILTER") == -1, diff))
url += csj + "%29"

for jira in sorted(diff):
> entries = jiras1[jira](jira.md)
> print "\n===", jira
> files = set()
> msg = set()
> auth = set()
> rev = set()
> for e in entries:
> > files.update(e.path)
> > msg.add(e.msg)
> > auth.add(e.auth)
> > rev.add(e.rev)

> print "_auth:", ",".join(auth)
> print "_rev:", ",".join(rev)
> print "_comments:"
> for m in msg:
> > print m

> print "_changes:"
> for f in sorted(files):
> > print f

print "\n=== jiras in", target1, "since creation of", stop\_branch
print "_jiras1:", ",".join(sorted(jiras1.viewkeys()))_

print "\n=== jiras in", target2, "since creation of", stop\_branch
print "_jiras2:", ",".join(sorted(jiras2.viewkeys()))_

print "\n=== diff"
print "_jiras:", ",".join(sorted(diff))
print "_url:", url