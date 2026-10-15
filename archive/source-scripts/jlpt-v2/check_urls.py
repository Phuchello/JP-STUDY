from pathlib import Path
import re,json,time,urllib.request,urllib.error,concurrent.futures,sys
from urllib.parse import urlparse
from pypdf import PdfReader

root=Path(__file__).resolve().parents[2];tmp=root/'tmp/jlpt-v2'
allowed={'www.jlpt.jp','hn.jpf.go.jp','www.irodori.jpf.go.jp','ask-books.com','tadoku.org','apps.ankiweb.net','docs.ankiweb.net','www.science.org','wixtedlab.ucsd.edu','pubmed.ncbi.nlm.nih.gov','www.aasm.org','support.google.com','onlinelibrary.wiley.com','gemini.google.com','notebooklm.google.com','jf.xcms.online','learninglab.psych.purdue.edu','eric.ed.gov'}
urls=set()
for p in (root/'FINAL').glob('*.md'):
    urls.update(re.findall(r'\]\((https?://[^\s]+)\)',p.read_text(encoding='utf-8')))
for p in (root/'FINAL').glob('*.pdf'):
    for page in PdfReader(p).pages:
        for ref in page.get('/Annots',[]):
            a=ref.get_object().get('/A',{})
            if a.get('/S')=='/URI':urls.add(str(a['/URI']))
urls={u for u in urls if urlparse(u).hostname in allowed}
def check(u):
    started=time.monotonic()
    req=urllib.request.Request(u,method='HEAD',headers={'User-Agent':'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req,timeout=12) as r:
            return dict(url=u,status=r.status,final=r.url,content_type=r.headers.get('Content-Type'),seconds=round(time.monotonic()-started,2))
    except urllib.error.HTTPError as e:
        if e.code in (404,405):
            try:
                request=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Range':'bytes=0-4095'})
                with urllib.request.urlopen(request,timeout=12) as r:
                    sample=r.read(4096)
                    return dict(url=u,status=r.status,method='GET after HEAD '+str(e.code),final=r.url,content_type=r.headers.get('Content-Type'),sample_length=len(sample),seconds=round(time.monotonic()-started,2))
            except Exception as retry:return dict(url=u,status=getattr(retry,'code',None),error=str(retry),head_status=e.code,seconds=round(time.monotonic()-started,2))
        return dict(url=u,status=e.code,error=str(e),seconds=round(time.monotonic()-started,2))
    except Exception as e:
        if 'timed out' in str(e):
            try:
                request=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0','Range':'bytes=0-4095'})
                with urllib.request.urlopen(request,timeout=15) as r:
                    sample=r.read(4096)
                    return dict(url=u,status=r.status,method='GET after timeout',final=r.url,content_type=r.headers.get('Content-Type'),sample_length=len(sample),seconds=round(time.monotonic()-started,2))
            except Exception as retry:return dict(url=u,status=getattr(retry,'code',None),error=str(retry),seconds=round(time.monotonic()-started,2))
        return dict(url=u,status=None,error=str(e),seconds=round(time.monotonic()-started,2))
cached={}
if '--new-only' in sys.argv:
    cached={x['url']:x for x in json.loads((tmp/'url_checks.json').read_text(encoding='utf-8')) if x['url'] in urls}
    (tmp/'url_checks_before_repair.json').write_text((tmp/'url_checks.json').read_text(encoding='utf-8'),encoding='utf-8')
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    result=list(pool.map(check,sorted(urls-set(cached))))+list(cached.values())
(tmp/'url_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'checked':len(result),'status_counts':{str(s):sum(x['status']==s for x in result) for s in sorted({x['status'] for x in result},key=str)},'issues':[x for x in result if x['status']!=200]},ensure_ascii=False))
