import random
'''
需要4级强化石1颗，已知可通过两种途径获得
①通过 NPC 购买1级强化石往上合成
②从其它玩家手中购买

方案①
1级强化石可通过 NPC 购买
1级强化石 x1 = 0.75金 + 8银
1银 = 0.05金
1体力 = 1金


合成条件
（若合成失败 消耗当次合成所包含的<辅助材料和金>，不消耗主材料和体力）
目标                主材料             辅助材料             额外消耗            成功率
2级强化石 x1         1级强化石 x1       1级强化石 x12        0.39金、10体力      1
3级强化石 x1         2级强化石 x1       1级强化石 x16        0.897金、10体力     0.5878 
4级强化石 x1         3级强化石 x1       3级强化石 x12        19.75金、10体力     1     

方案②
当前4级强化石的市场价为850金一颗

计算强化石合成成本 与 市场购买成本 哪个划算？
'''


def buy_l1_stone(num=1):
    """
    向 NPC 购买1级强化石
    返回购买 num 个1级强化石所消耗的金数
    
    Keyword Arguments:
        num {int} -- 需要购买的数量 (default: {1})
    
    Returns:
        {float} -- 消耗金数
    """
    if type(num) != int:
        raise TypeError('num must be an int number')
    if num <= 0:
        return 0

    silver = 0.05  # 银价格
    l1_stone_unit_price = 0.75 + silver * 8  # 1级强化石单价
    consume_gold = l1_stone_unit_price * num  # 消耗金数

    return consume_gold


def synthetic_l2(num=1):
    """
    合成2级强化石
    返回合成 num 个2级强化石所消耗的金数

    Keyword Arguments:
        num {int} -- 合成数量 (default: {1})

    Returns:
        {float} -- 消耗金数
    """

    if type(num) != int:
        raise TypeError('num must be an int number')
    if num <= 0:
        return 0

    main_material_price = buy_l1_stone(1)  # 主材料价格
    assist_material_price = buy_l1_stone(12)  # 辅助材料价格
    synthetic_price = 0.39  # 合成消耗价格
    vic_price = compute_vic_value(10)  # 体力消耗价格
    price = (main_material_price + assist_material_price + synthetic_price +
             vic_price)  # 2级强化石单价

    total_price = num * price  # 消耗金数

    return total_price


def synthetic_l3(num=1):
    """
    合成3级强化石
    返回合成 num 个3级强化石所消耗的金数

    Keyword Arguments:
        num {int} -- 合成数量 (default: {1})

    Returns:
        {float} -- 消耗金数
    """

    if type(num) != int:
        raise TypeError('num must be an int number')
    if num <= 0:
        return 0

    rate = 0.5878  # 成功率
    total_price = 0  # 消耗金数
    '''开始合成直到达到 num 个 3级强化石'''
    for i in range(num):
        '''生产材料'''
        main_material_price = synthetic_l2(1)  # 主材料价格
        vic_price = compute_vic_value(10)  # 体力消耗价格
        total_price += main_material_price + vic_price
        succeeded = False
        '''一直生产辅助材料、合成 直到成功'''
        while not succeeded:
            assist_material_price = buy_l1_stone(16)  # 辅助材料价格
            synthetic_price = 0.897  # 合成消耗价格
            total_price += assist_material_price + synthetic_price

            if rate > random.random():
                succeeded = True

    return total_price


def synthetic_l4(num):
    """
    合成4级强化石
    返回合成 num个4级强化石所消耗的金数

    Keyword Arguments:
        num {int} -- 合成数量 (default: {1})

    Returns:
        {float} -- 消耗金数
    """

    if type(num) != int:
        raise TypeError('num must be an int number')
    if num <= 0:
        return 0
    total_price = 0
    for i in range(num):
        main_material_price = synthetic_l3(1)  # 主材料价格
        assist_material_price = synthetic_l3(12)  # 辅助材料价格
        synthetic_price = 19.75  # 合成消耗价格
        vic_price = compute_vic_value(10)  # 体力消耗价格
        total_price += (main_material_price + assist_material_price +
                        synthetic_price + vic_price)

    return total_price


def compute_vic_value(num=1):
    """计算体力价值（金数）
    返回消耗 num 点体力的价值
    
    Keyword Arguments:
        num {int} -- 消耗的体力数 (default: {1})
    
    Returns:
        {float} -- 消耗的体力的价值
    """
    vic_value = 1  # 1点体力的价值
    return vic_value * num


print(synthetic_l4(10000))