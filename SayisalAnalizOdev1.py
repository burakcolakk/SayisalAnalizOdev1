import math

x = math.pi / 5
gercekdeger = math.cos(x)

yaklasim1 = math.cos(0)
birincikesmehatasi = abs(gercekdeger - yaklasim1)

yaklasim2 = 1 - (x ** 2) / 2
ikincikesmehatasi = abs(gercekdeger - yaklasim2)

print(f"f(𝜋/5) fonksiyonu gerçek değeri: {gercekdeger}")
print(f"Tek terimle yaklaşım: {yaklasim1}")
print(f"İki terimle yaklaşım: {yaklasim2}")
print(f"Birinci kesme hatası: {birincikesmehatasi}")
print(f"İkinci kesme hatası: {ikincikesmehatasi}")