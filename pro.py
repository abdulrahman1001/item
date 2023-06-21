menu= {'latte':50,'pizza':20}

while True:
    print("-enter 1 for add item\n -enter 2 for delete item \n -enter 3 for update price ")
    item=input("('enter  for exit'): ")
    
    if item=='':
        break
    
    elif int(item)==1:
        add= input('enter the name of item').lower()
        price=int(input('enter the price of item'))
        menu.update({add:price})
        print('-'*30)
    elif int(item)==2:
            name_item=input('enter the name of item:').lower()
            if name_item in menu.keys():
                
             del menu[name_item]
             print(f'item {name_item} has deletd')
             print('-'*20)

            else:
                print('not found item') 
                print('-'*20)
    elif int(item)==3:
         name_item=input('enter the name of item:').lower()
         if name_item in menu.keys(): 
            new_price= int(input('enter new price:'))
            menu[name_item] =new_price
            print(f'{name_item} has changed')
            print('-'*20)
         else:
          print('item not fount')
          print('-'*20)
                  
    elif item not in menu:
        print('item not found') 
        print('-'*30)
        
        

                
        
    
for name,count in menu.items():
    print(f'{name}:{count} riyal')    
    
  
    
  
            


            
        
    
             
    
    
    
   
    

   
    
