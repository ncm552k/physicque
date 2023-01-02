
food_dict = {
    # ten, khoi luong, don vi, min, max, calo, protein, carb, fat
    1:['Lòng trắng trứng', 50,'g', 2, 10, 26, 5.5, 0, 0],
    2:['Thăn bò', 50,'g', 2, 10, 65, 12, 0, 2.6],
    3:['Ức gà', 50,'g', 2, 10, 82, 15.5, 0, 1.8],
    4:['Thăn lợn', 50,'g', 2, 10, 71.5, 13, 0, 1.75],
    5:['Trứng cả quả', 50,'g', 2, 10, 83, 7.4, 0, 5.8],
    
    6:['Cá hồi', 50,'g', 2, 10, 103, 10, 0, 6],
    7:['Cá thu', 50,'g', 2, 10, 94.5, 9.5, 0, 6],
    8:['Cá ngừ', 50,'g', 2, 10, 64.5, 14.5, 0, 0.3],
    9:['Tôm', 50,'g', 2, 10, 49.5, 12, 0.1, 0.15],
    10:['Bơ lạc', 10,'g', 1, 10, 58.8, 12.5, 10, 25],
    
    11:['Whey Protein', 1,'muỗng', 1, 4, 110, 25, 2, 0.5],
    12:['Phô mai', 10,'g', 2, 10, 40.2, 2.5, 0.13, 3.3],
    13:['Sữa chua Hy Lạp', 100,'g', 1, 5, 97, 9, 3, 5],
    14:['Đậu phụ', 100,'g', 1, 5, 76, 8, 2, 4.8],
    15:['Sữa chua không đường', 100,'g', 1, 5, 61, 3.7, 4.8, 3.0],
    
    16:['Sữa chua có đường', 100,'g', 1, 5, 103, 3.5, 15.4, 3.0],
    17:['Sữa chua tách béo', 100,'g', 1, 5, 35, 3.5, 5.1, 0.1],
    18:['Khoai lang', 50,'g', 2, 10, 44.5, 0.8, 10, 0.1],
    19:['Cà rốt', 50,'g', 2, 10, 20.5, 0.45, 5, 0.1],
    20:['Chuối', 50,'g', 2, 10, 44, 0.55, 11.5, 0.15],

    21:['Dưa hấu', 50,'g', 4, 10, 15, 0.3, 4, 0.1],
    22:['Táo', 50,'g', 4, 10, 26, 0.15, 7, 0.1],
    23:['Việt quất', 50,'g', 1, 6, 28.5, 0.35, 7, 0.15],
    24:['Ổi', 50,'g', 4, 10, 34, 1.3, 7, 0.5],
    25:['Quả bơ', 50,'g', 1, 6, 80, 1, 1.15, 4.7],

    26:['Khoai tây', 50,'g', 2, 16, 38, 1, 8.5, 0],
    27:['Cà chua', 50,'g', 2, 6, 8.5, 0.45, 2, 0.1],
    28:['Ớt chuông', 50,'g', 2, 6, 10, 0.45, 2.3, 0.1],
    29:['Dâu tây', 50,'g', 1, 6, 6, 0.35, 4, 0.15],
    30:['Cải bắp', 50,'g', 4, 16, 12, 0.65, 2.55, 0],

    31:['Cải chíp', 50,'g', 4, 16, 13, 1, 0.5, 0],
    32:['Cải xoăn', 50,'g', 4, 16, 29.5, 2.5, 2.5, 0.5],
    33:['Măng tây', 50,'g', 4, 16, 10, 1.1, 1.85, 0],
    34:['Rau muống', 50,'g', 4, 16, 9, 1.3, 1.65, 0.1],
    35:['Rau dền', 50,'g', 4, 16, 11.5, 1.25, 2, 0.15],

    36:['Rau ngót', 50,'g', 4, 16, 2.65, 2.65, 11, 4],
    37:['Rau mùng tơi', 50,'g', 4, 16, 11, 1.5, 1.35, 0.4],
    38:['Đậu cô ve', 50,'g', 2, 10, 36.5, 2.5, 5.5, 0],
    39:['Củ cải', 50,'g', 4, 16, 7.5, 0.35, 1.7, 0],
    40:['Bí xanh', 50,'g', 4, 16, 8, 0.6, 1.55, 0.15],

    41:['Bí đỏ', 50,'g', 4, 16, 13, 0.5, 3.5, 0],
    42:['Đậu hà lan', 50,'g', 2, 10, 40.5, 2.6, 7.15, 0.15],
    43:['Đậu lăng', 50,'g', 2, 10, 58, 4.5, 10, 0.2],
    44:['Dứa', 50,'g', 4, 10, 25, 0.25, 6.5, 0],
    45:['Yến mạch', 50,'g', 1, 6, 194.5, 8.5, 33.15, 3.45],

    46:['Hạt diêm mạch', 50,'g', 2, 10, 60, 2.2, 10.65, 0.95],
    47:['Cơm gạo lứt', 50,'g', 2, 10, 41, 0.92, 8.5, 0.325],
    48:['Cơm trắng', 50,'g', 2, 10, 65, 1.35, 14.2, 0.15],
    49:['Xôi trắng', 50,'g', 2, 10, 48.5, 1, 10.5, 0.1],
    50:['Mỳ ý', 50,'g', 2, 10, 87, 3.75, 18.5, 0.4],

    51:['Bánh mì gối trắng', 50,'g', 2, 10, 133, 3.8, 25.3, 1.65],
    52:['Bánh mì gối đen', 50,'g', 2, 10, 137.5, 4.05, 25.6, 2.05],
    53:['Sữa tươi không đường', 50,'ml', 2, 10, 32.5, 1.6, 2.2, 1.9],
    54:['Sữa tươi có đường', 50,'ml', 2, 10, 36, 1.45, 4.0, 1.6],
    55:['Sữa đậu nành', 50,'ml', 2, 12, 27, 1.65, 3, 0.9],

    56:['Hạnh nhân', 10,'g', 1, 5, 57.5, 2.1, 2.2, 4.9],
    57:['Hạt điều', 10,'g', 1, 5, 55.3, 1.8, 3, 4.4],
    58:['Socola đen', 10,'g', 1, 5, 54.5, 0.5, 6.1, 3.1],
    59:['Ngũ cốc', 50,'g', 1, 8, 132, 6.5, 22.5, 2.1],
    60:['Nho', 50,'g', 2, 10, 57, 0.55, 13.65, 0.2],

    61: ['Gạo nếp', 100, 'g', 1, 3, 346, 8.4, 65.9, 1.6],
    62: ['Mì ý', 100, 'g', 1, 4, 131, 5, 25, 2],
    63: ['Pate', 10, 'g', 2, 10, 326, 1.08, 2.46, 1.54],
    64: ['Sườn bò', 50, 'g', 2, 10, 155, 11, 0, 21],
    65: ['Dầu ôliu', 1, 'g', 1, 10, 8.84, 0, 0, 1],
    
    66: ['Bánh mì nguyên cám', 50, 'g', 2, 10, 123.5, 6.5, 20.5, 1.7],
    67: ['Bò băm(80:20)', 50, 'g', 2, 10, 127, 8.5, 0, 10],
    68: ['Thịt heo(mông)', 50, 'g', 2, 10, 94, 9, 0, 6.5],
    69: ['Bột cacao', 10, 'g', 2, 10, 120, 10, 10, 5],
    70:['Đu đủ', 50, 'g', 2, 10, 21.5, 0.24, 5.41, 0.13],

    71: ['Ngô', 50, 'g', 2, 10, 209.5, 7.24, 33.15, 5.32],
    72: ['Bưởi', 50, 'g', 2, 10, 16.5, 0.35, 4.2, 0.05], 
    73: ['Đậu phộng', 10, 'g', 2, 10, 57, 2.51, 2.1, 4.8],
    74: ['Mật ong', 1, 'thìa canh', 1, 4, 45.6, 0.045, 12.36]
}


advices={
    1:"Abc",
    2:"xyz"
}


bulking = {
    "calo": 1.2,
    "macro": [0.35,0.45,0.2],
    "advices":[1,2],
    "meals":{
        1: [[18, 20, 3], [55, 46, 70], [45, 20, 22, 55], [18, 5, 55], [71, 2, 38], [71, 5, 20]],
        2: [[72, 70], [52, 73, 20], [20, 45, 74], [41, 53, 74, 19], [20, 10, 55]],
        3: [[47, 4, 41], [50, 2, 28, 29], [47, 7, 40, 19], [47, 9, 38], [47, 4, 36], [50, 27, 2], [47, 4, 36, 70]],
        4: [[15, 23], [11, 22], [55, 56], [11, 23], [55, 23]],
        5: [[47, 6, 41], [18, 4, 20], [3, 71, 38], [47, 4, 41, 22], [45, 4], [46, 53, 72]]
    }
}

cutting1 = {
    "calo": 0.9,
    "macro": [0.5,0.3,0.2],
    "advices":[1,2],
    "meals":{
        1:[[5,45]],
        2:[[55,29]],
        3:[[3,34]],
        4:[[11,57,23]],
        5:[[8,41]],
    }
}


cutting2 = {
    "calo": 0.8,
    "macro": [0.55,0.2,0.25],
    "advices":[1,2],
    "meals":{
        1:[[1,2],[1,3,5],[1,2,5]],
        2:[[1,2,21],[1,4,10],[1,10,4]],
        3:[[1,2,3],[1,4,10],[1,10,4]],
        4:[[1,2,5],[1,3,4,10],[1,10,4]],
        5:[[1,2,8],[1,4,10],[1,10,4]],
    }
}

cutting3 = {
    "calo": [0.8,1.3],
    "macro": [[0.55,0.15,0.3],[0.3,0.6,0.1]],
    "advices":[1,2],
    "meals1":{
        1:[[5,46],[1,3,5],[1,2,5]],
        2:[[1,2,21],[1,4,10],[1,10,4]],
        3:[[1,2,3],[1,4,10],[1,10,4]],
        4:[[1,2,5],[1,3,4,10],[1,10,4]],
        5:[[1,2,8],[1,4,10],[1,10,4]],
    },
    "meals2":{
        1:[[1,2],[1,3,5],[1,2,5]],
        2:[[1,2,21],[1,4,10],[1,10,4]],
        3:[[1,2,3],[1,4,10],[1,10,4]],
        4:[[1,2,5],[1,3,4,10],[1,10,4]],
        5:[[1,2,8],[1,4,10],[1,10,4]],
    }
}

maintaince = {
    "calo": 1,
    "macro": [0.4,0.4,0.2],
    "advices":[1,2],
    "meals":{
        1: [[45, 17, 20], [66, 12, 16, 22], [59, 53, 5],[51, 63,53]],
        2: [[78, 16, 21], [1, 23, 11], [45, 15, 60],[59,22]],
        3: [[47,67, 33,24], [50, 4, 32,55], [48, 7, 34,21]],
        4: [[1, 13,], [59, 20, 12], [15, 29,],[18,11]],
        5: [[47, 9, 42,25], [50, 67, 39,53], [48, 3, 19,65],[47,8,40,44]],
    }
}

post_contest= {
    "calo": 1.1,
    "macro": [0.35,0.45,0.2],
    "advices":[1,2],
    "meals":{
        1: [[61, 63, 53], [62, 2, 15], [45, 20, 54]],
        2: [[10, 15], [57, 23], [12, 29]],
        3: [[47, 64, 24, 65], [66, 63, 33, 23], [47, 67, 35, 44]],
        4: [[57, 53], [58, 60], [56, 15]],
        5: [[47, 68, 28, 20], [47, 64, 65, 21], [47, 67, 34, 25]]
    }
}

meals_percent=[0.25,0.125,0.25,0.125,0.25]

meals_name = ['Bữa sáng', 'Bữa phụ 1','Bữa trưa','Bữa phụ 2','Bữa tối']