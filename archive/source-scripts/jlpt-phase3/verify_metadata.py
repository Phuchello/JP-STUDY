from pathlib import Path
import json,urllib.request,urllib.parse,concurrent.futures,time
T=Path(__file__).resolve().parent
dois=['10.1111/lang.12479','10.1111/modl.12581','10.3102/0034654307313795','10.1207/S15326985EP3801_3','10.1111/lang.12001','10.1002/tesq.157','10.1177/1362168815597504','10.1111/j.1467-9922.2010.00620.x','10.1111/j.1467-9922.2007.00398.x','10.1111/lang.12285','10.1111/flan.12272','10.30191/ets.202401_27(1).sp02','10.1017/S0272263109990520','10.1016/j.system.2013.07.013']
titles=['Sleep Deprivation and Memory Meta-Analytic Reviews of Studies on Sleep Deprivation Before and After Learning','Classroom Interventions and Foreign Language Anxiety A Systematic Review With Narrative Approach']
def fetch(item):
 try:
  if item in dois:url='https://api.crossref.org/works/'+urllib.parse.quote(item,safe='')
  else:url='https://api.crossref.org/works?rows=1&query.bibliographic='+urllib.parse.quote(item)
  req=urllib.request.Request(url,headers={'User-Agent':'JLPT-Learning-Research/1.0 (personal noncommercial study)'})
  with urllib.request.urlopen(req,timeout=25) as r:m=json.load(r)['message']
  if isinstance(m,dict) and 'items' in m:m=m['items'][0]
  return {'query':item,'DOI':m.get('DOI'),'title':m.get('title'),'authors':m.get('author'),'journal':m.get('container-title'),'published':m.get('published'),'online':m.get('published-online'),'print':m.get('published-print'),'url':m.get('URL'),'ok':True}
 except Exception as e:return {'query':item,'ok':False,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:out=list(ex.map(fetch,dois+titles))
(T/'verified_metadata.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
for m in out:print(json.dumps({k:v for k,v in m.items() if k not in ['authors']},ensure_ascii=False))
