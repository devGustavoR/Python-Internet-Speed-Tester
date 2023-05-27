import speedtest
#coding: utf-8

def verificar_velocidade():
  st= speedtest.Speedtest()
  
  velocidade_download=st.download() /1024 / 1024
  velocidade_upload = st.upload() / 1024 / 1024
  ping = st.results.ping

  print(f"Velocidade de Download:{velocidade_download: .2f} Mbps")
  print(f"Velocidade de Upload:{velocidade_upload: .2f} Mbps")
  print(f"Ping: {ping:.2f} ms")

  if velocidade_download >= 10 and velocidade_upload >= 5 and ping <= 50:
    print("\nNet boa pra jogar")
  else:
    print("Melhor tu pagar outra internt")

verificar_velocidade()