""" პროგრამული ამოცანა """
import pandas as pd
from random import randint, choice
import pymongo
import matplotlib.pyplot as plt
# 36 ქალაქი
city = ["აბასთუმანი", "ახალციხე", "ბაკურიანი", "ბოლნისი", "ბორჯომი", "გონიო", "გორი", "გუდაური", "გურჯაანი", "ზესტაფონი",
        "ზუგდიდი", "ოზურგეთი", "რუსთავი", "თიანეთი", "ლაგოდეხი", "ლანჩხუთი", "მანგლისი", "მარნეული", "თბილისი", "ონი",
        "თელავი", "საგარეჯო", "სამტრედია", "საჩხერე", "ფოთი", "ხობი", "სურამი", "ურეკი", "სენაკი", "უშგული", "ქობულეთი",
        "ქუთაისი", "ჩოხატაური","ჭიათურა", "ხარაგაული", "ხაშური"]
# 15 ღირშესანიშნავი ადგილი ან ქალაქი
places = ['ბათუმი', 'დაშბაშის კანიონი', 'დმანისი', 'ვარძია', 'თუშეთი', 'მარტვილის კანიონი', 'მცხეთა', 'ნუნისი',
          'ოკაცეს კანიონი', 'პრომეთეს მღვიმე', 'სათაფლია', 'სვანეთი', 'სიღნაღი', 'ყაზბეგი', 'ხიხანის ციხე' ]
# წელიწადის პერიოდი
Quarter = ['January-March', 'April-June', 'July-September', 'October-December']
# 10 წელი
year = [ye for ye in range(2010, 2020)]

columns = ["Year", "Quarter", "FromCity", "VisitedPlace", "NumberOfVisits"]
arr = [[choice(year), choice(Quarter), choice(city), choice(places), randint(5, 30)] for _ in range(5000)]

# კოდის ერთჯერადად ამუშავების შემდეგ 21 ხაზზე გამოყენებული კოდი დააკომენტარეთ
df = pd.DataFrame(arr, columns=columns).to_excel('data.xlsx')

"""
წინამდებარე ფაილში გენერირდება (სიმულაციური) მონაცემები საქართველოს სხვადასხვა ქალაქებიდან გარკვეულ წლებში განხორციელებულ 
ექსკურიებზე (ვიზიტებზე). სიმარტივისთვის აღებულია 36 ქალაქი, წლები 2010-2020, 15 ღირესანიშნავი ადგილი.

პროგრამაში გენერირდება 5000 ჩანაწერი. ყოველი მონაცემები დალაგებულია ფორმით:

  1. წელი (წლები მოცემულია შუალედში 2010 – 2019 -ის ჩათვლით)
  2. წლის პერიოდი ('January-March', 'April-June', 'July-September', 'October-December')
  3. ქალაქი, რომლიდანაც განხორციელდა ვიზიტი
  4. ღირშესანიშნავი ადგილი, სადაც განხორციელდა ვიზიტი
  5. მითითებულ პერიოდში განხორციელებული ვიზიტების რაოდენობა
  
  (მაგალითად, [2011, 'January-March', 'ონი', 'ბათუმი', 5])
"""
class Exam:

    """
    შექმენით კლასი შესაბამისი რაოდენობის ატრიბუტებითა (რომლებიც უნდა განსაზღვროთ თქვენი შეხედულებით) და მეთოდებით:
    """
    def __init__(self, year, quarter, city, place, visits):
        # """ 1. (0.5 ქულა) კლასის კონსტრუქტორი (მითითება: აუცილებლობის შემთხვევაში დაშვებულია კლასის ატრიბუტებად
        #        ნებისმიერი ტიპის (list, tuple, dict, ...) მნიშვნელობების გამოყენების შესაძლებლობა).
        #        ასევე შექმენით ერთი დამატებითი ველი, რომელშიც ჩაიწერება ვიზიტების ჯამური რაოდენობა ყველა წლისა და
        #        ღირშესანიშნავი ადგილის მიხედვით. """
        self.year = year
        self.quarter = quarter
        self.city = city
        self.place = place
        self.visits = visits
        self.total_visits = 0
           

    def union(self):
        # """ 2. (1.5 ქულა) დაწერეთ მეთოდი, რომელიც სამგანზომილებიანი ლექსიკონის მეშვეობით მოახდენს მონაცემების გაერთიანებას.
        #        პირველ განზომილებაზე გასაღების როლში გამოიყენეთ ქალაქი, რომლიდანაც ადგილი ჰქონდა ვიზიტს, მეორე განზომილებაზე
        #        გამოიყენეთ ღირშესანიშნავი ადგილი, სადაც იყო ვიზიტი, ხოლო მესამე განზომილებაზე კი - წელი, რომელშიც ადგილი
        #        ჰქონდა ვიზიტს. სამივე განზომილების მიმართ მნიშვნელობის როლში უნდა იყოს გამოყენებული წელიწადის სხვადასხვა
        #        პერიოდში განხორციელებული ვიზიტების ჯამური რაოდენობა. """
            data = {}
            for record in arr:
                year = record[0]
                city = record[2]
                place = record[3]
                visits = record[4]
                
                if city not in data:
                    data[city] = {}
                if place not in data[city]:
                    data[city][place] = {}
                if year not in data[city][place]:
                    data[city][place][year] = 0
                    
                data[city][place][year] += visits
            return(data)
        

    @staticmethod
    def makeRecord(objects_array):
        # """ 3. (0.5 ქულა) კლასის სტატიკური მეთოდი, რომელიც მოახდენს მიმდინარე კლასის ტიპის ობიექტების სიმრავლის ჩაწერას
        #     MongoDB მონაცემთა ბაზაში. """
            client = pymongo.MongoClient("mongodb://localhost:27017/")
            db = client["mydatabase"]
            collection = db["mycollection"]
            collection.insert_many(objects_array)
            print("Objects written to the database.")
      
    @staticmethod
    def createDiagram(records):
        # """ 4. (1.5 ქულა) კლასის სტატიკური მეთოდი, რომელიც მოახდენს იმ ქალაქების მონაცემების ვიზუალიზაციას ვიზიტების ჯამური
        #        რაოდენობის მიხედვით, რომლებიდანაც განხორციელდა ყველაზე მეტი ვიზიტი. """
        city_visits = {}
        for record in records:
            city = record[2]
            visits = record[4]
            if city in city_visits:
                city_visits[city] += visits
            else:
                city_visits[city] = visits
        
        cities = list(city_visits.keys())
        visits = list(city_visits.values())

        plt.bar(cities, visits)
        plt.xlabel("City")
        plt.ylabel("Total Visits")
        plt.show()

    def __ge__(self, other):
        # """ 5. (0.5 ქულა) კლასის ობიექტისთვის გადატვირთეთ ოპერატორი >= მთელს პერიოდში განხორციელებული ვიზიტების ჯამური
        #     რაოდენობის მიხედვით. """
         if isinstance(other, Exam):
            return self.total_visits >= other.total_visits
         else:
            return NotImplemented
       
       

    def output(self):
        # """ 6. (1 ქულა) მონაცემთა გამოტანის მეთოდი, რომელიც მიმდინარე ობიექტისთვის მონაცემებს გამოიტანს შემდეგი პრინციპით:
        #          [1] პირველ ხაზზე ქალაქი რომლიდანაც განხორციელდა ვიზიტი
        #          [2] შემდეგ ხაზებზე შეწევით: ღირშესანიშნავი ადგილი და ამ მიმართულებით განხორციელებული ვიზიტების ჯამური რაოდენობა
        #              მთელს პერიოდში
        #             (მაგალითად,
        #                 თბილისი:
        #                     თუშეთი - 100 (სადაც 100 არის 10 წლის განმავლობაში თბილისიდან თუშეთში განზორციელებული ვიზიტების ჯამური რაოდენობა)
        #                     სიღნაღი - 50 და ა.შ."""
        dictionary = {}
        for element in arr:
            if element[2] == self.city:
                if element[3] not in dictionary:
                    dictionary[element[3]] = element[4]
                else:
                    dictionary[element[3]] += element[4]
        
        print(f'{self.city}:\n')
        for key, value in dictionary.items():
            print(f' {key} - {value}\n')      


     


        
        

      

def main():
    
    # """ ფუნქცია პროგრამის მუშაობის შემოწმებისთვის """

    # """ (0.5 ქულა) pandas მოდულის გამოყენებით მოახდინეთ ფაილიდან მონაცემების კითხვა და ობიექტების შექმნა. """
    # """ (0.5 ქულა) მოახდინეთ ობიექტების გაერთიანება. """ 
    
        df = pd.read_excel("data.xlsx")
        obj_list = []
        for index, row in df.iterrows():
            obj = Exam(row["Year"], row["Quarter"], row["FromCity"], row["VisitedPlace"], row["NumberOfVisits"])
            obj_list.append(obj)

    # """ (0.5 ქულა) მოახდინეთ მიღებული ობიექტების სიმრავლის დალაგება კლებადობით ვიზიტების ჯამური რაოდენობის მიხედვით. """
        sorted_list = sorted(obj_list, key=lambda x: x.visits)
       

    # """ (0.5 ქულა) მოახდინეთ მიღებული ობიექტების სიმრავლის პირველივე მნიშვნელობის ბეჭდვა. """
        first_obj = obj_list[0]
        print(first_obj)

    # """ (0.5 ქულა) ობიექტების დალაგებული სიმრავლიდან მონაცემები გადაწერეთ MongoDB მონაცემთა ბაზაში. """s
        client = pymongo.MongoClient("mongodb://localhost:27017/")  
        db = client["object_array"]
        collection = db["object_array"]

        for obj in sorted_list:
             collection.insert_one(obj.__dict__)

    # """ (0.5 ქულა) MongoDB მონაცემთა ბაზიდან წაიკითხეთ პირველი 7 მონაცემი. წაკითხვისას უნდა ხდებოდეს ყოველი მონაცემისთვის
    #                მხოლოდ ორი ველის ((1) ქალაქის დასახელება; (2) ვიზიტების ჯამური რაოდენობა) მნიშვნელობის მიღება. """
       
        my_documents = collection.find({},{"city":1, "visits":1}).limit(7)

        for document in my_documents:
            print(document)


    # """ (0.5 ქულა) MongoDB მონაცემთა ბაზიდან წაკითხული მონაცემების გამოყენებით მოახდინეთ შესაბამისი დიაგრამის შედგენა. """
        x = []
        y = []

        for document in my_documents:
            x.append(document[1])
            y.append(document[2])

        plt.scatter(x, y)
        plt.xlabel("ქალაქი")
        plt.ylabel("ვიზიტი")
        plt.show()

        

    # """ (1.0 ქულა) ლოგიკურად გამართული დასრულებული კოდი: 
    #                ((1) ყველა მეთოდი უნდა იყოს ლოგიკურად სწორად იმპლემენტირებული;
    #                 (2) ყველა პუნქტი ლოგიკურად უნდა იყოს სწორად გაკეთებული)       """
    


if __name__ == '__main__':
    main()