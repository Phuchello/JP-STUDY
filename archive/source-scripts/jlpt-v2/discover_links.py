from pathlib import Path
import urllib.request, re, json, html
from urllib.parse import urljoin
from html.parser import HTMLParser

ROOT=Path(__file__).resolve().parent
PAGES=['https://hn.jpf.go.jp/irodori/so-cap-1','https://hn.jpf.go.jp/irodori/nhap-mon']
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if v and (k in ['href','src','onclick'] or 'pdf' in v or 'mp3' in v):self.links.append([tag,k,v])
result=[]
for u in PAGES:
    try:
        req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=25) as r:
            data=r.read(2_000_000).decode('utf-8',errors='replace');status=r.status;final=r.url
        p=Links();p.feed(data)
        name=u.rsplit('/',1)[-1].replace('.html','')
        (ROOT/(name+'.html')).write_text(data,encoding='utf-8')
        links=[{'attribute':k,'url':urljoin(final,v) if k!='onclick' else v} for tag,k,v in p.links if any(x in v.lower() for x in ['sample2018','.mp3','.pdf','elementary','audio','shokyu','download'])]
        result.append({'url':u,'status':status,'final':final,'links':links})
    except Exception as e:result.append({'url':u,'error':str(e)})
(ROOT/'discovered_links.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
for x in result:
    print(json.dumps(x,ensure_ascii=False))
