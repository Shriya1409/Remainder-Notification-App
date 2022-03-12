import time
from plyer import notification
 
 
if __name__=="__main__":
 
        notification.notify(
            title = "Please Drink water!!",
            message=" The U.S. National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men About1.5 cups (2.7 liters) of fluids a day for women" ,
            app_icon="C:\\Users\\Ruby nadkarni\\Downloads\\Iconsmind-Outline-Glass-Water.ico", #C:\\Users\\Ruby nadkarni\\Desktop\\remainder application with notification\\Iconsmind-Outline-Glass-Water.ico",

            # displaying time
            timeout=10
)
        # waiting time
        time.sleep(7)

