#!/usr/bin/python3
import telebot
import mysql.connector

mydb = mysql.connector.connect(
host='localhost',
user='root',
passwd='',
database='lokasi')

#cek database sudah bisa diakses apa belum
# print(mydb)
#memberi input ke SQL
sql = mydb.cursor()

api = '1785057036:AAEdS2avFRnv30F83N5yTM38GMg2FyAQc1U'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['posisi'])
def gps(message):
  #split message
  texts = message.text.split(' ')
  print(texts)
  #ambil parameter tanggal
  tanggal = texts[1]

  #input untuk Sql
  sql.execute("select ID, link from     data_lokasi where tanggal='{}'".format(tanggal))
  hasil_sql = sql.fetchall()
  print(hasil_sql)

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
 

  bot.reply_to(message, pesan_balasan)


print('bot start running')
bot.polling()