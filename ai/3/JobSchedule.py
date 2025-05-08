class Job:
    def __init__(self,job_id,deadline,profit):
        self.job_id=job_id
        self.deadline=deadline
        self.profit=profit
        
    def __repr__(self):
        return f"job id {self.job_id} time: {self.deadline}"

def job_scheduling(jobs):
    print("jobs to be scheduled are: ")
    for job in jobs:
        print(job)
        
    print()
    print("--"*40)
    print()

    jobs.sort(key=lambda job : job.profit , reverse=True)

    print("jobs with max to min profit are: ")
    for job in jobs:
        print(job)
        
    print()
    print("--"*40)
    print()

    total_profit=0
    scheduled_jobs=[]

    max_deadline=max(job.deadline for job in jobs)
    slots=[-1]*(max_deadline+1)

    for job in jobs:
        for t in range(job.deadline ,0,-1):
            if slots[t]==-1:
                slots[t]=job.job_id
                total_profit+= job.profit
                scheduled_jobs.append((job.job_id,t))
                print(f"job {job.job_id} scheduled at time {t}")
                break
            else:
                print("searching for an earlier time slot ")


    print()
    print("--"*40)
    print()
    
    for job_id, time_slot in scheduled_jobs:
     print(f"Job {job_id} at time {time_slot}")
    print(f"total profit= {total_profit}")
    return scheduled_jobs,total_profit

if __name__ == '__main__':

    n=int(input("how many jobs to schedule? "))
    jobs=[]
    for i in range(n):
        print(f"\nEnter details for job {i+1}:")
        job_id=input("enter job id : ")
        deadline=int(input("enter job deadline : "))
        profit=int(input("enter profit : "))
        jobs.append(Job(job_id,deadline,profit))
        
    scheduled_jobs,total_profit=job_scheduling(jobs)
    
        