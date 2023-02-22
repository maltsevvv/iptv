# IPTV channels A1 (movies)

```
https://raw.githubusercontent.com/maltsevvv/iptv/main/a1.m3u
```

### Full channel list A1 (voka.tv) https://github.com/mashrum/a1_m3u



## Сканирование multicast

```
wget https://raw.githubusercontent.com/maltsevvv/iptv/main/iptvsearch.py
```

```
python3 iptvsearch.py
```



### EPG https://iptvx.one/epg/epg_lite.xml.gz

## Редактирование epg.xml
```
 curl -s -L --connect-timeout 5 --max-time 10 --retry 5 --retry-delay 5 --retry-max-time 40 'https://iptvx.one/epg/epg_lite.xml.gz' | zcat | sed -n -e '1,3 p' -e '/channel.*"\(tv1000.*\|.*kino.*\|hollywood\|nst\|muvitv\|amedia.*\|vip.*\|gulli-girl\|sts-kids-hd\|mult.*\|backustv.*\)"/p' -e '$a<\/tv>' >> epg.xml
```


### для LibreElec
```
tee -a /storage/.config/epg.sh <<_EOF_
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

_EOF_
```

```
chmod +x /storage/.config/epg.sh
```

### Запуск `sh /storage/.config/epg.sh`

### Запуск каждые 3 часа

crontab -e
```
0 */3 * * * /usr/bin/bash /storage/.config/epg.sh
```


