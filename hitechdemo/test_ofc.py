# def required_admin(demo_func):
#     def check_admin(*args,**kwargs):
#         check_result=permission_check(*args)
#         if check_result in 'admin':
#             print(*args)
#             return demo_func(*args,**kwargs)
#         else:
#             raise Exception("Not allowed")
#     return check_admin
#
# def permission_check(username):
#     list_admin=['Deep Kandpal','Anil']
#     if username in list_admin:
#         return "admin"
#     else:
#         return "Not Admin"
#
#
# @required_admin
# def delete_user(user_name):
#     print("I am deleting")
#     return "I am Admin"
#
# print(delete_user("Kandpal"))

class Car(object):
    def __init__(self,brand=None):
        print("{0} brand producing large  range of cars.".format(brand))


class Brand(Car):
    def __init__(self,name=None):
        print("{0} cars are best in market.".format(name))
        super().__init__(name)

br=Brand('Honda')
