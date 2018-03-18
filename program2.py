#Makena Kong
#mkong02

#take a positive decimal integer and return the binary rep in a string
def dec_to_binary(num):
   result = ""
   if num <= 0:
      return result
   if num % 2 == 0:
      return  dec_to_binary(num//2) + "0"
   else:
      return dec_to_binary(num//2) + "1"
   return result
    

#takes a decimal and any base 2-16 and returns the rep in a string
def dec_to_base(num, base):
   result = ""
   if base < 2 or base > 16:
      return "no"
   if num <= 0:
      return result
   else:
      temp = num % base
      if temp < 10:
         return dec_to_base(num//base,base) + str(temp)
      else:
         return dec_to_base(num//base,base) + chr(temp+55)
   return result
        

#print(dec_to_binary(233))
#print(dec_to_base(233,8))
#print(dec_to_base(233,16))
#print(dec_to_base(233, 17))
