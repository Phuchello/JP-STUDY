from pathlib import Path
import json,re,html
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,Spacer,PageBreak
R=Path(__file__).resolve().parents[1];O=R/'deliverables/phase3';T=R/'tmp/pdf-build';T.mkdir(parents=True,exist_ok=True)
for n,f in [('VN','arial.ttf'),('VNB','arialbd.ttf')]:pdfmetrics.registerFont(TTFont(n,'C:/Windows/Fonts/'+f))
pdfmetrics.registerFontFamily('VN',normal='VN',bold='VNB');pdfmetrics.registerFont(TTFont('JP','C:/Windows/Fonts/msgothic.ttc',subfontIndex=0))
W,H=A4;AW=W-80
def rich(s):
 s=html.escape(str(s));s=re.sub(r'\*\*(.*?)\*\*',r'<b>\1</b>',s);s=re.sub(r'[\u3000-\u30ff\u3400-\u9fff\uff00-\uffef]+',lambda m:'<font name="JP">'+m.group()+'</font>',s);return s.replace('\n','<br/>')
styles={k:ParagraphStyle(k,fontName='VNB' if k in ['title','head'] else 'VN',fontSize=z,leading=l,textColor=colors.HexColor('#203747'),spaceAfter=sp,keepWithNext=k in ['title','head']) for k,z,l,sp in [('title',21,26,14),('head',12.5,16,7),('body',12,16.2,9),('small',10,13.5,7),('compact',11,14.8,7)]}
def p(s,kind='body'):return Paragraph(rich(s),styles[kind])
def link(label,url):return Paragraph('<link href="'+html.escape(url,quote=True)+'" color="#174e67"><u>'+rich(label)+'</u></link>',styles['body'])
def table(rows,widths=[.28,.72]):
 z=Table([[p(c,'compact') for c in row] for row in rows],colWidths=[AW*x for x in widths],hAlign='LEFT');z.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e6f0f1')),('VALIGN',(0,0),(-1,-1),'TOP'),('LINEBELOW',(0,0),(-1,-1),.4,colors.HexColor('#c3cfd4')),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]));return z
layouts={}
def pdf(name,pages):
 story=[];titles=[];metrics=[]
 for i,(title,items) in enumerate(pages):
  items=[p(title,'title')]+items;titles.append(title);height=sum(x.wrap(AW-12,H-90)[1]+x.getSpaceAfter()+x.getSpaceBefore() for x in items);metrics.append({'page':i+1,'estimatedHeight':round(height,1),'available':H-95});story+=items
  if i+1<len(pages):story.append(PageBreak())
 def foot(c,d):
  c.bookmarkPage('p'+str(d.page));c.addOutlineEntry(titles[min(d.page-1,len(titles)-1)],'p'+str(d.page),level=0);c.setFont('VN',8);c.setFillColor(colors.HexColor('#4c606b'));c.drawString(40,25,'Bản công khai · 15/10/2026');c.drawRightString(W-40,25,str(d.page)+' / '+str(len(pages)))
 SimpleDocTemplate(str(O/name),pagesize=A4,leftMargin=40,rightMargin=40,topMargin=38,bottomMargin=43,title=pages[0][0],author='Hệ thống học tiếng Nhật cá nhân').build(story,onFirstPage=foot,onLaterPages=foot);layouts[name]=metrics
start=[('Mở và học một việc',[
 p('Hôm nay chỉ cần: mở ứng dụng → chọn sức → làm vài câu → chữa một lỗi → dừng. Không phải đọc toàn bộ bộ tài liệu.'),link('Mở JLPT_PRACTICE/index.html','JLPT_PRACTICE/index.html'),
 table([['Sức hôm nay','Một lựa chọn vừa đủ'],['Buồn ngủ / kiệt sức','Nghỉ. Hoặc ôn câu cũ tối đa 5–10 phút nếu còn tập trung. Mệt 4–5: ứng dụng không giao chẩn đoán mới.'],['Bình thường','Thử 20–25 phút tổng: STANDARD 8–12 câu trong 15 phút + chữa một lỗi. Có thể dừng sớm.'],['Ngày nghỉ / đủ sức','Thử 45–60 phút, chia nhỏ. DEEP 25–40 phút gồm làm nhiều kỹ năng và chữa sau nộp; không phải nghĩa vụ mỗi ngày.']]),
 p('Đây là mức thử, chưa phải khả năng đã xác nhận. Không bớt ngủ, không học bù. Lịch ca phải do bạn xác nhận; không mặc định có ca khuya hằng ngày.'),p('Lần đầu đủ sức: chọn QUICK 3–5 câu một mục tiêu N4; sau đó STANDARD ngắn để lấy dữ liệu mới. Nếu không có giọng Nhật, ứng dụng bỏ phần nghe trong phiên tự chọn.'),p('Sau lỗi: mở “Học mẫu liên quan” 3–5 phút, tự đổi một chi tiết. Chỉ mở lời giải sau khi đã thử. Mẫu mở rộng là học có hướng dẫn, chưa tính điểm đo độc lập.'),p('Ưu tiên nghe/nói: một đoạn Irodori đã chọn hoặc một vai 3 phút. Không bắt đầu bằng đề N2 đầy đủ.')]),
 ('Làm, hiểu kết quả, giữ tiến độ',[
 table([['Bước','Việc cần làm'],['1 · Bắt đầu','Mở index.html bằng Chrome/Edge trên laptop. Chọn mức mệt hôm nay; không có giá trị mặc định giả. QUICK chấm từng câu; STANDARD/DEEP nộp rồi mới xem.'],['2 · Trong bài','Một câu trên màn hình. Chọn bằng chạm hoặc phím 1–4. Tích “đã đoán” nếu chưa chắc. Có thể bỏ trống hoặc nộp phần đã xem; câu chưa mở không tính sai.'],['3 · Sau nộp','Xem đúng/đã trả lời, câu trống; đọc một giải thích và bằng chứng. Ôn, có trợ giúp, đoán, gián đoạn được ghi riêng với câu mới tự làm.'],['4 · Gemini tùy chọn','Bấm “Sao chép lỗi”, tự mở Gemini và dán. Gia sư hỏi câu mới rồi chờ bạn trả lời. Nút chỉ sao chép; không đọc lịch sử hay ghi Excel.'],['5 · Dừng','Lưu tự động trong trình duyệt này. Trước khi đổi thiết bị/xóa trình duyệt, xuất JSON ở Sao lưu. CSV chỉ là tổng hợp cho trang Excel “Luyện tập”.']]),
 p('Laptop đã kiểm bằng Chrome chạy tự động. Bố cục 768×1024 và 1024×768 đã kiểm mô phỏng, chưa thử iPad thật. iPad/ứng dụng Files có thể không chạy HTML local; nếu mở chỉ thấy bản xem trước, dùng laptop. Không hứa Safari/voice hoạt động khi chưa thử.'),p('Nghe dùng giọng tổng hợp Nhật nếu thiết bị có. Không phải âm JLPT, chưa kiểm chất lượng âm thực. Nguồn chính thức có MP3 trong sổ Excel; khi luyện bằng bản chữ, không tính là nghe độc lập.'),p('Đã có 80 câu gốc nền N4, 4 vai nói, 30 cách ghép bài từ cùng ngân hàng, 31 thẻ mẫu. Chưa có 300–500 câu, chưa mở ngân hàng N3/N2. Bộ mới hữu hạn; hết câu mới thì ghi rõ là ôn.')]),
 ('Sau 7 / 14 ngày và kỳ N2',[
 p('Bản công khai dùng hồ sơ ví dụ tổng hợp: người lớn vừa học vừa làm, quỹ học thay đổi, ưu tiên nghe/nói. Chưa có chẩn đoán để gán trình độ hoặc dự báo đỗ N2. Mốc tài liệu 15/10/2026; kỳ JLPT tham chiếu 06/12/2026.'),
 table([['Mốc từ buổi đầu thật','Xem gì và điều chỉnh'],['D7','Có mở học vừa sức không? Mẫu lỗi nào lặp ≥2? Có thường cần gợi ý, đoán hoặc bị gián đoạn không? Nếu quá tải: giảm số câu/độ khó, không tăng giờ bằng cách bớt ngủ.'],['D14','Có câu CHƯA THẤY cùng mục tiêu sau ≥3 ngày không? Tách câu cũ/có hỗ trợ. Cần ≥5 câu mới mỗi nhóm để xem xu hướng; ít hơn ghi “chưa đủ dữ liệu”, không kết luận làm chủ.'],['Thử N3 / phần N2','Chỉ sau hai lần khác câu, nền N4 tự làm ổn, hiểu được bằng chứng và vẫn vừa sức. Ngưỡng thử 80% là quy tắc dự án, không chứng nhận JLPT. Thử một khối chính thức trong sổ cũ; chưa làm trọn N2.']]),
 p('Phiếu bổ sung tùy khi có dữ liệu — không cần trả lời mới được bắt đầu:', 'head'),
 p('1. Tuần gần nhất: giờ lớp, việc và số ca khuya từng ngày?\n2. Giờ ngủ và thời gian đi tàu thực tế từng ngày?\n3. Sau 7 ngày thử, phiên nào vừa sức, phiên nào quá tải?\n4. Có bảng điểm N3 cũ hoặc kết quả N4/N3 mới kèm số câu, ngày và trợ giúp không?\n5. Trên lớp đang dùng sách/bài nào, phần nào còn dang dở?\n6. Trình duyệt/iPad có mở được ứng dụng và giọng Nhật không?'),
 p('QA: tác tử AI khác kiểm mù 80/80 câu và 4 vai lượt đầu; tác giả đã sửa lỗi. Lượt kiểm sau sửa đã đạt; 31 thẻ và 37 câu học cũng đã được rà độc lập. Chưa có thẩm định bản ngữ, hiệu chuẩn người học hay kiểm âm TTS. Không coi điểm luyện là điểm chuẩn JLPT. Chi tiết trong QA_REPORT.md.','small')])]
pdf('START_HERE.pdf',start)
