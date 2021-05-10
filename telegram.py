#!/usr/bin/python3
import telebot
import mysql.connector

mydb = mysql.connector.connect(
host='localhost',
user='root',
passwd='',
database='data penjualan')

#cek database sudah bisa diakses apa belum
# print(mydb)
#memberi input ke SQL
sql = mydb.cursor()

api = '1779306907:AAFqNwsvUuVRJufM_pYDXlq0XFQH3P1DLR0'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['penjualan'])
def penjualan(message):
  #split message
  texts = message.text.split(' ')
  # print(texts)
  #ambil parameter tanggal
  tanggal = texts[1]

  #input untuk SQL, ambil nama_item dan jumlah_dalam_kg
  sql.execute("select nama_item, jumlah_dalam_kg from     data_penjualan_harian where tanggal='{}'".format(tanggal))
  hasil_sql = sql.fetchall()
  # print(hasil_sql)

  #pesan yang dikirim oleh bot
  pesan_balasan = ''
  for x in hasil_sql:
     pesan_balasan = pesan_balasan + str(x) + '\n'

  #memperbagus balasan bot
  #menghilangkan tanda petik
  pesan_balasan = pesan_balasan.replace("'","")
  #menghilangkan tanda kurung
  pesan_balasan = pesan_balasan.replace("(","")
  pesan_balasan = pesan_balasan.replace(")","")
  #menghilangkan tanda koma
  pesan_balasan = pesan_balasan.replace(",","")

  bot.reply_to(message, pesan_balasan)


print('bot start running')
bot.polling()