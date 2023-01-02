from typing import List, Callable, Tuple
from info import Information, getTypeOfCutting, Gender, FatType, Phase
from utils import printYesNo, printChat
from genetic import Genome, run_evolution
import random
from constant import advices, food_dict, meals_name, bulking, cutting1, cutting2, cutting3, maintaince, post_contest


def printMeals( 
    gnome: Genome, \
    meals_foods: List[int], \
    food_per_meal: List[int], \
    day: int) -> None:
    tot_calo = sum(x*food_dict[y][5] for x,y in zip(gnome,meals_foods))
    tot_prot = sum(x*food_dict[y][6] for x,y in zip(gnome,meals_foods))
    tot_carb = sum(x*food_dict[y][7] for x,y in zip(gnome,meals_foods))
    tot_fat = sum(x*food_dict[y][8] for x,y in zip(gnome,meals_foods))

    count=0
    index=0
    output=f"Ngày {str(day)}"
    
    for x in food_per_meal:
        string=f"\n- {str(meals_name[count])}: "
        for _ in range(x):
            key_food=meals_foods[index]
            string += str(gnome[index] * food_dict[key_food][1]) + str(food_dict[key_food][2])+ " " + str(food_dict[key_food][0]) + ", "
            index+=1
        output+=string
        count+=1

    output += f"\n- Tổng: {tot_calo}kcal, {tot_prot}g protein, {tot_carb}g carb, {tot_fat}g fat"
    printChat(output)


# def random_meal_plan(phase: dict) -> tuple:
#     food_per_meal=[]
#     meals_foods=[]
#     for menus in phase['meals'].values():
#         random_menu = menus[random.randint(0,len(menus)-1)]
#         meals_foods+=random_menu
#         food_per_meal.append(len(random_menu))
#     return (food_per_meal, meals_foods)  


def random_meal_plan(meals: dict) -> tuple:
    food_per_meal=[]
    meals_foods=[]
    for option in meals.values():
        random_menu = option[random.randint(0,len(option)-1)]
        meals_foods += random_menu
        food_per_meal.append(len(random_menu))
    return (food_per_meal, meals_foods)   


def printAdvices(phase: dict, base_calo: float, isCutting3: bool = False) -> None:
    all_advices=''
    all_advices += '- Mức năng lượng cơ bản của cơ thể là '+ str(base_calo) + ' kcal'
    for x in phase['advices']:
        all_advices +='\n- ' + str(advices[x])
    if isCutting3:
        all_advices +='\n- Mức năng lượng thụ của 5 ngày đầu là '+ str(base_calo * phase['calo'][0]) + ' kcal'
        all_advices +='\n- Mức năng lượng thụ của 2 ngày cuối là '+ str(base_calo * phase['calo'][1]) + ' kcal'
    else:
        all_advices +='\n- Mức năng lượng thụ của giai đoạn này là '+ str(base_calo * phase['calo']) + ' kcal'
    printChat(all_advices)


def processMenu(info: Information) -> None:
    match info.phase.value:
        case Phase.BULKING.value:
            calo = info.base_calo*bulking["calo"]
            for day in range(1,8):
                food_per_meal, meals_foods = random_meal_plan(bulking["meals"])
                population, times = run_evolution(calo, bulking["macro"], meals_foods, food_per_meal )
                printMeals(population[0], meals_foods, food_per_meal, day)

        case Phase.CUTTING1.value:
            calo = info.base_calo*cutting1["calo"]
            for day in range(1,8):
                food_per_meal, meals_foods = random_meal_plan(cutting1["meals"])
                population, times = run_evolution(calo, cutting1["macro"], meals_foods, food_per_meal )
                printMeals(population[0], meals_foods, food_per_meal, day)

        case Phase.CUTTING2.value:
            calo = info.base_calo*cutting2["calo"]
            for day in range(1,8):
                food_per_meal, meals_foods = random_meal_plan(cutting2["meals"])
                population, times = run_evolution(calo, cutting2["macro"], meals_foods, food_per_meal )
                printMeals(population[0], meals_foods, food_per_meal, day)

        case Phase.CUTTING3.value:
            calo1 = info.base_calo*cutting3["calo"][0]
            for day in range(1,6):
                food_per_meal, meals_foods = random_meal_plan(cutting3["meals1"])
                population, times = run_evolution(calo1, cutting3["macro"][0], meals_foods, food_per_meal )
                printMeals(population[0], meals_foods, food_per_meal, day)

            calo2 = info.base_calo*cutting3["calo"][1]
            for day in range(6,8):
                food_per_meal, meals_foods = random_meal_plan(cutting3["meals2"])
                population, times = run_evolution(calo2, cutting3["macro"][1], meals_foods, food_per_meal )
                printMeals(population[0], meals_foods, food_per_meal, day)
            

        case Phase.MATAINANCE.value:
            calo = info.base_calo*maintaince["calo"]
            for day in range(1,8):
                food_per_meal, meals_foods = random_meal_plan(maintaince["meals"])
                population, times = run_evolution(calo, maintaince["macro"], meals_foods, food_per_meal )
                printMeals(population[0], meals_foods, food_per_meal, day)

        case Phase.POST_CONTEST.value:
            calo = info.base_calo*post_contest["calo"]
            for day in range(1,8):
                food_per_meal, meals_foods = random_meal_plan(post_contest["meals"])
                population, times = run_evolution(calo, post_contest["macro"], meals_foods, food_per_meal )
                printMeals(population[0], meals_foods, food_per_meal, day)






# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Program run here

flag = True

while flag:
    info = Information()
    info.setHeight()
    info.setWeight()
    info.setFat()
    
    if info.fat_type == FatType.FAT1:
        ans = printYesNo('Tỷ lệ mỡ trong người của bạn cao so với mức tiêu chuẩn. Có phải bạn muốn Cutting không?')
        if ans:
            type_cutting = getTypeOfCutting()
            info.setPhase(type_cutting)
        else:
            info.choosePhase()

    if info.fat_type == FatType.FAT2:
        info.setGender()

        if info.gender == Gender.MALE:
            ans = printYesNo('Tỷ lệ mỡ trong người của bạn cao so với mức tiêu chuẩn. Có phải bạn muốn Cutting không?')
            if ans:
                type_cutting = getTypeOfCutting()
                info.setPhase(type_cutting)
            else:
                info.choosePhase()
        else:
            ans = printYesNo('Tỷ lệ mỡ trong người của đang nằm ở mức duy trì. Có phải bạn muốn duy trì không?')
            if ans:
                info.setPhase(Phase.MATAINANCE)
            else:
                info.choosePhase()

    if info.fat_type == FatType.FAT3:
        ans = printYesNo('Tỷ lệ mỡ trong người của đang nằm ở mức duy trì. Có phải bạn muốn duy trì không?')
        if ans:
            info.setPhase(Phase.MATAINANCE)
        else:
            info.choosePhase()

    if info.fat_type == FatType.FAT4:
        info.choosePhase()
        info.setGender()
        info.setAge()

    info.setActivity()
    info.setBaseCalo()

    #tư vấn các thứ bla bla
    match info.phase.value:
        case Phase.BULKING.value:
            printAdvices(bulking, info.base_calo)

        case Phase.CUTTING1.value:
            printAdvices(cutting1, info.base_calo)

        case Phase.CUTTING2.value:
            printAdvices(cutting2, info.base_calo)

        case Phase.CUTTING3.value:
            printAdvices(cutting3, info.base_calo, True)
            
        case Phase.MATAINANCE.value:
            printAdvices(maintaince, info.base_calo)

        case Phase.POST_CONTEST.value:
             printAdvices(post_contest, info.base_calo)

    menu_option = printYesNo('Bạn có muốn xây dựng thực đơn mẫu không?')
    if menu_option:
        processMenu(info)
        
    flag = printYesNo('Bạn có muốn được tư vấn nữa không?')