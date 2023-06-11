# IPTV channels A1 (kino)

```
https://raw.githubusercontent.com/maltsevvv/iptv/main/a1.m3u
```

#### Full channel list A1 (voka.tv) https://github.com/mashrum/a1_m3u

### Сканирование iptv A1
```
wget https://raw.githubusercontent.com/maltsevvv/iptv/main/iptvsearch.py
```  
```
python3 iptvsearch.py
```

### EPG https://iptvx.one/epg/epg_lite.xml.gz

### Resize file EPG for:
### *LibreElec*

Folder for configuration file `/storage/.config`  
Folder for EPG `/storage/downloads/`  

```
wget -P /storage/.config/ https://raw.githubusercontent.com/maltsevvv/iptv/main/epg.sh
```

```
chmod +x /storage/.config/epg.sh
```

#### Запуск `sh /storage/.config/epg.sh`

#### Запуск каждые 3 часа. ADD in crontab  
```
crontab -e
```  
```
0 */3 * * * /usr/bin/bash /storage/.config/epg.sh
```
  
### *Raspbian*

Folder for configuration file `/usr/local/bin/`  
Folder for EPG `/home/pi/`  

```
wget -P /usr/local/bin/ https://raw.githubusercontent.com/maltsevvv/iptv/main/epg.sh
```

```
sudo chmod +x /usr/local/bin/epg.sh
```

#### Запуск `sh /storage/.config/epg.sh`

#### Запуск каждые 3 часа. ADD in crontab  
```
crontab -e
```  
```
0 */3 * * * /usr/bin/bash /usr/local/bin/epg.sh
```

