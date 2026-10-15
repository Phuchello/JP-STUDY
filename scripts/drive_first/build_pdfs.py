from pathlib import Path
import json,re,html,os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,PageBreak
R=Path(__file__).resolve().parents[2];O=R/'deliverables/phase3.5';T=R/'tmp/drive-first';lib={p['id']:p for p in json.loads((R/'deliverables/phase3/JAPANESE_PATTERN_LIBRARY/patterns.json').read_text(encoding='utf-8'))['patterns']}
for n,f in [('VN','arial.ttf'),('VNB','arialbd.ttf')]:pdfmetrics.registerFont(TTFont(n,'C:/Windows/Fonts/'+f))
pdfmetrics.registerFontFamily('VN',normal='VN',bold='VNB');pdfmetrics.registerFont(TTFont('JP','C:/Windows/Fonts/msgothic.ttc',subfontIndex=0))
styles={n:ParagraphStyle(n,fontName='VNB' if n in ['title','head'] else 'VN',fontSize=z,leading=l,spaceAfter=gap,keepWithNext=n in ['title','head']) for n,z,l,gap in [('title',20,25,14),('head',12,16,8),('body',12,17,10),('small',10,14,8)]}
def rich(s):return re.sub(r'[\u3000-\u30ff\u3400-\u9fff\uff00-\uffef]+',lambda m:'<font name="JP">'+m[0]+'</font>',html.escape(str(s))).replace('\n','<br/>')
def p(s,k='body'):return Paragraph(rich(s),styles[k])
def a(label,url):return Paragraph('<link href="'+html.escape(url,quote=True)+'" color="#16456c"><u>'+rich(label)+'</u></link>',styles['body'])
def make(dest,pages):
 story=[]
 for j,(title,items) in enumerate(pages):
  if j:story.append(PageBreak())
  story.append(p(title,'title'));story+=items
 def foot(c,d):c.setFont('VN',8);c.setFillColor(colors.HexColor('#555555'));c.drawString(42,25,'JP-STUDY · Phase 3.5 · tham chiếu vừa sức');c.drawRightString(A4[0]-42,25,str(d.page))
 SimpleDocTemplate(str(dest),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=42,author='JP-STUDY',title=pages[0][0]).build(story,onFirstPage=foot,onLaterPages=foot)
def start(url=None):
 first=[p('Mở một bảng → chọn một việc → làm → chữa một lỗi → dừng. Không cần quản lý cây thư mục hoặc đọc hết tài liệu.')]
 first += [a('MỞ HỌC HÔM NAY',url)] if url else [p('Mở bảng JP_STUDY_HOC_HOM_NAY được người quản lý cấp riêng. Bản công khai này không chứa đường dẫn Drive riêng.')]
 first += [p('Khi đủ sức','head'),p('1. Bài đầu dự kiến: N4 trợ từ, 5 câu, khoảng 5–8 phút. Nếu ô báo “Chờ kích hoạt Forms”, chưa có quiz trực tuyến; chọn nghe/nói bên dưới hoặc để hôm khác.\n2. Chọn “Tự làm” chỉ khi chưa xem câu/khóa và không tra. Đã thấy thì chọn ôn; có gợi ý thì chọn hỗ trợ. Được bỏ trống.\n3. Sau Nộp, bấm Xem điểm; chỉ lúc này mới xem giải thích.\n4. Trở lại bảng → CHỮA MỘT LỖI → chép B9 vào Gemini nếu muốn. Không có lỗi thì dừng luôn.'),p('Khi mệt','head'),p('Buồn ngủ hoặc kiệt sức: nghỉ là hợp lệ. Nếu còn tỉnh và muốn, ôn cũ tối đa 5–10 phút. Ngày bình thường thử 20–25 phút tổng; đủ sức thử 45–60 phút được chia nhỏ. Không bớt ngủ, không học bù.'),p('Các phút là mức thử, chưa phải khả năng đã xác nhận. Không có chuỗi ngày bắt buộc.','small')]
 second=[p('Một tuần là kho lựa chọn','head'),p('Không cần làm đủ bảy ngày. Chỉ hoàn thành một việc trong tuần vẫn dùng được hệ thống.\n• Một quiz trợ từ ngắn.\n• Một quiz từ/kanji.\n• Nghe một đoạn chính thức rồi mới xem chữ.\n• So một mẫu ngữ pháp dễ nhầm.\n• Một đoạn đọc ngắn.\n• Chữa một lỗi với Gemini.\n• Tùy sức: một vai nói 3 phút.'),a('Nghe chính thức: Irodori','https://www.irodori.jpf.go.jp/en/elementary01/'),a('Mở Gemini — tự chép gói lỗi, không tự đọc Drive','https://gemini.google.com/'),p('Giữ dữ liệu riêng','head'),p('Đừng gửi cả lịch sử học qua link công khai. Không chia sẻ thư mục gốc. Người quản lý chỉ cấp bảng và học liệu cần dùng cho đúng người; dữ liệu gốc và báo cáo riêng ở thư mục theo dõi. Tab ẩn không bảo vệ quyền truy cập.'),p('Điểm quiz gốc không phải điểm JLPT. Chưa có ngân hàng N3/N2. Quiz văn bản không đo nghe hoặc nói. iPad/điện thoại thật và Forms sau kích hoạt còn cần thử trực tiếp.','small')]
 return [('Bắt đầu ở một màn hình',first),('Chọn vừa sức và giữ riêng tư',second)]
make(O/'00_BAT_DAU_O_DAY.pdf',start())
topics=[('01_NGU_PHAP_N4.pdf','Nền N4: đọc đúng vai và thể',['G02','G08'],'Đọc một câu trong bài học và xác định ai làm gì, ở đâu, thể nào.'),('02_MEO_NGHE.pdf','Nghe: theo thông tin được sửa',['L01'],'Lịch gặp thay đổi: giữ giờ/ngày cuối cùng đã xác nhận.'),('03_MEO_DOC.pdf','Đọc: tìm đúng vùng bằng chứng',['R02'],'Đọc thông báo mua hàng/lịch sử dụng rồi xác định điều kiện áp dụng.'),('04_NGU_PHAP_DE_NHAM.pdf','So điều kiện có ngữ cảnh',['G07'],'Chọn cách nói theo quan hệ điều kiện; không dịch mọi mẫu thành một chữ “nếu”.'),('05_GIAO_TIEP_DOI_SONG.pdf','Giao tiếp: xác nhận cho rõ',['T06'],'Xác nhận lại giờ hoặc thông tin trước khi thực hiện.'),('06_KHUNG_VIET_NOI.pdf','Khung nhắn và nói một việc',['T03'],'Nhờ thay đổi một thời điểm; tự thay dữ kiện, không sao chép câu mẫu như dữ liệu thật.')]
for filename,title,ids,use in topics:
 pages=[]
 for i in ids:
  c=lib[i];items=[p(i+' · '+c['nameVi'],'head'),p('Dùng khi: '+use),p(c.get('meaningVi') or c.get('listenFor') or c.get('formality') or c.get('formula',''))]
  example=c.get('minimalPair') or c.get('example') or c.get('dialogue') or c.get('formula');items+=[p('Ví dụ gốc đã rà','head'),p(example)]
  extra=c.get('contrastVi') or c.get('exampleVi') or c.get('dialogueVi');
  if extra:items+=[p(extra)]
  if c.get('formula') and c.get('formula')!=example:items+=[p('Khung: '+c['formula'])]
  ex=c['practice'][0] if c.get('practice') else None
  if ex:items+=[p('Tự thử một lần','head'),p(ex['stem']),p(' / '.join(str(j+1)+'. '+v for j,v in enumerate(ex['options']))),p('Sau khi thử: '+ex['answerVi'],'small')]
  else:items += [p('Tự thử: '+c.get('exerciseVi','Đổi một dữ kiện và tự nói một câu.'))]
  items += [p('Nếu mở thẻ trong lúc đo, ghi có trợ giúp. Ví dụ ở phiếu là học có hướng dẫn, không tính điểm mới.','small'),a('CHỮA / TẬP MỘT CÂU VỚI GEMINI','https://gemini.google.com/')]
  if c.get('sources'):items += [a('Tham khảo: '+c['sources'][0]['title'],c['sources'][0]['url'])]
  pages.append((title,items))
 make(O/filename,pages)
print('Public: 7 PDFs; owner dashboard URL is handed over separately and never embedded here.')
