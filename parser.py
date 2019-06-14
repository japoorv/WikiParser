import xml.sax
import wiki_parser as wparser
import time
pid='';
page_text='';
revision=0;
contributor=0;
temp_pid='';
progrss=0;
class MyHandler(xml.sax.handler.ContentHandler):
	def __init__(self):
		xml.sax.ContentHandler.__init__(self);
		self.tagname=''

	def startElement(self,name,attr):
		global pid;
		global revision;
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
		
	def endElement(self,name):
		global progrss;
		global page_text;
		global pid;
		global revision;
		global contributor;
		global temp_pid;
		if (name=='text'):
			wparser.parse_text(page_text,pid); #Parses the given text
			page_text='';
			contributor=0;
			revision=0;
			progrss+=1;
			print (progrss);

		elif(name=='id' and contributor==0):
			pid+=str(int(temp_pid));
			temp_pid='';


	def characters(self,content):
		global page_text;
		global pid;
		global temp_pid;
		if (self.tagname=='id' and contributor==0):
			temp_pid+=content;
		elif (self.tagname=='text'):
			page_text+=content;

def main():
	tic=time.time();
	parser=xml.sax.make_parser()
	handler=MyHandler()
	parser.setContentHandler(handler)
	parser.parse('b.xml');
	toc=time.time();
	print(toc-tic);
if __name__=='__main__' :
	main();