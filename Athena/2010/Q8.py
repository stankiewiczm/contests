from numpy import *
#hihellolookhavealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamiliardoesit
#"""
#A avealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamilia
#D drome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamiliard
#E ellolookhavealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamiliardoe
#F   fghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsf
#H hihellolookhavealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjh  
#I ihellolookhavealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamiliardoesi
#K khavealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlk
#L llolookhavealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamil
#M me xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfam
#N ndrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soun
#O olookhavealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamiliardo
#P palindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsap
#R rome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamiliar
#S spalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx sounds
#T tthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx soundsfamiliardoesit
#V vealookatthispalindrome xxqwertyuiopasdfghjklzxcvbnmmnbv
#U uiopasdfghjklzxcvbnmmnbvcxzlkjhgfdsapoiuytrewqxx sou

Total = 112;            # jedno-literowe palindromy.
MidP = (2**26*2-1)*4+2  # Ilosc palindromow w srodku

# Jezeli palindrom siedzie caly w "xxqwerty...ytrewqxx", to liczymy ilosc slow:
Total += 2**25-1;       # na 25 liter, nie liczas x;
Total += MidP;          # za x



TODO = ['A','D','E','F','H','I','K','L','M','N','O','P','R','S','T','U','V','X'];




