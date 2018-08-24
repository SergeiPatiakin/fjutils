# This script is on the system's fast path. It's got to be fast.
if [ -z "$FJUTILS_PATH" ]; then
	echo 'Configuration error: $FJUTILS_PATH is not defined'
elif [ -z "$MACHINE_NICKNAME" ]; then
	echo 'Configuration error: $MACHINE_NICKNAME is not defined'
else
	export PATH="${PATH}:$FJUTILS_PATH/bin"
	export PS1="\[\033[0;30;33m\]$MACHINE_NICKNAME\$(fjproj_current):\[\033[32m\]\w\[\e[0m\]\\\$ "
	fjproj_current()
	{
		if [ -n "$FJPROJ_CURRENT" ]; then
			echo -n "($FJPROJ_CURRENT)"
		fi
	}
	cdp()
	{
		eval "$(ssc_cdp $@)"
	}
	fjp()
	{
		eval "$(ssc_fjp $@)"
	}
fi