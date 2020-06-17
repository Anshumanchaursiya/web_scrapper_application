from django.shortcuts import render
from django.http import HttpResponse

import requests
from bs4 import BeautifulSoup



def base(request):
	return render(request,'base.html')


def blog_list(request):
	if request.method == "POST":
		tag = request.POST['myvalue']

	tag_list = ['social-media','content-marketing','email-marketing','project-management','workflow','analytics','product','customer-marketing','thought-leadership']


	if tag in tag_list:
		res = requests.get('https://coschedule.com/topic/'+ tag + '/')
		soup = BeautifulSoup(res.text,'lxml')
	
		tot_title = soup.find_all('h2')
		tot_creator = soup.find_all('h5')
		#tot_response = soup.find_all( class_='blog-main-post')
		tot_response = soup.find_all('a',{'class':'blog-main-post'})
	
		tot_date = soup.find_all('span', {'itemprop':"datePublished"})
	
		list_title = []
		list_creator = []
		list_response = []
		list_data = []
	
		k = len(tot_response)
		print(k)

		if k<10:
			row = k
		else:
			row	= 10

		for i in range(row):
			list_title.append(tot_title[i].text)
	
		for i in range(row+1):
			list_creator.append(tot_creator[i].text)
	
		list_creator.pop(0)
	
		for i in range(row):
			list_response.append(tot_response[i].text)
	
		for i in range(row):
			list_data.append(tot_date[i].text)
	
	
		serial_num = ['blog->1','blog->2','blog->3','blog->4','blog->5','blog->6','blog->7','blog->8','blog->9','blog->10']
	
		list_detail = [list(a) for a in zip(list_title, list_creator,list_data)]
	else:
		list_detail = ['PLEASE INPUT THE CORRECT TAG']

	return render(request,'base.html',{'list_detail':list_detail})




