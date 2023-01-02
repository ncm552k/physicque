from enum import Enum
from utils import setValue, printChat, printYesNo


class Gender(Enum):
    MALE = "Nam"
    FEMALE = 'Nữ'

class Phase(Enum):
    BULKING = 'Bulking'
    CUTTING1 = 'Cutting1'
    CUTTING2 = 'Cutting2'
    CUTTING3 = 'Cutting3'
    MATAINANCE = 'Duy trì'
    POST_CONTEST = 'Sau thi đấu'

class Activity(Enum):
    TYPE1 = 1.2
    TYPE2 = 1.375   
    TYPE3 = 1.55   
    TYPE4 = 1.725  
    TYPE5 = 1.9   

class FatType(Enum):
    FAT1 = 1
    FAT2 = 2
    FAT3 = 3
    FAT4 = 'skip'

def getTypeOfCutting() -> str:
    prep = printYesNo("Bạn có chuẩn bị cho thi đấu không?")

    if prep:
        weeks = None
        while(weeks==None):
            try:
                weeks = int(setValue("Khoảng bao lâu nữa bạn tham gia thi đấu? (Nhập số tuần)"))
                if weeks <= 0:
                    weeks=None
                    printChat("Chiều cao phải lớn hơn 0!")
            except ValueError:
                printChat("Nhập sai định dạng!")

        if weeks > 8:
            return Phase.CUTTING1
        elif weeks <=8 and weeks >=2:
            return Phase.CUTTING2
        else:    
            return Phase.CUTTING3
    else:
        return Phase.CUTTING1



class Information:
    def __init__(self):
        self.fat_percent = None
        self.height = None
        self.weight = None
        self.gender = None
        self.age = None
        self.base_calo = None
        self.phase = None
        self.activity=None
        self.fat_type = None

    def setHeight(self):
        while(self.height==None):
            try:
                self.height = float(setValue("Nhập chiều cao của bạn? (cm)"))
                if self.height <= 0:
                    self.height=None
                    printChat("Chiều cao phải lớn hơn 0!")
            except ValueError:
                printChat("Nhập sai định dạng!")     

    def setWeight(self):
        while(self.weight==None):
            try:
                self.weight = float(setValue("Nhập cân nặng của bạn? (kg)"))
                if self.weight <= 0:
                    self.weight=None
                    printChat("Cân nặng phải lớn hơn 0!")
            except ValueError:
                printChat("Nhập sai định dạng!")

    def setAge(self):
        while(self.age==None):
            try:
                self.age = int(setValue("Bạn bao nhiêu tuổi?"))
                if self.age <= 0:
                    self.age=None
                    printChat("Tuổi phải lớn hơn 0!")
            except ValueError:
                printChat("Nhập sai định dạng!")


    def setFat(self):
        while(self.fat_type==None):
            try:
                in_value = setValue("Tỷ lệ chất béo trong cơ thể của bạn là bao nhiêu? (Nhập 'skip' để bỏ qua)")

                if in_value.strip() == 'skip':
                    self.fat_type = FatType.FAT4
                    break

                in_value = float(in_value)

                if in_value <= 0:
                    printChat("Tỷ lệ mỡ phải lớn hơn 0!")
                    continue
                if(in_value < 15):
                    self.fat_type = FatType.FAT3
                    self.fat_percent = in_value
                    break
                if(in_value >= 15 and in_value<=25):
                    self.fat_type = FatType.FAT2
                    self.fat_percent = in_value
                    break
                if(in_value > 25):
                    self.fat_type = FatType.FAT1
                    self.fat_percent = in_value
                    break
            except ValueError:
                printChat("Nhập sai định dạng!")


    def setGender(self):
        while(self.gender==None):
            in_value = setValue("Giới tính của bạn là? (Lựa chọn)\
                                \n1. Nam \
                                \n2. Nữ")
            match in_value:
                case '1':
                    self.gender = Gender.MALE
                case '2':
                    self.gender = Gender.FEMALE
                case _:
                    printChat("Lựa chọn không có, vui lòng nhập lại!")    


    def setActivity(self):
        while(self.activity==None):
            in_value = setValue("Chọn cường độ luyện tập của bạn. (Lựa chọn)\
                                \n1. Ít hoạt động, chỉ ăn đi làm về ngủ \
                                \n2. Có tập nhẹ nhàng, tuần 1-3 buổi\
                                \n3. Có vận động vừa 4-5 buổi\
                                \n4. Vận động nhiều 6-7 buổi\
                                \n5. Vận động rất nhiều ngày tập 2 lần\
                                ")
            match in_value:
                case '1':
                    self.activity = Activity.TYPE1
                case '2':
                    self.activity = Activity.TYPE2
                case '3':
                    self.activity = Activity.TYPE3
                case '4':
                    self.activity = Activity.TYPE4
                case '5':
                    self.activity = Activity.TYPE5
                case _:
                    printChat("Lựa chọn không có, vui lòng nhập lại!") 

    def setBaseCalo(self):
        if self.fat_percent==None:
            if self.gender == Gender.MALE:
                self.base_calo = (10*self.height + 6.25*self.weight - 5*self.age + 5) * self.activity.value
            else:
                self.base_calo = (10*self.height + 6.25*self.weight - 5*self.age - 161) * self.activity.value
        else:
            self.base_calo = (370 + 21.6 * (1 - self.fat_percent / 100) * self.weight) * self.activity.value
    
        


    def setPhase(self, inputValue):
        self.phase = inputValue

    
    def choosePhase(self):
        while(self.phase==None):
            in_value = setValue("Chọn giai đoạn luyện tập của bạn. (Lựa chọn)\
                                \n1. Bulking \
                                \n2. Cutting\
                                \n3. Duy trì\
                                \n4. Sau thi đấu\
                                ")
            match in_value:
                case '1':
                    self.phase = Phase.BULKING
                case '2':
                    self.phase = getTypeOfCutting()
                case '3':
                    self.phase = Phase.MATAINANCE
                case '4':
                    self.phase = Phase.POST_CONTEST
                case _:
                    printChat("Lựa chọn không có, vui lòng nhập lại!") 

    def __str__(self) -> str:
        return str(self.fat_percent) + " " + \
                str(self.height) + " " + \
                str(self.weight) + " " + \
                str(self.gender) + " " + \
                str(self.age) + " " + \
                str(self.base_calo) + " " + \
                str(self.phase) + " " + \
                str(self.activity) + " " + \
                str(self.fat_type) 