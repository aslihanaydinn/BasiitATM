import time
tonyHesap = {
    'name' : 'Tony Stark',
    'accountNo' : '918273645',
    'balance' : 950000,
    'adAccount' : 330000
}
steveHesap = {
    'name' : 'Steve Rogers',
    'accountNo' : '1029384756',
    'balance' : 30000,
    'adAccount' : 10000
}
natashaHesap = {
    'name' : 'Natasha Romanoff',
    'accountNo' : '142536478094',
    'balance' : 90000,
    'adAccount' : 10000
}


def paraCek(hesap):
     print(f"Merhaba {hesap['name']}")
     tutar = int(input("Ne kadar para çekmek istiyorsunuz?"))
     #bakiye = hesap['balance'] + hesap['adAccount']
     if (hesap['balance'] - tutar < 0):
          print(f'{hesap['name']} bakiyeniz yeterli değil! Ek hesaba yönlendiriliyorsunuz...')
          time.sleep(3.0)
          
          if ((hesap['balance'] + hesap['adAccount']) < tutar ):
               print(f'{hesap['name']} hesaplarınızda yeterli bakiye yok!')
          else:
               kalanBakiye = (hesap['balance'] + hesap['adAccount']) - tutar
               print(f'{hesap['name']} hesaplarınızdan para çekiliyor...')
               time.sleep(3.0)
               print(f'{hesap['name']} tüm hesaplarınızda kalan toplam bakiyeniz: {kalanBakiye}')
     else:
          hesap['balance']= hesap['balance'] - tutar
          print(f'{hesap['name']} hesabınızdan para çekiliyor...')
          time.sleep(3.0)
          print(f'{hesap['name']} paranız çekildi, ana hesabınızda kalan bakiyeniz: {hesap['balance']}')
paraCek(tonyHesap)

