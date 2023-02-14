import csv

pass_score = 30

def csv_to_dist(file):
  data = {}
  count = 1
  with open(file, 'r', encoding='utf-8') as f:
    info = csv.DictReader(f)
    
    for row in info:
      data[count] = row
      count += 1
  return data, count-1

def convert_result_to_csv(job_result, user_id):
  maximum = len(job_result)
  header = ['userID']
  for i in range(maximum):
    header.append('jobID')
  data = job_result
  data.insert(0, user_id)
  
  with open('jobprediction.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    
    writer.writerow(header)

    writer.writerow(data)


def get_country_name_by_id(id):
  data, _ = csv_to_dist('data/1.countries.csv')
  for i in data:
    if int(data[i]['id'])==int(id):
      return data[i]['name']

def process_user(data):
  tags = []
  user_id = data['id']
  interest = data['userInterests']
  country_id = data['countryID']
  country = get_country_name_by_id(country_id)
  for i in interest.split('/'):
    tags.append(i)
  return user_id, tags, country

def user_activity(user_id):
  course_id = []
  data, _ = csv_to_dist('data/6.activity.csv')
  for i in data:
    if int(data[i]['userID']) == int(user_id):
      if data[i]['courseID'] in course_id:
        continue
      course_id.append(data[i]['courseID'])
  return course_id
      
def get_tagID_by_courseID(course_id: list):
  courseID = course_id
  course_id = []
  data, _ = csv_to_dist('data/4.courses.csv')
  for i in data:
    if data[i]['id'] in courseID:
      if data[i]['courseCategories'] != '':
        value = data[i]['courseCategories'].split('/')
        course_id.extend(value)
  return course_id
      
def filter_tags_by_skills_score(userId, userTag):
  data, _ = csv_to_dist('data/7.skills.csv')
  datas = {}
  count = 0
  for i in data:
    if int(data[i]['userID']) == int(userId) and data[i]['tagID'] in userTag:
      count += 1
      datas[count] = {}
      datas[count]['tagID'] = data[i]['tagID']
      datas[count]['userID'] = data[i]['userID']
      datas[count]['score'] = data[i]['score']
      
  return datas, count
      

def process_tags(userTag, userId):
  result_tags, count = filter_tags_by_skills_score(userId, userTag)
  score = []
  new_score_list = []
  for i in result_tags:
    score.append(result_tags[i]['score'])
  for i in score:
    if i not in new_score_list:
      new_score_list.append(i)
  new_score_list.sort(reverse=True)
  
  return new_score_list, result_tags, count

def get_job_info(new_tag, userCountry):
  data, _ = csv_to_dist('data/5.jobs.csv')
  job_id_list = []
  count = 0
  for i in data:
    jobId = data[i]['id'] 
    jobLocation = data[i]['location']
    jobTag = data[i]['tags']
    if int(jobTag) == int(new_tag) and userCountry in jobLocation:
      count += 1
      job_id_list.append(jobId)
  return job_id_list
    

def get_user_info_by_id(user_id):
  jobId_lists = []
  data, length = csv_to_dist('data/3.users.csv')
  for i in data:
    if int(user_id) > int(data[length]['id']):
      print("you have exceeded user id")
      print(f"user id is from {data[1]['id']}-{data[length]['id']}")
      break
    else:
      if int(data[i]['id']) == int(user_id):
        user_result = process_user(data[i])
        userID = user_result[0]
        userTag = user_result[1]
        userCountry = user_result[2]
        scale, new_tag, count = process_tags(userTag, userID)
        if count > 0:
          for j in scale:
            for n in new_tag:
              if int(j) == int(new_tag[n]['score']):
                new_tags = new_tag[n]['tagID']
                # print(j, new_tags, userCountry)
                jobId = get_job_info(new_tags, userCountry)
                jobId_lists.extend(jobId)
        else:
          list_result = user_activity(userID)
          result = get_tagID_by_courseID(list_result)
          for i in result:
            jobId = get_job_info(i, userCountry)
            jobId_lists.extend(jobId)
  
  return jobId_lists[:20]


user_id = input("[+] Enter the user id to check: ")
if user_id == '':
  print("Your input can't be empty")
else:
  user_activity(user_id)
  job_result = get_user_info_by_id(user_id)
  convert_result_to_csv(job_result, user_id)
