from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
#import PyPDF2
import re
from .models import ReceiptData, Customer, Items
def nlp(text):
    # FUnction to detect payment method
    def isPaymentMethod(x):
        payment_types_card = ["Card", "mastercard", "visa"]
        payment_types_cheque = ["bank", "cheque"]
        if x.lower() in payment_types_cheque:
            return True
        return False


    # Function to detect alphanumeric content
    def hasAlphanumeric(x):
        alphanumerreg = r'(\b[A-Z0-9]{10}\b)'
        if re.match(alphanumerreg, x):
            try:
                found = re.search(alphanumerreg, x).group(0)
                return found
            except AttributeError:
                return ''


    # Function to detect Items
    def detectItems(x):
        itemregex1 = r'(\d+)\s*\n(\w+\s+)+\s*\n(\d+)\s*\n\$?(\d+\.\d{2})\s*\n\$?(\d+\.\d{2})\s*\n'
        itemregex2 = r'([A-Z][\w\s\(\)]+)\s+(\d+)\s+\$?(\d+\.\d{2})\s+\$?(\d+\.\d{2})'
        itemlist = []
        itemdetails = re.findall(itemregex2, x)
        print(itemdetails)
        for items in itemdetails:
            itemlist.append(list(items))
        return itemlist


    # Function to detect date regex
    def isInvoiceDate(x):
        dateregex1 = r'(\d\d-\w+-\d\d\d\d)'
        dateregex2 = r'(\d\d-\d\d-\d\d\d\d)'
        dateregex3 = r'(\d\d\/\d\d\/\d\d\d\d)'
        dateregex4 = r'(\d\d\s+\w+\s+\d\d\d\d)'
        dateregex5 = r'(\w+\s+\d\d,?\s+,?\d\d\d\d)'

        if re.match(dateregex1, x):
            try:
                found = re.search(dateregex1, x).group(0)
                return found
            except AttributeError:
                return ''
        if re.match(dateregex2, x):
            try:
                found = re.search(dateregex2, x).group(0)
                return found
            except AttributeError:
                return ''
        if re.match(dateregex3, x):
            try:
                found = re.search(dateregex3, x).group(0)
                return found
            except AttributeError:
                return ''
        if re.match(dateregex4, x):
            try:
                found = re.search(dateregex4, x).group(0)
                return found
            except AttributeError:
                return ''
        if re.match(dateregex5, x):
            try:
                found = re.search(dateregex5, x).group(0)
                return found
            except AttributeError:
                return ''
        return ''


    def hasAmountAtEnd(x):
        amountregex = r'\d+$'
        if re.match(amountregex, x):
            return True
        return False


    #filename = r'C:\Users\Suyash\Downloads\TestPDF\JPG\3.pdf'
    #pdfFileObj = open(filename, 'rb')
    #pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    #num_pages = pdfReader.numPages
    count = 0
    #text = ""

    # The while loop will read each page
    #while count < num_pages:
     #   pageObj = pdfReader.getPage(count)
      #  count += 1
       # text += pageObj.extractText()
    temp = ""

    for c in text:
        if c != ',':
            temp = temp + c
    text = temp
    #print(text)
    #print()
    #print()
    #print(repr(text))
    #print()
    usefuldata = {}
    usefuldata["Invoice Number"] = ""
    usefuldata["Total Bill"] = ""
    usefuldata["Customer ID"] = ""
    usefuldata["Date"] = ""
    usefuldata["Payment method"] = "Card"
    usefuldata["Items"] = []

    info = text.split("\n")
    lowertext = text.lower()
    lowerinfo = lowertext.split("\n")
    # for x in info:
    #	print(x)
    interest_words = [["invoice", "number", "no.", "No"], ["bill", "total", "amount"],
                      ["account", "number", "No.", "No", "customer"], ["invoice", "date"],
                      ["cheque", "card", "visa", "mastercard"]]
    interest_count = [0] * 5
    tokens = word_tokenize(text)
    lowertokens = word_tokenize(lowertext)
    # punctuations = ['(',')',';','[',']']
    # stop_words = stopwords.words('english')
    # keywords = [word for word in tokens if not word in stop_words]#and not word in punctuations]
    # lowerkeywords = [word for word in lowertokens if not word in stop_words]# and not word in punctuations]
    taggedlist = pos_tag(tokens)
    lowertaggedlist = pos_tag(lowertokens)
    lowerdicttagwords = dict(lowertaggedlist)
    dicttagwords = dict(taggedlist)

    table_header = ["amount", "method", "date"]
    usefuldatadetect = {}
    usefuldatadetect["Invoice Number"] = False
    usefuldatadetect["Total Bill"] = False
    usefuldatadetect["Customer ID"] = False
    usefuldatadetect["Date"] = False
    usefuldatadetect["Payment method"] = True
    # for x in dicttagwords:
    #	print(str(x)+"  "+str(dicttagwords[x]))
    # for x in lowerdicttagwords:
    #	print(str(x)+"  "+str(lowerdicttagwords[x]))
    '''
    for lineno in range(len(info)):
        line=info[lineno]
        if line[len(line)-1]==':':
            line=line+info[lineno+1]
            del info[lineno+1]
            continue
        wordsinline=line.split(" ")
        count=0
        for z in wordsinline:
            if dicttagwords[z]=="NN" or dicttagwords[z]=="NNP":
    '''

    for lineno in range(len(info)):
        line = info[lineno]
        tokensinline = word_tokenize(line)
        lowertokensinline = word_tokenize(line.lower())
        '''for x in tokensinline:
            print(x,end=" ")
        print()'''
        colpossible = [word for word in tokensinline if not word in table_header]
        lowercolpossible = [word for word in lowertokensinline if not word in table_header]
        tablecol = False
        if isInvoiceDate(line) and usefuldatadetect["Date"] == False:
            usefuldata["Date"] = x
        '''for y in range(len(colpossible)):
            if dicttagwords[colpossible[y]]=='NNP' and lowerdicttagwords[lowercolpossible [y]]=='NN':
                continue
            else:
                tablecol=False'''

        if tablecol == False:
            interest_count = [0] * 5
            for x in tokensinline:
                if x.lower() in interest_words[0]:
                    interest_count[0] = interest_count[0] + 1
                if x.lower() in interest_words[1]:
                    interest_count[1] = interest_count[1] + 1
                if x.lower() in interest_words[2]:
                    #print("For CustID: " + line)
                    interest_count[2] = interest_count[2] + 1
                if x.lower() in interest_words[3]:
                    interest_count[3] = interest_count[3] + 1
                if isPaymentMethod(x):
                    #print("payment detected :" + x)
                    usefuldata["Payment method"] = "cheque"

                if isInvoiceDate(x) != '':
                    usefuldata["Date"] = x

            if interest_count[1] > 0:
                if hasAmountAtEnd(tokensinline[len(tokensinline) - 1]):
                    usefuldata["Total Bill"] = tokensinline[len(tokensinline) - 1]
                else:
                    usefuldata["Total Bill"] = info[lineno + 1]
            elif interest_count[0] > 0:
                if interest_count[0] >= interest_count[2]:
                    if hasAmountAtEnd(tokensinline[len(tokensinline) - 1]):
                        usefuldata["Invoice Number"] = tokensinline[len(tokensinline) - 1]
                    else:
                        usefuldata["Invoice Number"] = info[lineno + 1]
            elif interest_count[2] > 0:
                if hasAlphanumeric(tokensinline[len(tokensinline) - 1]):
                    usefuldata["Customer ID"] = tokensinline[len(tokensinline) - 1]
                else:
                    usefuldata["Customer ID"] = info[lineno + 1]
   # print("Trial is : ")

    usefuldata["Items"] = detectItems(text)

   # print()
    #print()
    for m in usefuldata:
        print(str(m) + " " + str(usefuldata[m]))

    print(usefuldata["Items"][0])
    c1=Customer()
    c1.customer_id=usefuldata["Customer ID"]
    c1.customer_name="Soumya"
    c1.customer_gender="Female"
    c1.customer_email="soumya.koppaka@spit.ac.in"
    c1.customer_address="Andheri"
    c1.customer_phone=123456
    c1.save()
    r1=ReceiptData()
    r1.customer_id=c1
    r1.invoice_no=usefuldata["Invoice Number"]
    r1.amount = usefuldata["Total Bill"]
    r1.date = usefuldata["Date"]
    r1.mode = usefuldata["Payment method"]
    r1.save()
    #i1=Items()
    objs = [Items() for i in range(len(usefuldata["Items"]))]
    for i in range(len(usefuldata["Items"])):
        #other_object.add(obj)
        #objs[i]=Items()
        objs[i].invoice_no=r1
        objs[i].item_name=usefuldata["Items"][i][0]
        objs[i].quant=usefuldata["Items"][i][1]
        objs[i].unit_price=usefuldata["Items"][i][2]
        objs[i].total=usefuldata["Items"][i][3]
        objs[i].save()