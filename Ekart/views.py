from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from Ekart.models import Mobile, Laptop, Camera

# Create your views here.
def signup(request):
	if request.method == "POST":
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		email = request.POST.get("email")
		try:
			user = User.objects.get(username=username)
			if user is not None:
				return HttpResponse("Please Check the Info, User might already exist.")
		except User.DoesNotExist:
			user = User.objects.create_user(username, email, password)
			#return HttpResponse(f" User {user} created successfully ")
			return render(request, "signin.html")			
	return render(request, "signup.html")
	
def signin(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, "home.html", {"user":user})
		else:
			return HttpResponse("Enter a valid username and password!")
	return render(request, "signin.html")

def logout(request):
    django_logout(request)
    return render(request, "signin.html")

def homePage(request):
	return render(request, "home.html")
	
def mobiles(request):
	mob_names = ['apple', 'google', 'samsung', 'oneplus', 'redmi', 'realme']
	
	i = 0
	while i < len(mob_names):
		items = get_mob_details(mob_names[i])
	
		Mobile.objects.get_or_create(product_image = items[0], product_name = items[1], product_small_description = items[2], product_big_description = items[3], product_price = items[4], company_name = mob_names[i])

		i = i+1
	
	mobiles = Mobile.objects.all()
	return render(request, "mobiles.html", {"products":mobiles})
	
def laptops(request):
	lap_names = ['dell', 'hp', 'lenovo', 'asus', 'apple_mac', 'vaio']
	
	i = 0
	while i < len(lap_names):
		items = get_laptop_details(lap_names[i])
		
		Laptop.objects.get_or_create(product_image = items[0], product_name = items[1], product_small_description = items[2], product_big_description = items[3], product_price = items[4], company_name = lap_names[i])

		i = i+1
	
	laptops = Laptop.objects.all()
	return render(request, "laptops.html", {"products":laptops})
	
def dslrs(request):
	cam_names = ['nikon', 'canon', 'sony', 'samsung', 'yashika', 'panasonic']
	
	i = 0
	while i < len(cam_names):
		items = get_dslr_details(cam_names[i])
		
		Camera.objects.get_or_create(product_image = items[0], product_name = items[1], product_small_description = items[2], product_big_description = items[3], product_price = items[4], company_name = cam_names[i])

		i = i+1
		
	camera = Camera.objects.all()
	return render(request, "dslrs.html", {"products":camera})
	
def get_mob_details(name):
	arr = []
	if name == 'apple':
		image_file = '/static/mobiles/iphone-se-2.jpg/'
		pname = 'iPhone-SE-2'
		psdesc = 'iPhone SE (2020) smartphone was launched on 15th April 2020. The phone comes with a 4.70-inch touchscreen display.'
		pbdesc = 'iPhone SE (2020) smartphone was launched on 15th April 2020. The phone comes with a 4.70-inch touchscreen display with a resolution of 750x1334 pixels at a pixel density of 326 pixels per inch. The iPhone SE (2020) supports wireless charging, as well as proprietary fast charging.'
		pprice = 20000
		arr = [image_file, pname, psdesc, pbdesc, pprice, name]
		
	elif name == 'google':
		image_file = '/static/mobiles/pixel-2.jpg/'
		pname = 'Pixel-2'
		psdesc = 'Google Pixel 2 smartphone comes with a 5-inch touchscreen display with a resolution of 1080 * 1920 pixels.'
		pbdesc = 'Google Pixel 2 smartphone comes with a 5-inch touchscreen display with a resolution of 1080 * 1920 pixels. The phone is powered by 1.9GHz octa-core Qualcomm Snapdragon 835 processor clubbed with 4GB RAM.'
		pprice = 38000
		arr = [image_file, pname, psdesc, pbdesc, pprice, name]
		
	elif name == 'samsung':
		image_file = '/static/mobiles/samsung-s10.jpg/'
		pname = 'Samsung-10'
		psdesc = 'The phone is powered by Octa core Cortex A55 processor and in-built storage capacity of USB 3.0 128GB.'
		pbdesc = 'The phone is powered by Octa core (2.73 GHz, Dual core, M4 Mongoose + 2.31 GHz, Dual core, Cortex A75 + 1.95 GHz, Quad core, Cortex A55) processor. It runs on the Samsung Exynos 9 Octa 9820 Chipset. It has 8 GB RAM and 128 GB internal storage. Samsung Galaxy S10 smartphone has a Dynamic AMOLED display.'
		pprice = 42000
		arr = [image_file, pname, psdesc, pbdesc, pprice, name]
		
	elif name == 'oneplus':
		image_file = '/static/mobiles/oneplus-7t.jpg/'
		pname = 'Oneplus-7T'
		psdesc = 'OnePlus 7T camera features Dual-LED flash, HDR, and panorama powered by an octa core 855 SoC.'
		pbdesc = 'OnePlus 7T camera features Dual-LED flash, HDR, and panorama. The new OnePlus phone is powered by an octa core Qualcomm Snapdragon 855 Plus SoC. Coupled with 8 GB of storage, the phone can handle most tasks with ease. Connectivity options included in the device are Bluetooth, USB, Wi-Fi, 3G and 4G.'
		pprice = 35000
		arr = [image_file, pname, psdesc, pbdesc, pprice, name]
		
	elif name == 'redmi':
		image_file = '/static/mobiles/5-pro.jpg/'
		pname = 'Note-5-Pro'
		psdesc = 'The device sports a 5.99-inch IPS LCD full HD+ display, which exhibits an excellent pixel density'
		pbdesc = 'The device sports a 5.99-inch IPS LCD full HD+ display, which exhibits an excellent pixel density of 403 PPI. It has the Corning Gorilla Glass that will protect it from minor scratches. The Xiaomi Redmi Note 5 Pro has a 4,000mAh Li-Polymer battery, which supports quick charging..'
		pprice = 15000
		arr = [image_file, pname, psdesc, pbdesc, pprice, name]
		
	elif name == 'realme':
		image_file = '/static/mobiles/2-pro.jpg/'
		pname = 'Realme-2-Pro'
		psdesc = 'The Realme 2 Pro functions on a two Cortex A53 quad-core processors (1.95GHz + 1.8GHz)'
		pbdesc = 'The Realme 2 Pro functions on a two Cortex A53 quad-core processors (1.95GHz + 1.8GHz) seated upon a Qualcomm Snapdragon 660 MSM8956 chipset which is promising in terms of performance. An Adreno 512 GPU handles the graphics and a 4GB RAM keeps it lag-free while heavy gaming and multitasking..'
		pprice = 12000
		arr = [image_file, pname, psdesc, pbdesc, pprice, name]
		
	else:
		return HttpResponse(f" Invalid Item Name ")
		
	return arr

def get_laptop_details(name):
	arr = []
	if name == 'dell':
		image_file = '/static/laptops/dell.jpg/'
		pname = 'Dell Inspiron 2664'
		psdesc = 'Dell as a range of affordable laptop computers, desktop computers and all-in-one computers'
		pbdesc = 'The Inspiron (/ˈɪnspɪrɒn/ IN-spirr-on, stylized as inspiron) is a computer product line created, designed, developed, marketed, produced and sold by Dell as a range of affordable laptop computers, desktop computers and all-in-one computers..'
		pprice = 52000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'hp':
		image_file = '/static/laptops/hp.jpg/'
		pname = 'HP Pavillion'
		psdesc = 'HP Pavilion 15 is a Windows 10 laptop with a 15.60-inch display that has a resolution of 1366x768 pixels.'
		pbdesc = 'HP Pavilion 15 is a Windows 10 laptop with a 15.60-inch display that has a resolution of 1366x768 pixels. It is powered by a Core i7 processor and it comes with 8GB of RAM. The HP Pavilion 15 packs 1TB of HDD storage. Graphics are powered by Nvidia GeForce 940MX.'
		pprice = 48000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'lenovo':
		image_file = '/static/laptops/lenovo.jpg/'
		pname = 'Lenovo Yoga'
		psdesc = 'The Lenovo IdeaPad Yoga is a line of convertible tablet computers that run the Windows operating system (OS).'
		pbdesc = 'The Lenovo IdeaPad Yoga is a line of convertible tablet computers that run the Windows operating system (OS). The Lenovo IdeaPad Yoga features a 360-degree hinged display that allows the device to be used as a traditional laptop or as a touchscreen tablet..'
		pprice = 42000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'asus':
		image_file = '/static/laptops/asus.jpg/'
		pname = 'Asus'
		psdesc = 'Designed for entertainment, the 15.6-inch ASUS X540 is powered by an Intel Core processor.'
		pbdesc = 'Designed for daily productivity and entertainment, the 15.6-inch ASUS X540 is powered by an Intel Core processor, and features NVIDIA graphics and an ODD. The 14-inch ASUS X441 is powered by an Intel Core processor with 16GB RAM, and features NVIDIA graphics and ASUS SonicMaster technology..'
		pprice = 35000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'apple_mac':
		image_file = '/static/laptops/mac_book.jpg/'
		pname = 'Macbook Air Pro'
		psdesc = 'The MacBook Air is a line of laptop computers developed and manufactured by Apple Inc.'
		pbdesc = 'The MacBook Air is a line of laptop computers developed and manufactured by Apple Inc. It consists of a full-size keyboard, a machined aluminum case, and a thin light structure. The Air was originally positioned as a premium ultraportable positioned above the previous MacBook line.'
		pprice = 78000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'vaio':
		image_file = '/static/laptops/vaio.jpg/'
		pname = 'Vaio'
		psdesc = 'Sony VAIO Fit 15 SVF15318 laptop runs on Windows 8 and has Intel Core i5 (4th generation)'
		pbdesc = 'Sony VAIO Fit 15 SVF15318 Brief Description. Sony VAIO Fit 15 SVF15318 laptop runs on Windows 8 (64 bit) OS and has Intel Core i5 (4th generation) 1.6 GHz with Intel Turbo boost up to 2.6Ghz processor. It has Intel HD Graphics 4000 / Nvidia GeForce GT 740M 1GB DDR3 graphics processor. with 1366 x 768 pixels resolution.'
		pprice = 41000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	else:
		return HttpResponse(f" Invalid Item Name ")
		
	return arr

def get_dslr_details(name):
	arr = []
	if name == 'nikon':
		image_file = '/static/dslrs/nikon.jpg/'
		pname = 'Nikon D5200'
		psdesc = 'With the Nikon D5200 you can also engage in continuous shooting with a 5 FPS framerate.' 
		pbdesc = 'With the Nikon D5200 you can also engage in continuous shooting with a 5 FPS framerate.  This allows you to take actions shots in sequence without having to miss a single moment.'
		pprice = 33000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'canon':
		image_file = '/static/dslrs/canon.jpg/'
		pname = 'Canon EOS 70D'
		psdesc = 'The Canon EOS 70D is a digital single-lens reflex camera by Canon publicly announced on July 2.'
		pbdesc = 'The Canon EOS 70D is a digital single-lens reflex camera by Canon publicly announced on July 2, 2013 with a suggested retail price of $1,199. The EOS 70D is the launch platform for Canons Dual Pixel CMOS Autofocus, which provides great improvement in focusing speed while in Live View, both for stills and video.'
		pprice = 42000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'sony':
		image_file = '/static/dslrs/sony.jpg/'
		pname = 'Sony Alpha 2'
		psdesc = 'Sony Alpha a7 II Review. The Sony Alpha a7 II is an image-stabilized full frame mirrorless camera.'
		pbdesc = 'Sony Alpha a7 II Review. The Sony Alpha a7 II is an image-stabilized full frame mirrorless camera, the fourth release in Sonys a7 lineup and the follow up the original a7. It uses the same 24-megapixel sensor as its predecessor, and the same Bionz X processor as the rest of the a7 series.'
		pprice = 58000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'samsung':
		image_file = '/static/dslrs/samsung_d.jpg/'
		pname = 'Samsung NX30'
		psdesc = 'The Samsung NX30 is a midrange mirrorless camera that features a 20.3MP CMOS sensor.'
		pbdesc = 'The Samsung NX30 is a midrange mirrorless camera that features a 20.3MP CMOS sensor and the companys latest DRIMeIV processor. It supports the same NX-mount lenses as its predecessor (the NX20).'
		pprice = 61000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'yashika':
		image_file = '/static/dslrs/yashika.jpg/'
		pname = 'Yashika Dx Master'
		psdesc = 'Yashika was a Japanese manufacturer of cameras, originally active from 1949.'
		pbdesc = 'Yashika was a Japanese manufacturer of cameras, originally active from 1949 until 2005 when its then-owner, Kyocera, ceased production.'
		pprice = 44000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	elif name == 'panasonic':
		image_file = '/static/dslrs/panasonic.jpg/'
		pname = 'Vaio'
		psdesc = 'Its slender body features a high-res electronic viewfinder built into the back.'
		pbdesc = 'Its slender body features a high-res electronic viewfinder built into the back rather than having a chunkier DSLR-style design. Good for shooting from any angle, the viewfinder and rear screen both have a tilt facility.'
		pprice = 41000
		arr = [image_file, pname, psdesc, pbdesc, pprice]
		
	else:
		return HttpResponse(f" Invalid Item Name ")
		
	return arr
	
def productDesc_cart_checkout_ack_page(request, name, no, itype):
	global items
	if itype == 'mobile':
		items = get_mob_details(name)
	elif itype == 'laptop':
		items = get_laptop_details(name)
	elif itype == 'dslr':
		items = get_dslr_details(name)
	elif itype == 'na':
		print("NA")
		print(name)
		if (name == 'apple' or name == 'google' or name == 'samsung' or name == 'oneplus' or name == 'redmi' or name =='realme'):
			items = get_mob_details(name)
			print('Inside Mobile')
		elif (name == 'dell' or name == 'hp' or name == 'lenovo' or name == 'asus' or name == 'apple_mac' or name == 'vaio'):
			items = get_laptop_details(name)
		else:
			items = get_dslr_details(name)
			
	else:
		print(itype)
	
	image_file = items[0]
	pname = items[1]
	psdesc = items[2]
	pbdesc = items[3]
	pprice = items[4]

	username = None
	if request.user.is_authenticated:
		username = request.user.username
	user = User.objects.get(username=username)
	
	if no == 1:
		return render(request, "cart_page.html", {"image":image_file, "prod_name":pname, "prod_price":pprice, "name":name})
	elif no == 2:
		return render(request, "checkout_page.html", {"image":image_file, "prod_name":pname, "prod_price":pprice, "name":name, "user":user})
	elif no == 3:
		return render(request, "ack_page.html", {"prod_name":pname, "prod_price":pprice, "user":user})
	
	return render(request, "products_desc.html", {"image":image_file, "prod_name":pname, "prod_desc":pbdesc, "prod_price":pprice, "name":name})