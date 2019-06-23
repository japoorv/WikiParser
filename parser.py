import xml.sax
import wiki_parser as wparser
import time
pid='';
page_text='';
revision=0;
contributor=0;
temp_pid='';
progrss=0;
tag=0;
ns='';

def conv(a):
	b='';
	for i in range(0,len(a)):
		if (a[i].isdigit()):
			b+=a[i];
	return str(b);
class MyHandler(xml.sax.handler.ContentHandler):
	def __init__(self):
		xml.sax.ContentHandler.__init__(self);
		self.tagname=''

	def startElement(self,name,attr):
		global pid;
		global revision;
		global tag;
		global contributor;
		self.tagname=name;
		if (name=='revision'):
			revision=1;
		elif (name=='contributor'):
			contributor=1;
		elif (name=='id' and revision==0 and contributor==0):
			pid='';
		elif (name=='id' and revision==1 and contributor==0):
			pid+='_'
		if (name=='text' or tag!=0):
			tag+=1;
		
		
	def endElement(self,name):
		global progrss;
		global page_text;
		global pid;
		global revision;
		global tag;
		global contributor;
		global ns;
		global temp_pid;
		if (name=='text'):
			if(ns==0):
				wparser.parse_text(page_text,pid); #Parses the given text
			page_text='';
			contributor=0;
			revision=0;
			progrss+=1;

		

		elif(name=='id' and contributor==0):
			pid+=str(int(temp_pid));
			temp_pid='';

		elif (name=='ns'):
			ns=int(ns)
		if (tag>0):
			tag-=1;


	def characters(self,content):
		global page_text;
		global pid;
		global temp_pid;
		global ns;
		if (self.tagname=='id' and contributor==0):
			temp_pid+=content;
		elif (self.tagname=='text' or tag==1):
			page_text+=content;
		elif (self.tagname=='ns'):
			bb=conv(content);
			if (bb!=''):
				ns=bb;

			
	
			

def main():
	global page_text
	tic=time.time();
	parser=xml.sax.make_parser()
	handler=MyHandler()
	parser.setContentHandler(handler)
	parser.parse('b.xml');
	toc=time.time();
	print(toc-tic + ' seconds elapsed');
if __name__=='__main__' :
	main();
