import datetime
from docx import Document


def save_document(doc: Document, prefix="融课数据表"):
    # 生成当前日期和时间字符串，精确到小时
    current_time = datetime.datetime.now().strftime("%Y%m%d%H")

    # 创建文件名
    filename = f"{prefix}-{current_time}.docx"

    # 保存文档
    doc.save(filename)

    return filename
