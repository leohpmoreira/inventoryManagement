from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

import sqlite3

def mm2p(milimetros):
    return milimetros / 0.352777


data = sqlite3.connect("inventory.db")
cur = data.cursor()
cnv = canvas.Canvas("meu_pdf.pdf")


cnv.drawString(mm2p(22),mm2p(275),"ID")
cnv.drawString(mm2p(42),mm2p(275), "TIPO")
cnv.drawString(mm2p(72),mm2p(275) , "PRODUTO")
cnv.drawString(mm2p(104),mm2p(275) , "QUANTIDADE")
cnv.drawString( mm2p(140),mm2p(275), "DATA")


eixoy=250
#select * from Movimentacao where strftime('%m', Data) = '06' and  strftime('%Y', Data) = '2022';
# cur.execute("SELECT * FROM Login WHERE UserID = :login AND Password = :passwd",{'login': self.lineEdit_user.text(), 'passwd': pwd})
cur.execute("select * from Movimentacao where strftime('%m', Data) = :month and  strftime('%Y', Data) = :year;",{'month':"06",'year':"2022"})
results = cur.fetchall()
for row in results:
    cnv.drawString(mm2p(22),mm2p(eixoy),str(row[0]))
    cnv.drawString(mm2p(42),mm2p(eixoy),str(row[1]))
    cnv.drawString(mm2p(72),mm2p(eixoy),str(row[2]))
    cnv.drawString(mm2p(104),mm2p(eixoy),str(row[3]))
    cnv.drawString(mm2p(140),mm2p(eixoy),str(row[4]))

    eixoy -= 15
data.close()
cnv.save()
