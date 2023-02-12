## Редактироване файла EPG.xml

tee -a /usr/local/bin/epg.sh <<_EOF_
#!/bin/bash
curl -s -L --connect-timeout 5 --max-time 10 --retry 5 --retry-delay 5 --retry-max-time 40 'https://iptvx.one/epg/epg_lite.xml.gz' | zcat | sed -n -e '1,3 p' -e '/channel.*"\(tv1000.*\|.*kino.*\|hollywood\|nst\|muvitv\|amedia.*\|vip.*\|gulli-girl\|sts-kids-hd\|mult.*\|backustv.*\)"/p' -e '$a<\/tv>' >> /home/pi/epg.xml
_EOF_


sudo tee -a /etc/systemd/system/epg.service  <<_EOF_
[Unit]
Description=Downloads and edit EPG
Wants=epg.timer

[Service]
Type=oneshot
ExecStart=/usr/local/bin/epg.sh

[Install]
WantedBy=multi-user.target
_EOF_


sudo tee -a /etc/systemd/system/epg.timer  <<_EOF_
[Unit]
Description=Start service EPG every 3 hours
Requires=epg.service

[Timer]
Unit=epg.service
OnCalendar=*-*-* *:03:00 

[Install]
WantedBy=timers.target
_EOF_