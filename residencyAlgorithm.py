#TODO: create a safety net of unassigned students slotted into companies
from http.cookiejar import unmatched

# student tuple format
# (student_id, listing_id, student_rank, company_rank)
#id_ranking:
#student_id: id of the student, to return information to
#listing_id: id of the residency partner
#student_rank: the position the student ranked the company  (from 1 to 3)
#company_rank: the position the company ranked its students

#here were example variables for testing
#constants PLEASE PLEASE PLEASE DO NOT INTERACT
STUDENT_ID = 0
LISTING_ID = 1
STUDENT_RANK = 2
COMPANY_RANK = 3


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


#residency_rankings = [residency,[[student, score][student, score]...]
residency_rankings=[]
#[id, [score, company] [score, company], [score, company]]
student_rankings=[]
#[studentid, listingid]
studentResidencyMatchings=[]

#this is the algorithm to match the students with residencies
#input: it uses an array in the following [studentID, listingID, studentRanking, companyRanking]
#we get these values from the residency ranking table
#student_IDS: a list of Student IDS
#residencylist: can either be a list of the listingIDs or residincyID depending on the format of the input
#spacesArray: is a list of spaces each listing has
def calculateResidencies(input, studentIDS, residencyIDList, spacesArray) :

    #the first step iterates through all the listings and scores its students
    #using the student ranking+company ranking
    #if the company has more than one spot we divide by a balancing factor to
    #decrease the range of values. Balancing factor = positions/2+0.5
    for x in range(len(residencyIDList)) :
        #initate a list of scores for this residency
        current_residency_id = residencyIDList[x]
        #this is a temporary list
        residency_score_list = []
        current_position_count = spacesArray[x]

        #calculate balancing factor
        if current_position_count > 1 :
            balancing_factor = round(current_position_count/2)
        else :
            balancing_factor = 1
        #for each of the inputs. we add the student and company rank and add student id
        for y in input :
            if y[LISTING_ID]==current_residency_id:
                score = round((y[STUDENT_RANK]+y[COMPANY_RANK])/balancing_factor)
                residency_score_list.append([y[STUDENT_ID], score])

        #sort the list by score in acsending order and add that list to the resdiency rankings
        residency_score_list.sort(key=lambda scr: scr[1])
        residency_rankings.append([current_residency_id,residency_score_list])

    #for each student, we find their score in the residency rankings and list them
    #the goal of this is to find the students best score to increase their odds of getting that position
    for x in range(len(studentIDS)):
        # for each student
        current_student = studentIDS[x]
        current_scores = []
        # current_scores.append(current_student)
        for idx, y in enumerate(residency_rankings):
            for z in y[1]:
                if z[0] == current_student:
                    current_scores.append([residencyIDList[idx], z[1]])
        current_scores.sort(key=lambda scr: scr[1])
        current_scores.insert(0, current_student)
        student_rankings.append(current_scores)
    #print(student_rankings)

    #finally we iterate through all the students, and find a residency with a position for them to enter in
    for x in range(len(student_rankings)):
        scores = student_rankings[x]
        current_student = scores.pop(0)

        for y in range(len(scores)):
            company = residencyIDList.index(scores[y][0])

            if spacesArray[company] > 0:
                spacesArray[company] -= 1
                studentResidencyMatchings.append([current_student, scores[y][0]])
                break

    return studentResidencyMatchings


#formatted printing of variables of the process
#print("Student's rankings")
#print(student_rankings)
#for x in range(len(student_rankings)) :
#
#    print("Student ID:" + str(student_rankings[x][0]))

#    for y in range(1,len(student_rankings[x])) :
#        print("Company: " + str(companynames[residency_ids.index(student_rankings[x][y][0])]) + " - ID - " + str(student_rankings[x][y][0]) + " | " + "Score : " + str(student_rankings[x][y][1]))
#    print("----------------------------------------")
#print(studentResidencyMatchings)
#for x in studentResidencyMatchings :
#    print("Student ID: " + str(x[0]) + " | Company: " + companynames[residency_ids.index(x[1])])
