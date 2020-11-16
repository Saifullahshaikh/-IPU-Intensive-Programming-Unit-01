def Grade(sub1,sub2,sub3,sub4,sub5):
    lst=[sub1,sub2,sub3,sub4,sub5]
    for i in lst:
        if i>=0 and i<=100:
            if i >= 80:
                print(i,'Grade\t A \n Conratulation!')
            elif i > 70:
                print(i,'Grade \t B \n Conratulation!')
            elif i > 60:
                print(i,'Grade \t C \n Good!')
            elif i > 50:
                print(i,'Grade \t D \n pass')
            elif i > 40:
                print(i,'Grade \t E \n pass but work hard')
            else:
                print(i,'Grade \t F \n Sorry you are fail')
        else:
            print("You entered invalid marks")
Grade(80,90,50,40,10)

    


