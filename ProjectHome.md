cc2svn tool converts ClearCase view files with all history and given labels to SVN dump.
<br>
The dump can be loaded by SVN using 'cat svndump.txt | svnadmin load' command.<br>
<br>
<h2>Features:</h2>
<ul><li>transfers history of changes for files saving the date, author and comment for each revision<br>
</li><li>converts all/some/none branches (configurable)<br>
</li><li>converts all/some/none labels (configurable)<br>
</li><li>incremental dump mode<br>
</li><li>retry/ignore failed CC commands<br>
</li><li>cache for ClearCase files<br>
</li><li>tested on Linux/Solaris, python 2.5/2.6</li></ul>

<h2>Main points:</h2>

The tool uses the current ClearCase view to list the CC history (ct lshi -rec) then it goes through the history and processes each record.<br>
<br>
That means that the tool does not transfer those files that are not visible from the current CC view.<br>
<br>
However the tool transfers all CC labels to SVN tags correctly. For that in the second phase it sets config_spec of the current view to match the label (<code>element * LABEL</code>) for each given label and checks that no files are lost during the first phase.<br>
<br>
<b>WARNING</b>: Side effect - the tool changes the config_spec of the current working ClearCase view. Do not use the view during the tool work.<br>
<br>
All branches except the /main are created using 'svn cp' command basing on the CC parent branch.<br>
<br>
There is a difference in creating the branches in ClearCase and SVN:<br>
<br>
SVN copies all files from parent branch to the target like: svn cp branches/main branches/dev_branch<br>
<br>
ClearCase creates the actual branch for file upon checkout operation only.<br>
<br>
In other words the tool can't guarantee the content of /branches will be exactly like in ClearCase.<br>
<br>
But the tool guarantees the labels are transferred correctly.<br>
<br>
<br>
The tool uses cache directory to place ClearCase version files there. The cache speeds up the transfer process in many times in subsequent attempts (up to 10 times). It may be recommended to start the tool 2 days before the actual transfer loading all files to the cache. So only new versions appeared during these days will be retrieved from ClearCase in the day of the transfer.<br>
<br>
Actually the tool caches any data retrieved from ClearCase including the history file.<br>
<br>
<br>
The tool provides the possibility to retry/ignore any ClearCase command if error occurs.<br>
<br>
The tool will put empty file to the cache if you ignore ClearCase retrieving operation error.<br>
<br>
<br>
Timing: CC repository of 5 GB (~120.000 revisions) is converted in ~1 hour using the pre-cached files.<br>
<br>
<h2>Options:</h2>
<pre><code># The cleartool command full path<br>
CLEARTOOL = "/usr/atria/bin/cleartool"<br>
<br>
# The root directory for conversion<br>
# The tool will launch ct lshi -rec there and will convert all files found below this directory<br>
CC_VOB_DIR = "/vobs/MY_VOB_DIR/path/to/root"                                                   <br>
<br>
# The tool uses cache directory to place ClearCase version files there. The cache speeds up the transfer process<br>
# in many times in subsequent attempts (up to 10 times). It may be recommended to start the tool 2 days before the<br>
# actual transfer loading all files to the cache. So only new versions appeared during the 2 days will be retrieved from<br>
# ClearCase in the day of the transfer.                                                                                 <br>
# NOTE: Make sure there is enough space in cache directory.                                                             <br>
CACHE_DIR = "/var/tmp/cc2svn_cache"                                                                                     <br>
<br>
# The tool can not track the history of ClearCase symbolic links<br>
# This is a workaround for this. When the tool finds the symlink record in CC history<br>
# it creates the link in the given branch. If the branch does not exist at the time  <br>
# the link was created, the tool skips the link.                                     <br>
PUT_CCLINKS_TO_BRANCH = "main"                                                       <br>
<br>
# The tool may add some svn properties to the files depending on the file extension<br>
# config.autoprops contains the basic mapping for extension -&gt; svn properties<br>
# You can add or change your mapping there<br>
# The syntax is: shell-pattern = svnproperty=value;svnproperty=value;...<br>
# the space between shell-pattern and equal sign '=' is mandatory<br>
SVN_AUTOPROPS_FILE = THIS_FILE_DIR + "/config.autoprops"<br>
<br>
# If CC_LABELS_FILE is not defined, the tool will convert all labels it finds in history of the current view<br>
# If CC_LABELS_FILE is defined (recommended), the tool will transfer only those labels mentioned in file<br>
# If you do not want to transfer any labels, specify an empty file<br>
# file must contain one label per line, example:<br>
# LABEL_1<br>
# LABEL_2<br>
CC_LABELS_FILE = THIS_FILE_DIR + "/labels.txt"<br>
<br>
# If CC_BRANCHES_FILE is not defined, the tool will convert all branches it finds in history of the current view<br>
# If CC_BRANCHES_FILE is defined, the tool will transfer only those branches mentioned in file<br>
# If you do not want to transfer any branches, specify an empty file<br>
# file must contain one branch name per line (without slashes), example:<br>
# main<br>
# user_dev<br>
CC_BRANCHES_FILE = THIS_FILE_DIR + "/branches.txt"<br>
<br>
# If the tool finds the size of the file in cache is zero, it may try loading the file from ClearCase again.<br>
# This is to make sure zero size is not due to previous unsuccessful retrieving attempt.<br>
CHECK_ZEROSIZE_CACHEFILE = True<br>
<br>
# Should svndump contain the command to create SVN /branches and /tags directory or not<br>
# It will be an error if you try loading the dump with such command to SVN repository containing these directories<br>
SVN_CREATE_BRANCHES_TAGS_DIRS = False<br>
<br>
# SVN dump output file created by the tool<br>
SVN_DUMP_FILE = "svndump.txt"<br>
<br>
# ClearCase history file created by the tool<br>
HISTORY_FILE = "cchistory.txt"<br>
<br>
# DUMP_SINCE_DATE activates incremental dump mode. This should be used after the full dump mode only.<br>
# The idea is: you convert cc2svn on the day X without using this option, working in svn and ClearCase simultaneously<br>
# (do not commit the same changes in svn and CC), then create incremental dump using DUMP_SINCE_DATE=X option.<br>
# Dump will include revisions with date &gt; DUMP_SINCE_DATE (strict greater) only.<br>
# Note: SVN_CREATE_BRANCHES_TAGS_DIRS is ignored in incremental mode<br>
# Date format is YYYYMMDD.hhmmss (the same as CC is using).<br>
DUMP_SINCE_DATE = "20080921.175059"<br>
</code></pre>