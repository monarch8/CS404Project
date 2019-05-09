import os

# Course id: Course Name
courses = {303: 'Data Structures' ,
           490: 'Web Development',
           371: 'Database',
           550: 'Design and Analysis of Algorithms',
           101: 'Python'}
# Professor id: Professor Name
professors = {1: 'John Smith',
              2: 'Samir Khan',
              3: 'Ann Jackson',
              4:'Lucas H',
              5:'Dave Johns'}
# topic id: Topic Name
topics = {1: 'Programming',
          2:'HTML',
          3:'Math',
          4: 'C++',
          5:'Python',
          6:'Stats',
          7:'Algorithms'}

#Course id: {topic id: percent of course}
courseTopic = {303: {1: 20, 2: 0, 3: 20, 4: 20, 5: 0, 6: 0, 7: 40},
               490: {1: 40, 2: 60, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0},
               371: {1: 30, 2: 0, 3: 30, 4: 0, 5: 40, 6: 0, 7: 0},
               550: {1: 10, 2: 0, 3: 20, 4: 20, 5: 0, 6: 10, 7: 40},
               101: {1: 25, 2: 0, 3: 15, 4: 0, 5: 40, 6: 0, 7: 20}}

#Professor id: {topic id: knowledge of topic}
expertiseTable = {1: {1: 5, 2: 1, 3: 2, 4: 5, 5: 5, 6: 1, 7: 1},
                  2: {1: 3, 2: 1, 3: 3, 4: 5, 5: 2, 6: 4, 7: 5},
                  3: {1: 2, 2: 5, 3: 1, 4: 1, 5: 3, 6: 1, 7: 1},
                  4: {1: 5, 2: 2, 3: 2, 4: 2, 5: 5, 6: 5, 7: 3},
                  5: {1: 2, 2: 2, 3: 5, 4: 4, 5: 2, 6: 5, 7: 4}}

def match(course, professor):

    tempCourseComp = []
    for i in range(1, 8):
        tempCourseComp.append(courseTopic[course][i])

    tempProfKnow = []
    for i in range(1, 8):
        tempProfKnow.append(expertiseTable[professor][i])

    rating = 0
    for i in range(0, 7):
        rating = rating + (tempCourseComp[i] * tempProfKnow[i])

    return rating

def main():
    #check every course
    for course in courses:
        score = 0
        prof = 0
        #check every professor
        for professor in professors:
            tempScore = match(course, professor)
            if score < tempScore:
                score = tempScore
                prof = professor


        print(str(prof) + " is teaching " + str(course))
        professors.pop(prof)


main()

