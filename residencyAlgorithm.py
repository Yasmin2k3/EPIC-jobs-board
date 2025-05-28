#TODO: create a safety net of unassigned students slotted into companies
from http.cookiejar import unmatched

# student tuple format
# (id_ranking, student_id, listing_id, student_rank, company_rank)
#id_ranking:
#student_id: id of the student, to return information to
#listing_id: id of the residency partner
#student_rank: the position the student ranked the company  (from 1 to 3)
#company_rank: the position the company ranked its students

#constants PLEASE PLEASE PLEASE DO NOT INTERACT
STUDENT_ID = 0
LISTING_ID = 1
STUDENT_RANK = 2
COMPANY_RANK = 3

#example scenario
# 5 students
# 3 residencies

#TODO: temporary variables, make them be able to extract details from the data base
#the amount of positions per residency



# Example Constants
STRIPE = 0
WRXFLOW = 1
INTERCOM = 2
TOTALCARE = 3
KNEAT = 4
MANNA = 5
companynames = ["Stripe","WRXFLO","Intercom","Totalcare","Kneat", "Mana"]
#here is a two position residency at id `1
studentTupleExample = (
    #student 1
    (1, STRIPE, 1,1),
    (1,WRXFLOW,2,2),
    (1,INTERCOM,3,1),
    #student 2
    (2,WRXFLOW,1,1),
    (2,INTERCOM,2,2),
    (2,STRIPE,3,3),
    #student 3
    (3,TOTALCARE,1,2),
    (3,INTERCOM,2,3),
    (3,STRIPE,3,2),
    #student 4
    (4, KNEAT, 1, 3),
    (4, TOTALCARE, 3, 1),
    (4, MANNA, 3, 2),
    #student 5 (unlucky chap :( )
    (5, MANNA, 1, 1),
    (5,TOTALCARE,2,    3),
    (5, KNEAT,3,    2),
    # student 5 (unlucky chap :( )
    (6, WRXFLOW, 1, 3),
    (6, KNEAT, 2, 3),
    (6, MANNA, 2, 3)
)
#variables for calculations

position_count = [1,1,1,1,1,1]
residency_count=len(position_count)
residency_rankings=[]
#[id, [score, company] [score, company], [score, company]]
student_rankings=[]

studentResidencyMatchings=[]

#input tuple is a filtered section of the table
#Im assuming I'm getting a filtered table
#this function returns the id of the student the company would want most
def residencyCalculateList(input_tuple=studentTupleExample) :

    for x in range(residency_count) :
        #initate a list of scores
        residency_score_list = []
        current_position_count = position_count[x]
        if current_position_count > 1 :
            balancing_factor = round(current_position_count/2)
        else :
            balancing_factor = 1
        #for each of the inputs. we add the student and company rank and add student id
        for y in input_tuple :
            if y[LISTING_ID]==x:
                score = round((y[STUDENT_RANK]+y[COMPANY_RANK])/balancing_factor)
                residency_score_list.append([y[STUDENT_ID], score])
        #sort the list by score
        residency_score_list.sort(key=lambda scr: scr[1])
        residency_rankings.append(residency_score_list)
        #return the lowest score
def studentCalcBestCompany() :
    for x in range(6) :
        #for each student
        current_student = x+1
        current_scores = []
        #current_scores.append(current_student)
        for idx, y in enumerate(residency_rankings):
            for z in y:
                if z[0]==current_student :
                    current_scores.append([idx,z[1]])
        current_scores.sort(key=lambda scr: scr[1])
        current_scores.insert(0,current_student)
        student_rankings.append(current_scores)

    pass
unmatchedStudents=[]
def matchStudentResidency() :
    for x in range(len(student_rankings)):
        scores=student_rankings[x]
        current_student = scores.pop(0)

        for y in range(3) :
            company = scores[y][0]
            if position_count[company] > 0:
                position_count[company]-=1
                studentResidencyMatchings.append([current_student,company])
                break
            elif y==2 : #unmatched student stuff
                print("not in company" +str(current_student))
                unmatchedStudents.append(current_student)
    #while len(studentResidencyMatchings) < residency_count :
        #MatchUnmatched()

def MatchUnmatched() :

    pass
residencyCalculateList()
studentCalcBestCompany()

#format residence count list
print("Residency Count")
for x in range(residency_count) :

    print(companynames[x]+":")

    for y in range(len(residency_rankings[x])) :
        print("Student ID: " + str(residency_rankings[x][y][0]) + " | " + "Score : " + str(residency_rankings[x][y][1]))
    print("----------------------------------------")
print(student_rankings)
print("Student's rankings")
for x in range(len(student_rankings)) :

    print("Student ID:" + str(student_rankings[x][0]))

    for y in range(1,4) :
        print("Company: " + str(companynames[student_rankings[x][y][0]]) + " | " + "Score : " + str(student_rankings[x][y][1]))
    print("----------------------------------------")




matchStudentResidency()

print(position_count)
print(studentResidencyMatchings)
for x in studentResidencyMatchings :
    print("Student ID: " + str(x[0]) + " | Company: " + companynames[x[1]])
