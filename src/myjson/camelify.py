import re

def camelify(obj):
    # 传入对象非字典列表元祖之一，直接返回
    if type(obj) != dict and type(obj) != list and type(obj) != tuple:
        return obj
    # 传入对象是字典
    if type(obj) == dict:
        convert_dict = {}

        for snake_case_key in obj:
            # 遍历字典，将每个 key camelCase 化
            camel_case_key = re.sub(r'_(\w)', lambda match: match.group(1).upper(), snake_case_key)

            value = obj[snake_case_key]
            # 对值进行递归处理
            convert_dict[camel_case_key] = camelify(value)

        return convert_dict

    else:
        convert_list = []

        for item in obj:
            # 遍历每个元素，进行递归处理
            convert_list.append(camelify(item))

        return convert_list


# test
if __name__ == '__main__':
    print(camelify(3))
    print(camelify(True))
    print(camelify('abc'))
    print(camelify(None))
    print(camelify({'my_name': 'Cphayim', 'favorite_lang': ['Python', 'JavaScript', 'Java', 'PHP']}))
