# This script is on the system's fast path. It's got to be fast.
fjproj_current()
{
	if [ -n "$FJPROJ_CURRENT" ]; then
		echo -n "($FJPROJ_CURRENT)"
	fi
}
cdp()
{
    eval "$(ssc_cdp.py $@)"
}