class Swift:
  def __init__(self,BCountry,BName,BCity,BBranch,BCode,BCountryCode="None",BCityCode="None",SwiftCode="None"):
    self.BCountry=BCountry
    self.BName=BName
    self.BCity=BCity
    self.BBranch=BBranch
    self.BCode=BCode
    self.BCountryCode=BCountryCode
    self.BCityCode=BCityCode
    self.SwiftCode=SwiftCode
  
  def findCityCode(self,dct1):
    for i in list(dct1.keys()):
      if self.BCity==i:
        self.BCityCode=dct1[i]
      else:
        self.BCityCode=="Not a valid city"
  def findCountryCode(self,dct2):
    for i in list(dct2.keys()):
      if self.BCountry==i:
        self.BCountryCode=dct2[i]
      else:
        self.BCountryCode=="Invalid Country"
  def findSwiftCode(self):
    self.SwiftCode=(self.BCountryCode+self.BName[0:3]+self.BCityCode+self.BCode)

if __name__=="__main__":
  a=[]
  n=int(input("Enter no. of Banks: "))
  for i in range(n):
    BCountry=input("Enter the country: ")
    BName=input("Enter the Name of Bank: ")
    BCity=input("Enter the city: ")
    BBranch=input("Enter the Branch: ")
    BCode=input("Enter the Branch code: ")
    obj=Swift(BCountry,BName,BCity,BBranch,BCode)
    a.append(obj)
  dct1={}
  for i in range(3):
    City=input("Enter the City: ")
    Code1=input("Enter the code: ")
    dct1[City]=Code1
  dct2={}
  for i in range(3):
    Country=input("Enter the country: ")
    Code2=input("Enter the code: ")
    dct2[Country]=Code2
  
  for j in a:
    j.findCityCode(dct1)
    j.findCountryCode(dct2)
    j.findSwiftCode()
    print(j.BName,j.BCity,j.BCityCode,j.BBranch,j.SwiftCode)
