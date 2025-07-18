#pythonda veri yapılarını içeren modül
#################################################################################################################################################
#-sayılar
#-stringler
#-boolean ifadeler
#-listler
#-dictionaries(sözlükler)
#-tuple(demet)
#set(küme)
#################################################################################################################################################


#1-sayılar(integer,float)
x=46
print(type(x))
b=10.5
print(type(b))
print(2 ** 2)#sayı karesi alma 2**2=2üstü2 ile
#tip dönüşümü int -> string
sayi1=100
yeniSayi=str(sayi1)
print(type(yeniSayi))

#################################################################################################################################################

#2-stringler
x1="python programlama dili"
print((x1))
print("John")
print('John')

"John"
name = "John"
name = 'John'

#######################
# Çok Satırlı Karakter Dizileri böyle oluşturulur """ """ arasına yazılır uzun metin
#######################

"""Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

long_str = """Veri Yapıları: Hızlı Özet, 
Sayılar (Numbers): int, float, complex, 
Karakter Dizileri (Strings): str, 
List, Dictionary, Tuple, Set, 
Boolean (TRUE-FALSE): bool"""

#######################
# Karakter Dizilerinin Elemanlarına Erişmek
#######################

name
name[0]
name[3]
name[2]

#######################
# Karakter Dizilerinde Slice İşlemi
#######################

name[0:2]
long_str[0:10]

#######################
# String İçerisinde Karakter Sorgulamak - in
#######################

long_str

"veri" in long_str

"Veri" in long_str

"bool" in long_str

###############################################
# String (Karakter Dizisi) Metodları
###############################################

dir(str)#*****************içine girilen veri tipinin metodlarını gösterir*****************

#######################
# len
#######################

name = "john"
type(name)
type(len)

len(name)
len("vahitkeskin")
len("miuul")

#######################
# upper() & lower(): küçük-büyük dönüşümleri
#######################

"miuul".upper()
"MIUUL".lower()



#soru? metot ve fonksiyon aynı şey fakat fark ne???
#metotlar class yapılarınının içindeki fonksiyonlardır. fakat fonksiyonlar global olarak tanımlanmışlardır. class yapısı içinde değillerdir


#######################
# replace: karakter değiştirir
#######################

hi = "Hello AI Era"
hi.replace("l", "p")

#######################
# split: böler
#######################

"Hello AI Era".split()


#######################
# capitalize: ilk harfi büyütür
#######################

"foo".capitalize()

dir("foo")

"foo".startswith("f")
#################################################################################################################################################

#3-boolean ifadeler True/False
5 == 4
1 == 1

#################################################################################################################################################

#4-Listeler[]
liste1=[1,2,3,4,5]
liste2=["python", "java", "c++"]
liste3=[1,2,3,"python", "java", "c++"]

# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır.yani içinde farklı veri tiplerini barındırabilir.

notes = [1, 2, 3, 4]
type(notes)
names = ["a", "b", "v", "d"]
not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]#list yapıları içinde farklı veri tipleri barındırabilir.

not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]

type(not_nam[6])

type(not_nam[6][1])

notes[0] = 99

not_nam[0:4]#listlerin slice işlemi


###############################################
# Liste Metodları (List Methods)
###############################################

dir(notes)#*****************içine girilen veri tipinin metodlarını gösterir*****************

#######################
# len: builtin python fonksiyonu, boyut bilgisi.
#######################

len(notes)
len(not_nam)

#######################
# append: eleman ekler
#######################

notes
notes.append(100)

#######################
# pop: indexe göre siler
#######################

notes.pop(0)

#######################
# insert: indexe ekler
#######################

notes.insert(2, 99)

#################################################################################################################################################

#5-Sözlükler(dictionaries)    {"key":value,} "key2":value2}........
sozluk1={"ad":"Ali", "soyad":"Yılmaz", "yas":30}
# Değiştirilebilir.
# Sırasız. (3.7 versiondan sonra sıralı.)
# Kapsayıcı.


dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Reg"}

dictionary["REG"]

#farklı key-value çiftleri
dictionary = {"REG": ["RMSE", 10],
              "LOG": ["MSE", 20],
              "CART": ["SSE", 30]}

dictionary = {"REG": 10,
              "LOG": 20,
              "CART": 30}

dictionary["CART"][1]

#######################
# Key Sorgulama
#######################

"YSA" in dictionary

#######################
# Key'e Göre Value'ya Erişmek
#######################

dictionary["REG"]
dictionary.get("REG")

#######################
# Value Değiştirmek
#######################

dictionary["REG"] = ["YSA", 10]

#######################
# Tüm Key'lere Erişmek
#######################
dictionary.keys()

#######################
# Tüm Value'lara Erişmek
#######################

dictionary.values()


#######################
# Tüm Çiftleri Tuple Halinde Listeye Çevirme
#######################

dictionary.items()

#######################
# Key-Value Değerini Güncellemek
#######################

dictionary.update({"REG": 11})

#######################
# Yeni Key-Value Eklemek
#######################

dictionary.update({"RF": 10})

#################################################################################################################################################

#6-Tuple(demetler)()
demet1=(1,2,3,4,5)
# - Değiştirilemez.
# - Sıralıdır.
# - Kapsayıcıdır.

t = ("john", "mark", 1, 2)
type(t)

t[0]
t[0:3]

t[0] = 99

t = list(t)
t[0] = 99
t = tuple(t)

#################################################################################################################################################

#7-Küme(set)  {1,2,3,4,5} sözlükler gibi süslü parantez ama key value yok
set1={1,2,3,4,5}
# - Değiştirilebilir.
# - Sırasız + Eşsizdir.
# - Kapsayıcıdır.

#######################
# difference(): İki kümenin farkı
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

# set1'de olup set2'de olmayanlar.
set1.difference(set2)
set1 - set2

# set2'de olup set1'de olmayanlar.
set2.difference(set1)
set2 - set1

#######################
# symmetric_difference(): İki kümede de birbirlerine göre olmayanlar
#######################

set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

#######################
# intersection(): İki kümenin kesişimi
#######################

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])

set1.intersection(set2)
set2.intersection(set1)

set1 & set2

#######################
# union(): İki kümenin birleşimi
#######################

set1.union(set2)
set2.union(set1)


#######################
# isdisjoint(): İki kümenin kesişimi boş mu?
#######################

set1 = set([7, 8, 9])
set2 = set([5, 6, 7, 8, 9, 10])

set1.isdisjoint(set2)
set2.isdisjoint(set1)


#######################
# isdisjoint(): Bir küme diğer kümenin alt kümesi mi?
#######################

set1.issubset(set2)
set2.issubset(set1)

#######################
# issuperset(): Bir küme diğer kümeyi kapsıyor mu?
#######################

set2.issuperset(set1)
set1.issuperset(set2)

#################################################################################################################################################

#list,tuple,set ve dictionary veri yapıları aynı zamanda python collection veri yapılarıdır.

