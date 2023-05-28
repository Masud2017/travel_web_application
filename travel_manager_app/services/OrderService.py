from auth_app.models import Orders

'''
<h1>OrderService</h1>
A class that maintains all the operations related to ordering product
'''

class OrderService:
    def __init__(self,current_user_obj):
        self.current_user_obj = current_user_obj
        self.price = 0

    def order_pre_made_package(self,package_obj_data):
        self.pacakge_data = package_obj_data
    
    '''
    Calculates the total price of all the packages (pre made / custom)
    @return price - value of total calculated price
    '''
    def calculate_price(self):
        for pacakge_item in self.pacakge_data:
            self.price = self.price + pacakge_item.price

        return self.price