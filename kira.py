try:
  login_status = str(input('apakah anda sudah login?(True/False): '))
  
  if login_status == 'true' or login_status == 'True':
    user = True
  else:
    user = False
  
  if not user:
    print('Anda belum login!🙏')
  else:
    print('Anda sudah login!🤝')
   
  card_access = str(input('Punya kartu akses?(True/False)'))
  
  if card_access == 'true' or card_access == 'True':
    user = True
  else:
    user = False
    
  if not card_access:
    print('Anda tidak mempunyai kartu akses❌')
  else:
    print('Anda mempunyai kartu akses!😁')
   
  if (card_access == 'true' or card_access == 'True') and (login_status == 'true' or login_status == 'True'):
    print('akses diterima! anda sudah memenuhi syarat!')
  else:
    print('akses anda ditolak! syarat belum terpenuhi')
except ValueError: 
  print('tolong input data dengan benar!🤡🤡')