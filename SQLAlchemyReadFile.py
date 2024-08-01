import sqlalchemy as sqa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

#Creating a base
Base = declarative_base()


#Create a base template for the database entries
class Person(Base):

    __tablename__ = "People"

    ssn = sqa.Column("ssn", sqa.Integer, primary_key=True)
    firstname = sqa.Column("firstname", sqa.String)
    lastname = sqa.Column("lastname", sqa.String)
    gender = sqa.Column("gender", sqa.CHAR)
    age = sqa.Column("age", sqa.Integer)

    #Information we're going to save into the Database
    def __init__(self, ssn, first, last, gender, age):
        self.ssn = int(ssn)
        self.firstname = first
        self.lastname = last
        self.gender = gender
        self.age = int(age)

    #How it will be displayed
    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age}) "

#Creating a database with SQLite named mydb.db
engine = sqa.create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)
#Binds info to engine


#Open the text.txt file and create entries for each line of information in the filem, split by spaces
with open("text.txt") as file1:
    for line in file1:
        #Splitting the info in the txt file and saving it onto different variables
        info = line.split()
        Socialsn = info[0]
        Name = info[1]
        LastName = info[2]
        Gender = info[3]
        Age = info[4]

        #Creating a person variable so we could store the info into the database
        person = Person(Socialsn, Name, LastName, Gender, Age)
        with Session(engine) as session:
            #Actually commiting and saving the info to the database
            session.begin()
            session.add(person)
            session.commit()
            session.close()

