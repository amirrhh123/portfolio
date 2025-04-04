import mysql.connector
from persiantools.jdatetime import JalaliDateTime
import calendar
import time
tooth_extraction_cost=int(1000000)
Root_canal_therapy_and_Dental_filling=int(4000000)
Dental_laminate=int(12000000)
dental_implant=int(23000000)
Physiotherapy=int(350000)
Orthopedic=int(280000)




try:
        database=mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="ahf138499" )
        

        print("connected")  
        cursor=database.cursor()  
except:
        print(" connected")    



today=JalaliDateTime.today()
year=today.strftime("%Y")
month=today.strftime("%m")
day=today.strftime("%d")
hour=today.strftime("%H")
min=today.strftime("%M")
today_date=JalaliDateTime(int(year),int(month),int(day),int(hour),int(min))

print(today_date)

while True:
    print("Welcome to our medical complex.\nHow can we help you?")
    MainQuestion=str(input("1.Dentistry\n2.Physiotherapy\n3.Orthopedic\n---->"))

    

    if MainQuestion=="1":
        while True:
            query1="SELECT days FROM medical_complex.evendays_dentistmohamadi  where availability='(1)' "
            cursor.execute(query1)
            result1=cursor.fetchall()
            for i in result1:
                for z in i:
                    print(z)
            query2="SELECT days FROM medical_complex.odddays_dentistkamali  where availability='(1)' "
            
            cursor.execute(query2)
            result2=cursor.fetchall()
            for i in result2:
                for z in i:
                    print(z)
            VisitDentist=str(input("Please select visit time:  "))
        
            if VisitDentist=="1": 
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((85*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((80*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((75*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah")
                                        cursor.execute(f"")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {(tooth_extraction_cost):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((85*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((80*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((75*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {(Root_canal_therapy_and_Dental_filling):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((85*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((80*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((75*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {(Dental_laminate):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break    

                       
                   
                    
                
            elif VisitDentist=="2":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((85*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((80*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((75*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {(tooth_extraction_cost):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((85*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((80*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((75*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {(Root_canal_therapy_and_Dental_filling):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((85*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((80*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((75*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {(Dental_laminate):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="3":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((85*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((80*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((75*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {(tooth_extraction_cost):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((85*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((80*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((75*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {(Root_canal_therapy_and_Dental_filling):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((85*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((80*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((75*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {(Dental_laminate):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="4":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((85*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((80*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((75*tooth_extraction_cost)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {(tooth_extraction_cost):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((85*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((80*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((75*Root_canal_therapy_and_Dental_filling)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {(Root_canal_therapy_and_Dental_filling):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((85*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((80*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((75*Dental_laminate)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {(Dental_laminate):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="5":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="6":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break


                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="7":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="8":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="9":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="28":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="29":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break


                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="30":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="31":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="32":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="33":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="34":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="35":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="36":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break


                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Sunday/Esfand 5th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="10":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                        
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                        
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                        
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                        
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="11":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break


                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="12":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="13":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="14":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="15":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="16":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="17":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    nsurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    nsurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    nsurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="18":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="37":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="38":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="39":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="40":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="41":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                    
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                    
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                    
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                    
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="42":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="43":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="44":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="45":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Tuesday/Esfand 6th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="19":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break


                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="20":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="21":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="22":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="23":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="24":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="25":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="26":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="27":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="46":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(10-11) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="47":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(11-12) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="48":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(12-13) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="49":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(13-14) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="50":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(14-15) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="51":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(15-16) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="52":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break
                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(16-17) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="53":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(17-18) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_dentistkamali set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            elif VisitDentist=="54":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                Operation=str(input("What is your operation?\n1.Tooth extraction\n2. Root canal therapy and Dental filling\n3.Dental laminate\4.Dental implant \n---->"))
                                if Operation=="1":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="2":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                elif Operation=="3":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break


                                elif Operation=="4":
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((85*dental_implant)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((80*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {((75*dental_implant)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','Niro haye mosalah')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Thursday/Esfand 8th(18-19) and costs {(dental_implant):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'dentistary','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_dentistmohamadi set availability= replace(availability,'(1)','(2)') where num='{VisitDentist}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1) 
                                    
                                    break

                                else:
                                    print(" valid")
                                    

                    else:
                        print(" valid")    
                        

                break
            else:
                print("not valid")        
            break

    elif MainQuestion=="2":    
        while True:
            query1="SELECT days FROM medical_complex.evendays_physiotherapymoradbeigi  where availability='(1)' "
            cursor.execute(query1)
            result1=cursor.fetchall()
            for i in result1:
                for z in i:
                    print(z)
            
            Visitphysio=str(input("Please select visit time:  "))
        
            if Visitphysio=="1": 
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
                            
                           
            elif Visitphysio=="2":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(11-12) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
                            
                           
            elif Visitphysio=="3":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(12-13) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="4":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(13-14) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="5":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(14-15) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="6":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(15-16) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="7":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(16-17) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="8":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(17-18) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="9":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(18-19) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="10":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(10-11) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="11":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(11-12) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="12":
                
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(12-13) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="13":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(13-14) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="14":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(14-15) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="15":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(15-16) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="16": 
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(16-17) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="17":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(17-18) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="18":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Monday/Esfand 6th(18-19) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="19":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(10-11) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="20":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(11-12) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="21":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(12-13) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="22":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(13-14) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="23":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(14-15) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="24":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(15-16) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="25":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(16-17) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="26":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(17-18) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            elif Visitphysio=="27":
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    organ=int(input("How many organs do you want to undergo physiotherapy?\n--->"))
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((85*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((80*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {((75*organ*Physiotherapy)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Wednesday/Esfand 7th(18-19) and costs {(organ*Physiotherapy):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'physiotherapy','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.evendays_physiotherapymoradbeigi set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
            else:
                print("not valid")

                
    elif MainQuestion=="3":    
        while True:
            query1="SELECT days FROM medical_complex.odddays_orthopedicfalahian  where availability='(1)' "
            cursor.execute(query1)
            result1=cursor.fetchall()
            for i in result1:
                for z in i:
                    print(z)
            
            Visitphysio=str(input("Please select visit time:  "))
        
            if Visitphysio=="28": 
                name=str(input("Please enter your full name:\n---->"))
                while True: 
                    code_meli=str(input("Please enter your ID code:\n---->"))
                    if len(code_meli)==10:
                        age=int(input("Please enter your age:\n---->"))
                        while True:
                            tel=str(input("Please enter your telephone number:\n---->"))
                            if len(tel)==11:
                                    
                                    insurance=str(input("what is your insurance?\n1.Taamin ejtemaei\n2.Razi\n3.Niro haye mosalah\n4.none\n---->"))
                                    if insurance=="1":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((85*Orthopedic)/100):,} toman")
                                        cursor.execute(f"INSERT INTO medical_complex.clients(client_Name, id_code, telephone, age, section, insurance) VALUES('{name}','{code_meli}','{tel}',{age},'orthopedic','taamin ejtemaei')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_orthopedicfalahian set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        database.close()
                                        time.sleep(1)
                                    elif insurance=="2":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((80*Orthopedic)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'orthopedic','Razi')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_orthopedicfalahian set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1)
                                    elif insurance=="3":
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {((75*Orthopedic)/100):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'orthopedic','Niro haye mosalah")

                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_orthopedicfalahian set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    elif insurance=="4": 
                                        print(f"your vistit is Saturday/Esfand 4th(10-11) and costs {(Orthopedic):,} toman")
                                        cursor.execute(f"insert into medical_complex.clients(client_Name,id_code,telephone,age,section,insurance) VALUES('{name}','{code_meli}','{tel}',{age},'orthopedic','none')")
                                        database.commit()
                                        cursor.execute(f"update medical_complex.odddays_orthopedicfalahian set availability= replace(availability,'(1)','(2)') where num='{Visitphysio}_';")
                                        database.commit()
                                        time.sleep(1) 
                                    
                                    break
                            
