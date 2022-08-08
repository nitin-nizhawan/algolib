
# this file must be sourced to work
# as it is intended to modify environment variable

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
# make python module import work 
# relative to clrs directory

export PATH=$SCRIPT_DIR:$PATH
export PYTHONPATH=$SCRIPT_DIR:$PYTHONPATH
