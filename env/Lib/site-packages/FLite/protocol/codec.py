import pickle

"""
这段代码使用Python内置的pickle模块，实现了两个函数marshal和unmarshal。marshal函数将传入的原始数据(raw_data)序列化为二进制格式的字符串，而unmarshal函数则将传入的二进制字符串(data)反序列化为原始数据。
具体而言，pickle.dumps()函数将原始数据(raw_data)转化为二进制格式的字符串，pickle.loads()函数将二进制字符串(data)反序列化为原始数据。这种序列化和反序列化的过程可以用于将Python数据结构存储到文件中或通过网络传输。
"""


def marshal(raw_data):
    return pickle.dumps(raw_data)


def unmarshal(data):
    return pickle.loads(data)
