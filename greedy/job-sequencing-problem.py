# encoding:utf-8
# 问题描述：有n个工作任务，每个工作任务都有deadline时间，假设每个工作任务都可以在单元(1)时间内完成，如果任务在deadline时间内完成，
# 则会有一定的收益，那么请问最大收益的任务完成顺序。
# exp: a, 1, 20
#      b, 1, 10
#      c, 2, 20
#      d, 3, 5
# 那么完成顺序应该是a,c,d
## 解决方法：
# 对profit从大到小排序，把job放在deadline-1的位置，如果deadline-1位置上没有空位，那么就继续向前找空位，如果找到的话就入座，找不到就放弃该任务。


def getJobSequence(sorted_jobs, max_deadline):
    res_status_list = [False]*max_deadline
    finish_time = 0
    profit = 0
    jobs = [None]*max_deadline
    for job in sorted_jobs:
        job_profit = job[-1]
        job_id = job[0]
        job_deadline = job[1]
        if False in res_status_list[:job_deadline]:  # 说明还有可以存储的地方
            # 找到所有可以存储的位置
            valid_ind = [i for i in range(len(res_status_list[:job_deadline])) if res_status_list[:job_deadline][i]==False]
            jobs[valid_ind[-1]] = job_id
            res_status_list[valid_ind[-1]] = True
            profit+=job_profit
    print("job sequence is{}, and finish time is {}, and get total profit is {}".format(jobs, finish_time, profit))


if __name__ == "__main__":
    jobs = [['J1', 5, 200], # Job Array 
       ['J2', 3, 180], 
       ['J3', 3, 190], 
       ['J4', 2, 300], 
       ['J5', 4, 120],
       ['J6', 2, 100]] 
    sorted_jobs = sorted(jobs, key=lambda  x: x[2], reverse=True)
    max_deadline = max(jobs, key=lambda  x: x[1])[1]
    max_deadline = 3
    getJobSequence(sorted_jobs, max_deadline)
