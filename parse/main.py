import sys
# sys.path.append('../')
from drain import LogParser

input_dir  = 'merge' # The input directory of log file
output_dir = 'result/'  # The output directory of parsing results
log_file   = 'merged_logs.log'  # The input log file name
log_format = '<Container_ID> <Date> <Time> <Level> <Component>: <Content>'  # Spark log format
# Regular expression list for optional preprocessing (default: [])
# regex      = [
#     r'block_(|-)[0-9]+' , # block id
#     r'(/|)([0-9]+\.){3}[0-9]+(:[0-9]+|)(:|)', # IP
#     r'(?<=[^A-Za-z0-9])(\-?\+?\d+)(?=[^A-Za-z0-9])|[0-9]+$', # Numbers
# ] # HDFS log regex list

# regex = [r"(\d+\.){3}\d+", r"\b[KGTM]?B\b", r"([\w-]+\.){2,}[\w-]+"] # Spark log regex list

# regex = [
#     r'(attempt|rdd|broadcast)_[\d_a-z]+ -> $1_<*>',
#     r'(\d+(?:\.\d+)?(?:\s*[A-Za-z]+)?)',
#     r'((?:at|to|driver):\s+)([^\s,)]+)',
#     r'task\s+[\d.]+\s+in\s+stage\s+[\d.]+\s+\(TID\s+\d+\)'
#     ]
# General log templating regex list
regex = [
    r"(hdfs://[^\s]+|spark://[^\s]+|/[\w/\-\.]+|akka\.tcp://[^\]]+)", # HDFS/Spark/akka URL
    r"\b\d+\.\d+\.\d+\.\d+\b",  # IP address
    r"\b\d+\.\d+\b",  # Float numbers
    r"\b\d+\b",         # Integer numbers
    r'\b(yarn,yxsu|yarn,curl|yarn, yxsu)\b', # YARN log
]

st         = 0.5  # Similarity threshold
depth      = 4  # Depth of all leaf nodes

parser = LogParser(log_format, indir=input_dir, outdir=output_dir,  depth=depth, st=st, rex=regex)
parser.parse(log_file)