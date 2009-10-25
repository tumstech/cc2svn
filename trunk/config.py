
import os
CONFIG_DIR = os.path.dirname(os.path.realpath(__file__))

# The cleartool command full path
CLEARTOOL = "/usr/atria/bin/cleartool"

# The root directory for conversion
# The tool will launch ct lshi -rec there and will convert all files found below this directory
CC_VOB_DIR = "/vobs/MY_VOB_DIR/path/to/root"

# The tool uses cache directory to place ClearCase version files there. The cache speeds up the transfer process
# in many times in subsequent attempts (up to 10 times). It may be recommended to start the tool 2 days before the
# actual transfer loading all files to the cache. So only new versions appeared during the 2 days will be retrieved from
# ClearCase in the day of the transfer.
# NOTE: Make sure there is enough space in cache directory.
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
SVN_AUTOPROPS_FILE = CONFIG_DIR + "/config.autoprops"

# If CONVERT_ALL_CC_LABELS is True, the tool will convert all labels it finds in history of the current view
# If CONVERT_ALL_CC_LABELS is False (recommended), the tool will transfer only those labels mentioned in CC_LABELS_FILE
CONVERT_ALL_CC_LABELS = False 
CC_LABELS_FILE = CONFIG_DIR + "/labels.txt"

# If the tool finds the size of the file in cache is zero, it may try loading the file from ClearCase again.
# This is to make sure zero size is not due to previous unsuccessful retrieving attempt.
CHECK_ZEROSIZE_CACHEFILE = True

# Should svndump contain the command to create SVN /branches and /tags directory or not
# It will be an error if you try loading the dump with such command to SVN repository containing these directories
SVN_CREATE_BRANCHES_TAGS_DIRS = False

# SVN dump output file created by the tool
SVN_DUMP_FILE = "svndump.txt"

# ClearCase history file created by the tool
HISTORY_FILE = "cchistory.txt"

