from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
import sys
import mysql.connector
os.system("cls")
class baza_pyqt5(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(1350,680)
        self.setMaximumSize(1350,680)
        self.setWindowTitle("Saylov")
        
        self.tb=QTableWidget(self)
        self.setFont(QFont("Consolas",22))
        self.tb.setRowCount(3)
        self.tb.setColumnCount(6)
        self.tb.setGeometry(0,0,930,300)
        self.con=mysql.connector.connect(user='root',password='root',
                                          host='localhost',database='saylov')
        self.baza_show()
        
        self.btn=QPushButton("Refresh",self)
        self.btn.setGeometry(1100,20,200,50)
        self.btn.setFont(QFont("Consolas",18))
        self.btn.setStyleSheet("""border-color: rgb(0,255,0);
                              color: rgb(0,255,0);
                              border-radius: 25;
                              border-style: solid;
                              background-color: rgb(0,0,0);
                              border-width: 3px;""")
        self.btn.clicked.connect(self.baza_show)
        
        
    # #     #malumotni o'zgaritish
        
        self.lb=QLabel("      ADD INFO",self)
        self.lb.setGeometry(130,310,250,50)
        self.lb.setFont(QFont("Consolas",18))
        self.lb.setStyleSheet("""color: rgb(0,0,255);
                                background-color: rgb(247,233,142);
                                border-color: rgb(233,255,219);
                                border-width: 3px;
                              """)
        
        self.lb1=QLabel("Shahar:",self)
        self.lb1.setGeometry(40,370,150,40)
        self.lb1.setFont(QFont("Consolas",14))
        self.lb1.setStyleSheet("""color: rgb(0,0,0);""")
        
        self.shahar=QLineEdit(self)
        self.shahar.setGeometry(200,370,200,40)
        self.shahar.setFont(QFont("consolas",15))
        self.shahar.setStyleSheet("""background-color: rgb(227,218,201);
                                   color: rgb(0,128,128);
                                   """)
        
       
        
        self.lb2=QLabel("Uchastka raqami:",self)
        self.lb2.setGeometry(40,420,150,40)
        self.lb2.setFont(QFont("Consolas",14))
        self.lb2.setStyleSheet("""color: rgb(0,0,0);""")
        
        self.uchastka=QLineEdit(self)
        self.uchastka.setGeometry(200,420,200,40)
        self.uchastka.setFont(QFont("consolas",15))
        self.uchastka.setStyleSheet("""background-color: rgb(227,218,201);
                                   color: rgb(0,128,128);
                                   """)
        self.lb3=QLabel("Saylovchilar:",self)
        self.lb3.setGeometry(40,470,150,40)
        self.lb3.setFont(QFont("Consolas",14))
        self.lb3.setStyleSheet("""color: rgb(0,0,0);""")
        
        self.saylovchi=QLineEdit(self)
        self.saylovchi.setGeometry(200,470,200,40)
        self.saylovchi.setFont(QFont("consolas",15))
        self.saylovchi.setStyleSheet("""background-color: rgb(227,218,201);
                                   color: rgb(0,128,128);
                                   """)
        
        self.lb3=QLabel("Manzil:",self)
        self.lb3.setGeometry(40,520,150,40)
        self.lb3.setFont(QFont("Consolas",14))
        self.lb3.setStyleSheet("""color: rgb(0,0,0);""")
        
        self.manzil=QLineEdit(self)
        self.manzil.setGeometry(200,520,200,40)
        self.manzil.setFont(QFont("consolas",15))
        self.manzil.setStyleSheet("""background-color: rgb(227,218,201);
                                   color: rgb(0,128,128);
                                   """)
        
        self.lb3=QLabel("Tel raqam:",self)
        self.lb3.setGeometry(40,570,150,40)
        self.lb3.setFont(QFont("Consolas",14))
        self.lb3.setStyleSheet("""color: rgb(0,0,0);""")
        
        self.raqami=QLineEdit(self)
        self.raqami.setGeometry(200,570,200,40)
        self.raqami.setFont(QFont("consolas",15))
        self.raqami.setStyleSheet("""background-color: rgb(227,218,201);
                                   color: rgb(0,128,128);
                                   """)
        
        self.qushish=QPushButton("Qo'shish",self)
        self.qushish.setGeometry(250,630,150,40)
        self.qushish.setFont(QFont("Calibri",18))
        self.qushish.setStyleSheet("""
                        color: rgb(255,255,255);
                        border-color: rgb(220,220,220);                        
                        border-width: 3px;
                        border: 5px ridge purple;                       
                        background-color: rgb(70,130,180);
                        """)
        self.qushish.clicked.connect(self.addatabase)
        
        self.lab=QLabel("    CHANGE INFO",self)
        self.lab.setGeometry(650,310,250,50)
        self.lab.setFont(QFont("Consolas",18))
        self.lab.setStyleSheet("""color: rgb(0,0,255);
                               background-color: rgb(247,233,142);
                                border-color: rgb(233,255,219);
                                border-width: 3px;""")    
        
        self.cmb1=QComboBox(self)
        self.cmb1.setGeometry(550,370,200,40)
        self.cmb1.setFont(QFont("Consolas",16))
        self.cmb1.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        self.cmb1.addItems(["shahar","uchastka_raqami","saylovchi_soni","manzil","tel_raqam"])
        
        self.txt1=QLineEdit(self)
        self.txt1.setGeometry(550,420,250,40)
        self.txt1.setFont(QFont("consolas",15))
        self.txt1.setStyleSheet("""background-color: rgb(227,218,201);
                                   color: rgb(0,128,128);
                              """)
        
        self.cmb2=QComboBox(self)
        self.cmb2.setGeometry(850,370,200,40)
        self.cmb2.setFont(QFont("Consolas",16))
        self.cmb2.setStyleSheet("""border-color: rgb(255,255,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;""")
        self.cmb2.addItems(["shahar","uchastka_raqami","saylovchi_soni","manzil","tel_raqam"])
        

        self.txt2=QLineEdit(self)
        self.txt2.setGeometry(850,420,250,40)
        self.txt2.setFont(QFont("consolas",15))
        self.txt2.setStyleSheet("""background-color: rgb(227,218,201);
                                   color: rgb(0,128,128);
                              """)
        
        
        self.yangilash=QPushButton("Update",self)
        self.yangilash.setGeometry(790,490,150,40)
        self.yangilash.setFont(QFont("Calibri",18))
        self.yangilash.setStyleSheet("""
                        color: rgb(255,255,255);
                        border-color: rgb(220,220,220);                        
                        border-width: 3px;
                        border: 5px ridge purple;                       
                        background-color: rgb(70,130,180);
                        """)
        self.yangilash.clicked.connect(self.baza_update)
    
    def addatabase(self):
        shahar = self.shahar.text()
        uchastka = self.uchastka.text()
        saylovchi = self.saylovchi.text()
        manzil=self.manzil.text()
        tel=self.raqami.text()

        if not shahar or not uchastka or not saylovchi or not manzil or not tel:
            QMessageBox.warning(self, "Xatolik", "Iltimos, barcha maydonlarni to'ldiring.")
            return

        sql = """INSERT INTO info(shahar,uchastka_raqami,saylovchi_soni,manzil,tel_raqam) VALUES(%s,%s,%s,%s,%s)"""
        tpl = (shahar, uchastka,saylovchi,manzil,tel)

        try:
            self.kur.execute(sql, tpl)
            self.con.commit()
            QMessageBox.information(self, "Ma'lumot saqlandi", "Ma'lumotlar bazaga muvaffaqiyatli saqlandi.")
        except:
            QMessageBox.critical(self, "Xatolik", "Ma'lumotlar saqlashda xatolik yuz berdi.")
   
        self.shahar.setText("")
        self.uchastka.setText("")
        self.saylovchi.setText("")
        self.manzil.setText("")
        self.raqami.setText("")
        
    def baza_show(self):
        self.tb.setFont(QFont("Consolas",18))
        self.tb.setStyleSheet("""border-color: rgb(0,0,255);
                              color: rgb(0,0,255);
                              border-width: 4px;
                              border-style: solid;
                              background-color: rgb(192,192,192);""")
        self.tb.setHorizontalHeaderLabels(["ID", "Shahar","Uchastka Raqami", "Saylovchilar", "Manzil","Tel raqam"])
        head=self.tb.horizontalHeader()
        for x in range(6):
            head.setSectionResizeMode(x,QHeaderView.ResizeToContents)
        
        self.kur=self.con.cursor()
        self.kur.execute("SELECT * from info")
        res=self.kur.fetchall()
        n=len(res)
        self.tb.setRowCount(n)
        self.tb.setVerticalHeaderLabels(["","","","","","","","","",""])
        sch=0
        for x in res:
            self.tb.setItem(sch,0,QTableWidgetItem(str(x[0])))
            self.tb.setItem(sch,1,QTableWidgetItem(x[1]))
            self.tb.setItem(sch,2,QTableWidgetItem(str(x[2])))
            self.tb.setItem(sch,3,QTableWidgetItem(str(x[3])))
            self.tb.setItem(sch,4,QTableWidgetItem(x[4]))
            self.tb.setItem(sch,5,QTableWidgetItem(str(x[5])))
            sch+=1
            
            
    def baza_update(self):
        
        tanlash=self.cmb1.currentText()
        tanlash2=self.cmb2.currentText()
        eski=self.txt1.text()
        yangi=self.txt2.text()
        self.kur=self.con.cursor()
        self.kur.execute(f"UPDATE info SET {tanlash2} = '{yangi}' where {tanlash}='{eski}'")
        self.con.commit()
        self.txt1.setText("")
        self.txt2.setText("")
    

    def closeEvent(self, event):
        result = QMessageBox.question(self, "Saylov", "Dasturni yopmoqchimisiz?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    
app=QApplication(sys.argv)
ilova=baza_pyqt5()
ilova.show()
sys.exit(app.exec_())