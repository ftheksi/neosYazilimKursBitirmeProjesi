from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Category(models.Model):
    title=models.CharField(("Kategori"), max_length=50)
    slug=models.SlugField(("Slug Kategori"),blank=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Category,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Renk(models.Model):
    title=models.CharField(("Renkler"), max_length=50)
    slug=models.SlugField(("Slug Renk"),blank=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Renk,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Beden(models.Model):
    title=models.CharField(("Beden"), max_length=50)
    slug=models.SlugField(("Slug Beden"),blank=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Beden,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
class Beden2(models.Model):
    title=models.CharField(("Beden"), max_length=50)
    slug=models.SlugField(("Slug Beden"),blank=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Beden2,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class Urunler(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE) 
    category=models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
    image=models.ImageField(("Resim"), upload_to="urun",null=True)
    title=models.CharField(("Başlık"), max_length=50)
    text=models.TextField(("Açıklama"),max_length=600)
    puan=models.FloatField(("Puan"),default=0)
    slug=models.SlugField(("Slug Title"),blank=True,null=True)

    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Urunler,self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class UrunImg(models.Model):
    urun=models.ForeignKey(Urunler, verbose_name=("Ürün"), on_delete=models.CASCADE)
    resim=models.ImageField(("Resim"), upload_to="urun")

    def __str__(self):
        return self.urun.title

class BedenAyakkabi(models.Model):
    urun=models.ForeignKey(Urunler, verbose_name=("Ürün"), on_delete=models.CASCADE)
    renk=models.ForeignKey(Renk, verbose_name=("Renk"), on_delete=models.CASCADE)
    beden=models.ForeignKey(Beden, verbose_name=("Beden Numarası"), on_delete=models.CASCADE, null=True)
    fiyat=models.DecimalField(("Fiyat"), max_digits=50, decimal_places=2,default=0)
    stok=models.IntegerField(("Stok Miktarı"), default=0)

    def __str__(self):
        return self.urun.title


class BedenKiyafet(models.Model):
    urun=models.ForeignKey(Urunler, verbose_name=("Ürün"), on_delete=models.CASCADE)
    renk=models.ForeignKey(Renk, verbose_name=("Renk"), on_delete=models.CASCADE)
    fiyat=models.DecimalField(("Fiyat"), max_digits=50, decimal_places=2,default=0)
    stok=models.IntegerField(("Stok"), default=0)
    beden=models.ForeignKey(Beden2, verbose_name=("Beden"), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.urun.title + " || " + self.beden.title
    
class UrunStok(models.Model):
    urun=models.ForeignKey(Urunler, verbose_name=("Ürün"), on_delete=models.CASCADE)
    beden_ayakkabi=models.ManyToManyField(BedenAyakkabi, verbose_name=("Ayakkabı beden ve stok"),blank=True)
    beden_kiyafet=models.ManyToManyField(BedenKiyafet, verbose_name=("Kıyafet beden ve stok"),blank=True)
    

    def __str__(self):
        return self.urun.title
    
class Shopbasket(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    product_letter=models.ForeignKey(BedenKiyafet, verbose_name=("Ürün Giysi"), on_delete=models.CASCADE)
    price_all=models.DecimalField(("Fiyat"), max_digits=50, decimal_places=2,default=0)
    count=models.IntegerField(("Adet"),default=0)

    def __str__(self):
        return self.product_letter.urun.title
    
class Comment(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    product=models.ForeignKey(Urunler, verbose_name=("Ürün"), on_delete=models.CASCADE)
    text=models.TextField(("Yorum"),max_length=2000)
    date_now=models.DateTimeField(("Tarih-Saat"), auto_now_add=True)
    star=models.IntegerField(("Yorum Puanı"),default=5)




        









