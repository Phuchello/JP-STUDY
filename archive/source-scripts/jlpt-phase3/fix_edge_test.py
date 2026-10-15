from pathlib import Path
p=Path(__file__).resolve().parent/'test_edge_flows.cjs';s=p.read_text(encoding='utf-8').replace("includes('Không đọc được')","includes('Chưa có lưu tự động')");p.write_text(s,encoding='utf-8')
