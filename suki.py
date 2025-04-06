import datetime
now = datetime.datetime.now()
veggies=["brinjal","tomato","onion","carrot"]
quantity=[10,30,15,25]
S_P=[25,20,15,30]
C_P=[20,15,5,20]
cart=[]
cart_qty=[]
cart_per_kg=[]
total_cost_per_item=[]
user_name=[]
user_num=[]
user_bill=[]
users_items_bought=[]
user_items_bought_quantity=[]
user_eachitems_bought_cost_perkg=[]
user_eachitems_bought_cost_total=[]
sold_items=[]
sold_items_qty=[]
sold_items_cp=[]
sold_items_sp=[]
sold_items_profit=[]

revenue=0
'''cart=[]
cart_qty=[]
cart_per_kg=[]
total_cost_per_item=[]
total_bill=0
veggies=[]
quantity=[]
S_P=[]
C_P=[]'''
while True:
    print("1.Shopkeeper \n2.Customer \n3.Close the shop")
    view=int(input("Choose an option"))
    if view==1:
        while True:
            print("---Enter your Login Credentials----")
            Owner_id =int(input("Enter your login id:"))
            Owner_password=input("Enter Password:")
            if Owner_id ==5082005 and Owner_password=="Sukitha@2005":
                while True:
                    print("1.Add items to inventory\n2.Remove item\n3.Update item\n4.View Inventory\n5.View User Details\n6.View Today's Report\n7.Exit")
                    ch=int(input("choose an option:"))
                    if ch==1:
                        stock_add=input("What veggie do you want to add?")
                        if stock_add in veggies:
                            print(stock_add,"is already available in the stock Please use update option")
                        else:
                            veggies.append(stock_add)
                            quantity_of_stock_add=float(input("How much quantity to add?"))
                            quantity.append(quantity_of_stock_add)
                            c_p_of_veggie=float(input("Cost price of veggie you want to add?"))
                            C_P.append(c_p_of_veggie)
                            s_p_of_veggie=float(input("Selling price of veggie you want to add?"))
                            S_P.append(s_p_of_veggie)
                            print(stock_add,"is Successfully added to the stock")
                    elif ch==2:
                        item_remove=input("Enter the veggie you want to remove?")
                        if item_remove in veggies:
                            idx_remove=veggies.index(item_remove)
                            veggies.remove(item_remove)
                            del quantity[idx_remove]
                            del S_P[idx_remove]
                            del C_P[idx_remove]
                            print(item_remove,"is Successfully Removed from the Stock")
                        else:
                            print("Veggie is not available in the stock")
                    elif ch==3:
                        item_update=input("Enter the veggie you want to update?")
                        if item_update in veggies:
                            idx_item_update=veggies.index(item_update)
                            qty_update=float(input("How much quantity to update?"))
                            quantity[idx_item_update]=qty_update
                            c_p_update=float(input("Cost price of veggie you want to update?"))
                            C_P[idx_item_update]=c_p_update
                            s_p_update=float(input("Selling price of veggie you want to update?"))
                            S_P[idx_item_update]=s_p_update
                            print(item_update,"is succesfully updated to the stock")
                        else:
                            print(item_update,"is not available in the stock")
                    elif ch==4:
                        print('*'*10,"INVENTORY",'*'*10)
                        print("veggies",' '*10,"quantity",' '*5,"S_P ",' '*6,"C_P")
                        for i,j,k,l in zip(veggies,quantity,S_P,C_P):
                            print(i,' '*10,j,' '*10,k,' '*10,l)
                    elif ch==5:
                        if user_name==[]:
                            print("No Customer Visited Till now!!!")
                        else:
                            print('*'*10,"User details",'*'*10)
                            print("User_name",' '*10,"User_Phoneno",' '*10,"items",' '*50,"quantity",' '*20,"cost_perkg",' '*20,"cost_total",' '*20,"Total_Bill")
                            for p,q,r,s,t,u,v in zip(user_name,user_num,users_items_bought,user_items_bought_quantity,user_eachitems_bought_cost_perkg,user_eachitems_bought_cost_total,user_bill):
                                print(p,' '*10,q,' '*10,r,' '*10,s,' '*10,t,' '*10,u,' '*20,v)
                    elif ch==6:
                        if user_name==[]:
                            print("No Revenue Generated!!!")
                        else:
                            print('*'*10,"Today's Report",'*'*10)
                            for q in user_bill:
                                revenue=revenue+q
                                print("Revenue Generated ---",revenue)
                                print("Inventory We Left With")
                                print("veggies",' '*10,"quantity",' '*5,"S_P ",' '*6,"C_P")
                                for aa,ab,ac,ad in zip(veggies,quantity,S_P,C_P):
                                    print(aa,' '*10,ab,' '*10,ac,' '*10,ad)
                                print("Itemized Profit----")
                                print("Sold Veggies",' '*10,"Sold Quantity",' '*10,"Actual Price",' '*10,"Sold Price",' '*10,"Profit we got")
                                for ae,af,ag,ah,ai in zip(sold_items,sold_items_qty,sold_items_cp,sold_items_sp,sold_items_profit):
                                    print(ae,' '*10,af,' '*10,ag,' '*10,ah,' '*10,ai)
                    elif ch==7:
                        print("Exited from Shopkeeper View")
                        break
                                        
                    else:
                        print("Choose correct option!!!")
                break        
            else:
                print("Login Failed,Try Again")   
    elif view==2:
        print("Welcome to Vcube Veggetable Mart")
        while True:
            print("1.Add veggies to cart\n2.remove veggies in cart \n3.Update veggies in cart\n4.view cart\n5.Generate Bill")
            ch=int(input("choose an option:"))
            if ch==1:
                print('*'*10,"Vegetable We Have",'*'*10)
                print("veggies",' '*10)
                for z in veggies:
                    print(z)
                item=input("What do you want?")
                if item in cart:
                    print(item,"is already available in the cart Please use update option")
                elif item in veggies:
                    idx=veggies.index(item)
                    qty=float(input("how much quantity you want?"))
                    if quantity[idx]==0:
                        print("Out of Stock,Choose another veggie")
                    elif quantity[idx]<qty:
                        print("we have Less quantity of that veggie which is",quantity[idx],"kgs")
                    else:
                        cart.append(item)
                        sold_items.append(item)
                        cart_qty.append(qty)
                        sold_items_qty.append(qty)
                        quantity[idx]=quantity[idx]-qty
                        cost_per_kg=S_P[idx]
                        cart_per_kg.append(cost_per_kg)
                        costprice=qty*C_P[idx]
                        sold_items_cp.append(costprice)
                        amt=qty*S_P[idx]
                        sold_items_sp.append(amt)
                        profit=amt-costprice
                        sold_items_profit.append(profit)
                        total_cost_per_item.append(amt)
                        print(item,"is successfully added to cart")
                else:
                    print("item is not available in our shop")
            elif ch==2:
                cart_remove=input("Enter the veggie you want to remove?")
                if cart_remove in cart:
                    idx_remove_cart=cart.index(cart_remove)
                    cart.remove(cart_remove)
                    del cart_qty[idx_remove_cart]
                    del cart_per_kg[idx_remove_cart]
                    del total_cost_per_item[idx_remove_cart]
                    print(cart_remove,"is successfully removed from the cart")
                else:
                    print("Veggie is not available in the cart")
            elif ch==3:
                cart_update=input("Enter the veggie you want to update?")
                if cart_update in cart:
                    idx_item_update_cart=cart.index(cart_update)
                    qty_update_cart=float(input("How much quantity to update?"))
                    if cart_qty[idx_item_update_cart]>qty_update_cart:
                        up_qty=cart_qty[idx_item_update_cart]-qty_update_cart
                        quantity[idx]=quantity[idx]+up_qty
                    if cart_qty[idx_item_update_cart]<qty_update_cart:
                        up_qty=qty_update_cart-cart_qty[idx_item_update_cart]
                        quantity[idx]=quantity[idx]-up_qty
                    cart_qty[idx_item_update_cart]=qty_update_cart
                    total_cost_per_kg_update=qty_update_cart*cart_per_kg[idx_item_update_cart]
                    total_cost_per_item[idx_item_update_cart]=total_cost_per_kg_update
                    print(cart_update,"is successfully updated from the cart") 
                else:
                    print("Veggie is not available in the cart")
            elif ch==4:
                if cart==[]:
                    print("Your Cart is Empty Please Add Veggies")
                else:
                    print('*'*10,"CART",'*'*10)
                    print("Cart     Quantity   Priceperkg   Totalprice")
                    for i,j,k,l in zip(cart,cart_qty,cart_per_kg,total_cost_per_item):
                        print(i,'     ',j,'   ',k,'   ',l)  
            elif ch==5:
                if cart==[]:
                    print("Your Cart is Empty We Cannot Generate the Bill")
                else:
                    while True:
                        print("---Enter your Login Credentials----")
                        Owner_id =int(input("Enter your login id"))
                        Owner_password=input("Enter Password")
                        if Owner_id ==5082005and Owner_password=="Sukitha@2005":
                            total_bill=0
                            Cust_Name=input("Your Good Name Please!")
                            user_name.append(Cust_Name)
                            while True:
                                Cust_No=input("Your Mobile Number Please!")
                                if len(Cust_No)==10:  
                                    user_num.append(Cust_No)   
                                    print(Cust_Name," "*10,Cust_No)
                                    print(now.strftime("%Y-%m-%d %H:%M:%S"))
                                    print('*'*10,"Your Bill",'*'*10)
                                    print("Cart     Quantity   Priceperkg   Totalprice")
                                    for a,b,c,d in zip(cart,cart_qty,cart_per_kg,total_cost_per_item):
                                        print(a,'     ',b,'   ',c,'   ',d)
                                    for m in total_cost_per_item:
                                        total_bill=total_bill+m
                                    while True:
                                        ask=input("you want to give discount to customer: 'Yes or No'")
                                        if ask=="Yes" or ask=="yes":
                                            discount=int(input("How much percentage of discount you want to give to use"))
                                            dis_amt=(discount/100)*total_bill
                                            after_dis=total_bill-dis_amt
                                            user_bill.append(after_dis)
                                            print("Your Total Bill After Discount----",after_dis)
                                            print("HAPPY SHOPPING")
                                            print("THANK YOU VISIT AGAIN")
                                            users_items_bought.append(cart)
                                            user_items_bought_quantity.append(cart_qty)
                                            user_eachitems_bought_cost_perkg.append(cart_per_kg)
                                            user_eachitems_bought_cost_total.append(total_cost_per_item)
                                            cart=[]
                                            cart_qty=[]
                                            cart_per_kg=[]
                                            total_cost_per_item=[]       
                                            break
                                        elif ask=="No" or ask=="no":
                                            print("Your Total Bill----",total_bill)
                                            user_bill.append(total_bill)
                                            print("HAPPY SHOPPING")
                                            print("THANK YOU VISIT AGAIN")
                                            users_items_bought.append(cart)
                                            user_items_bought_quantity.append(cart_qty)
                                            user_eachitems_bought_cost_perkg.append(cart_per_kg)
                                            user_eachitems_bought_cost_total.append(total_cost_per_item)
                                            cart=[]
                                            cart_qty=[]
                                            cart_per_kg=[]
                                            total_cost_per_item=[]
                                            break
                                        else:
                                            print("enter correctly!!")
                                    break
                                elif len(Cust_No)<10 or len(Cust_No)>10:
                                    print("Number is not Valid Please Enter Correct Number!!! Number Must be 10 digits")
                                    
                                '''elif len(Cust_No)>10:
                                    print("Number is not Valid Please Enter Correct Number!!!")'''
                                    
                                '''else:
                                    break'''
                            break
                        else:
                            print("Login Failed,Try Again")
                    break                          
            else:
                print("Choose Correctly Sir")   
    elif view==3:
        print("Closing the Shop")
        break
    else:
        print("Choose Correctly Sir")
        
            

    
    
    

