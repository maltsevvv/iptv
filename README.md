# IPTV channels A1 (movies)

```
https://raw.githubusercontent.com/maltsevvv/iptv/main/a1.m3u
```

### Full channel list A1 (voka.tv) https://github.com/mashrum/a1_m3u

### EPG https://iptvx.one/epg/epg_lite.xml.gz

## Редактирование epg.xml
```
 curl -s -L --connect-timeout 5 --max-time 10 --retry 5 --retry-delay 5 --retry-max-time 40 'https://iptvx.one/epg/epg_lite.xml.gz' | zcat | sed -n -e '1,3 p' -e '/channel.*"\(tv1000.*\|.*kino.*\|hollywood\|nst\|muvitv\|amedia.*\|vip.*\|gulli-girl\|sts-kids-hd\|mult.*\|backustv.*\)"/p' -e '$a<\/tv>' >> epg.xml
```

## Сканирование multicast

```
wget https://raw.githubusercontent.com/maltsevvv/iptv/main/iptvsearch.py
```

```
python3 iptvsearch.py
```
