# Optimal Job Profit Scheduling

def max_profit_schedule(start_times, end_times, profits):
    number_of_jobs = len(start_times)
    # combine jobs into a single list 
    jobs = []
    for i in range(number_of_jobs):
        job_entry = (start_times[i], end_times[i], profits[i])
        jobs.append(job_entry)
    #sort jobs based on end time 
    for i in range(number_of_jobs - 1):
        for j in range(0, number_of_jobs - 1 - i):
            #compare end times
            if jobs[j][1] > jobs[j + 1][1]:
                temp_job = jobs[j]
                jobs[j] = jobs[j + 1]
                jobs[j + 1] = temp_job

    # create dp table
    dp = [0] * number_of_jobs
    dp[0] = jobs[0][2]
    # fill dp table
    for i in range(1, number_of_jobs):
        include_profit = jobs[i][2] #include current job
        # find the last non-overlapping job 
        last_valid_index = -1
        for previous_job_index in range(i - 1, -1, -1): #go thru backwards 
            # if previous job ends before or when the current job starts-> its valid
            if jobs[previous_job_index][1] <= jobs[i][0]:
                last_valid_index = previous_job_index
                break
        # if a valid previous job was then add its val from the dp
        if last_valid_index != -1:
            include_profit = include_profit + dp[last_valid_index]
        exclude_profit = dp[i - 1]
        #store whichever larger
        dp[i] = max(include_profit, exclude_profit)
    return dp[number_of_jobs - 1]

if __name__ == '__main__':
    start_times = list(map(int, input().split()))
    end_times = list(map(int, input().split()))
    profits = list(map(int, input().split()))

    result = max_profit_schedule(start_times, end_times, profits)
    print(result)
