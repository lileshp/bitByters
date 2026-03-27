'''
Encapsulation:
    binding datamembers (attributes & Methods) into a single unit (class)
    Access Modifiers:
        Public : Accessible from anywhere
        Protected: class and child class
        Private: only in class

        public - Default
        protected - _datamember
        private - __datamember
'''

class CSE:
    def __init__(self,name):
        self.name = name #public
        self._scholar = 4587 #protected
        self.__fee = 50000 #private
    def __payment(self):
        print("PAYMENT")
    def student_fee(self):
        print(f"Hello {self.name} your fee is : {self.__fee}")
        self.__payment()
john = CSE("JOHN")
print(john.name)
print(john._scholar)
john.student_fee()
john._CSE__payment() #Name mangling

'''
How we can call a private datamember outside the call
    1. via public method
    2. Name mangling

'''
class Training:
    __company = "PwC"
    def __assignBatch(self):
        return "PYTHON BATCH"

    def studentBatch(self):
        ba = self.__assignBatch()
        print(f"Your batch is {ba} in {Training.__company}")
std = Training()
std.studentBatch()