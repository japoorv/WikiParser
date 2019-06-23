def remove_comment(a):
	i=0;
	b='';
	while (i<len(a)):
		if (a[i]=='<' and i+3<len(a) and a[i:i+4]=='<!--'):
			comment='';
			i=i+3;
			while(i<len(a)):
				i=i+1;
				comment+=a[i];
				if (len(comment)>=3 and comment[-3:]=='-->'):
					break;
					
		else :
			b+=a[i];
		i=i+1;	
	return b;			
def remove_infobox(a):
	i=0;
	b='';
	while(i<len(a)): 
		if (i+6<len(a) and (a[i:i+6]=='{{use ' or a[i:i+6]=='{{shor' or a[i:i+6]=='{{conv' or a[i:i+6]=='{{loca' or a[i:i+6]=='{{use ' or a[i:i+6]=='{{main' or a[i:i+6]=='{{#swi' or a[i:i+6]=='{{#exp' or a[i:i+6]=='{{col-' or a[i:i+6]=='{{full' or a[i:i+6]=='{{info' or a[i:i+6]=='{{subs' or a[i:i+6]=='{{rp-p' or a[i:i+6]=='{{quot' or a[i:i+6]=='{{abou' or  a[i:i+6]=='{{circ' or a[i:i+5]=='{{ipa' or a[i:i+5]=='{{not' or (a[i:i+5]=='{{ref') or  (a[i:i+5]=='{{sfn') or (a[i:i+5]=='{{efn') or (a[i:i+5]=='{{not'))):
			brack=0;
			while(i<len(a)):
				if (a[i]=='{'):
					brack+=1;
				elif(a[i]=='}'):
					brack-=1;
				i=i+1;
				if (brack==0):
					break;
		else:
			b+=a[i];
			i+=1;
	return b;

def prcss_templates(a):
	i=0;
	b='';
	while(i<len(a)):
		if (a[i]=='{' and i+1<len(a) and a[i+1]=='{'):
			templates='';
			i=i+1;
			indi=-1;
			while(i<len(a)):
				i=i+1;
				templates+=a[i];
				if (templates[-2:]=='}}'):
					break;
				elif(templates[len(templates)-1]=='|'):
					indi=len(templates);
			b+=templates[indi:-2];
		else:
			b+=a[i];
		i=i+1;
		
	return b;	

def remove_files(a):
	i=0;
	b='';
	while(i<len(a)): 
		if (i+5<len(a) and (a[i:i+6]=='[[file' or a[i:i+6]=='[[imag')):
			brack=0;
			while(i<len(a)):
				if (a[i]=='['):
					brack+=1;
				elif(a[i]==']'):
					brack-=1;
				i=i+1;
				if (brack==0):
					break;
		else:
			b+=a[i];
			i+=1;
	return b;	

def remove_tables(a):
	i=0;
	b='';
	while(i<len(a)): 
		if (i+1<len(a) and a[i:i+2]=='{|'):
			brack=0;
			while(i<len(a)):
				if (a[i]=='{'):
					brack+=1;
				elif(a[i]=='}'):
					brack-=1;
				i=i+1;
				if (brack==0):
					break;
		else:
			b+=a[i];
			i+=1;
	return b;

def prcss_ilinks(a):
	i=0;
	b='';
	while(i<len(a)):
		if (i+1<len(a) and a[i:i+2]=='[['):
			brack=0;
			txt='';
			while(i<len(a)):
				if (a[i]=='['):
					brack+=1;
				elif(a[i]==']'):
					brack-=1;
				else:
					txt+=a[i];
				i=i+1;
				if (brack==0):
					if (txt.find('|')!=-1):
						b+=txt[1+txt.find('|'):len(txt)]
					else :
						b+=txt;		
					break;
		else:
			b+=a[i];
			i+=1;
	return b;	

def prcss_olinks(a):
	i=0;
	b='';
	while(i<len(a)):
		if (i+4<len(a) and a[i:i+5]=='[http'):
			brack=0;
			txt='';
			while(i<len(a)):
				if (a[i]=='['):
					brack+=1;
				elif(a[i]==']'):
					brack-=1;
				else:
					txt+=a[i];
				i=i+1;
				if (brack==0):
					if (txt.find(' ')!=-1):
						b+=txt[1+txt.find(' '):len(txt)]
					else :
						b+=txt;		
					break;
		else:
			b+=a[i];
			i+=1;
	return b;	

def remove_rfrns1(a):
	i=0;
	b='';
	flag=0;
	while (i<len(a)):
		if (i+3<len(a) and (a[i:i+4]=='<ref')):
			brack=0;
			while(i<len(a)):
				if (a[i]=='<'):
					brack+=1;
				elif(a[i]=='>'):
					brack-=1;
				elif (a[i]=='/'):
					flag=1;
				i=i+1;
				if (a[i-1]=='>' and brack==0 and flag==1):
					flag=0;
					break;
		else:
			b+=a[i];
			i+=1;
	return b;	

def remove_rfrns(a):
	i=0;
	b='';
	flag=0;
	while (i<len(a)):
		if (i+3<len(a) and (a[i:i+4]=='<gal')):
			brack=0;
			while(i<len(a)):
				if (a[i]=='<'):
					brack+=1;
				elif(a[i]=='>'):
					brack-=1;
				elif (a[i]=='/'):
					flag=1;
				i=i+1;
				if (a[i-1]=='>' and brack==0 and flag==1):
					flag=0;
					break;
		else:
			b+=a[i];
			i+=1;
	return b;	

def remove_divs(a):
	i=0;
	b='';
	flag=0;
	while (i<len(a)):
		if (i+3<len(a) and (a[i:i+4]=='<div')):
			brack=0;
			while(i<len(a)):
				if (a[i]=='<'):
					brack+=1;
				elif(a[i]=='>'):
					brack-=1;
				elif (a[i]=='/'):
					flag=1;
				i=i+1;
				if (a[i-1]=='>' and brack==0 and flag==1):
					flag=0;
					break;
		else:
			b+=a[i];
			i+=1;
	return b;
	
def rmv_heading(a,headings):
	i=0;
	b='';
	while(i<len(a)):
		if (i+1<len(a) and a[i:i+2]=='=='):
			heading='';
			for j in range(i+2,len(a)):
				if (j+1<len(a) and a[j:j+2]=='=='):
					break;
				else :
					heading+=a[j];
			heading=heading.replace(' ','');
			if (heading in headings):
				i=j+2;
				while(i<len(a)):
					if (i+1<len(a) and a[i:i+2]=='=='):
						break;
					else :
						i+=1;
				heading='';
			else :
				b+=a[i];
				i+=1;
		else :
			b+=a[i];
			i+=1;
	return b;

def parse_text(a,pid):
	a=a.lower();
	a=rmv_heading(a,['seealso','notes','references','bibliography','externallinks']);
	a=remove_comment(a); 
	a=remove_infobox(a);
	a=remove_files(a);
	a=remove_tables(a);
	a=prcss_ilinks(a); # internal links
	a=prcss_olinks(a); # external links
	a=remove_rfrns(a); # removing references
	a=remove_rfrns1(a);
	a=remove_divs(a);
	a=prcss_templates(a);
	a=a.replace('</div>',' ')
	a=a.replace('&nbsp;',' ');
	file=open((pid)+'.txt','w');
	file.write(a);
	file.close()
