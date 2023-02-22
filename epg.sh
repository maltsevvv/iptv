#!/bin/bash

url=https://iptvx.one/epg/epg_lite.xml.gz 
folder='/storage/downloads/'
epg_full=$folder'epg_lite.xml'
epg=$folder'epg.xml'

if wget -P $folder -q $url; then
	rm $epg_full $epg
	gunzip $epg_full'.gz'
	sed -n -e '1,3 p' $epg_full >> $epg
	###################################
	grep -e 'tv1000.*' $epg_full >> $epg
	grep -e '.*kino.*' $epg_full >> $epg
	grep -e 'hollywood' $epg_full >> $epg
	grep -e 'nst' $epg_full >> $epg
	grep -e 'muvitv' $epg_full >> $epg
	grep -e 'amedia.*' $epg_full >> $epg
	grep -e 'vip.*' $epg_full >> $epg
	grep -e 'gulli-girl' $epg_full >> $epg
	grep -e 'sts-kids-hd' $epg_full >> $epg
	grep -e 'mult.*' $epg_full >> $epg
	grep -e 'backus.*' $epg_full >> $epg
	###################################
	grep -e '</tv>' $epg_full >> $epg
else
	exit 0
fi
