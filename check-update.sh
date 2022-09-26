#!/bin/sh
curl http://releases.wildfiregames.com/ 2>/dev/null |sed -e 's,</tr>,</tr>\n,g' |grep alpha-unix-data |tail -n1 |sed -e 's,-alpha-unix-data.*,,;s,.*0ad-,,'
