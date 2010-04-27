
import os, logging
THIS_FILE_DIR = os.path.dirname(os.path.realpath(__file__))

# The cleartool command full path
if os.name in ['nt', 'os2']:
    CLEARTOOL = "c:\\Program Files\\Rational2003\\ClearCase\\bin\\cleartool"
else:
    CLEARTOOL = "/usr/atria/bin/cleartool"

# The root directory for conversion
# The tool will launch ct lshi -rec there and will convert all files found below this directory
if os.name in ['nt', 'os2']:
    CC_VOB_DIR = "c:\\source\\my_view"
else:
    CC_VOB_DIR = "/vobs/MY_VOB_DIR/path/to/root"

# The tool uses cache directory to place ClearCase version files there. The cache speeds up the transfer process
# in many times in subsequent attempts (up to 10 times). It may be recommended to start the tool 2 days before the
# actual transfer loading all files to the cache. So only new versions appeared during the 2 days will be retrieved from
# ClearCase in the day of the transfer.
# NOTE: Make sure there is enough space in cache directory.
if os.name in ['nt', 'os2']:
    CACHE_DIR = "C:\TEMP\cc2svn_cache"
else:
    CACHE_DIR = "/var/tmp/cc2svn_cache"

# The tool can not track the history of ClearCase symbolic links
# This is a workaround for this. When the tool finds the symlink record in CC history
# it creates the link in the given branch. If the branch does not exist at the time
# the link was created, the tool skips the link.
PUT_CCLINKS_TO_BRANCH = "main"

# The tool may add some svn properties to the files depending on the file extension
# config.autoprops contains the basic mapping for extension -> svn properties
# You can add or change your mapping there 
# The syntax is: shell-pattern = svnproperty=value;svnproperty=value;...
# the space between shell-pattern and equal sign '=' is mandatory
SVN_AUTOPROPS_FILE = os.path.join(THIS_FILE_DIR, "config.autoprops")

# If CC_LABELS_FILE is not defined, the tool will convert all labels it finds in history of the current view
# If CC_LABELS_FILE is defined (recommended), the tool will transfer only those labels mentioned in file
# If you do not want to transfer any labels, specify an empty file
# file must contain one label per line, example: 
# LABEL_1
# LABEL_2 
#CC_LABELS_FILE = os.path.join(THIS_FILE_DIR, "labels.txt")

# If COMPLETE_LABELS is True then cc2svn will attempt to complete labels on
# files that were not visible with the current config spec.  This is done by
# repeatedly setting the config spec for the view to each of the labels in order
# and checking for missing files.
COMPLETE_LABELS = False

# If CC_BRANCHES_FILE is not defined, the tool will convert all branches it finds in history of the current view
# If CC_BRANCHES_FILE is defined, the tool will transfer only those branches mentioned in file
# If you do not want to transfer any branches, specify an empty file
# file must contain one branch name per line (without slashes), example: 
# main  
# user_dev
#CC_BRANCHES_FILE = os.path.join(THIS_FILE_DIR, "branches.txt")

# If the tool finds the size of the file in cache is zero, it may try loading the file from ClearCase again.
# This is to make sure zero size is not due to previous unsuccessful retrieving attempt.
CHECK_ZEROSIZE_CACHEFILE = False

# Should svndump contain the command to create SVN /branches and /tags directory or not
# It will be an error if you try loading the dump with such command to SVN repository containing these directories
SVN_CREATE_BRANCHES_TAGS_DIRS = True

# SVN dump output file created by the tool
SVN_DUMP_FILE = "svndump.txt"

# ClearCase history file created by the tool
HISTORY_FILE = "cchistory.txt"

# DUMP_SINCE_DATE activates incremental dump mode. This should be used after the full dump mode only.
# The idea is: you convert cc2svn on the day X without using this option, working in svn and ClearCase simultaneously
# (do not commit the same changes in svn and CC), then create incremental dump using DUMP_SINCE_DATE=X option.
# Dump will include revisions with date > DUMP_SINCE_DATE (strict greater) only.
# Note: SVN_CREATE_BRANCHES_TAGS_DIRS is ignored in incremental mode
# Date format is YYYYMMDD.hhmmss (the same as CC is using).  
#DUMP_SINCE_DATE = "20010921.175059"

# If LOG_FILE is defined, log messages will be written to this file, rather than
# stdout.
LOG_FILE = "cc2svn.log"

# Level of log messages that should be written to the log file.  Messages at
# logging.WARN or above are always written to the console.
LOG_LEVEL = logging.DEBUG
