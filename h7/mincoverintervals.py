# minimum cover of intervals

def get_left_endpoint(interval):
    # return the left endpoint of the interval
        # so that we can sort by left endpoint 
    return interval[0]


def smallest_interval_cover(left_endpoints, right_endpoints):
    #combine left and right endpoints into list of intervals (left, right) tuples
    intervals = []
    for index in range(len(left_endpoints)):
        interval = (left_endpoints[index], right_endpoints[index])
        intervals.append(interval)

    #sort intervals by left endpoint so we can go from leftmost interval
    intervals.sort(key=get_left_endpoint)


    chosen_cover_intervals = [] #list of intervals chosen for the cover
    current_coverage_point = intervals[0][0] #tells how far we already covered 
    total_intervals = len(intervals)
    current_index = 0

    #keep selecting intervals as long as we can push coverage farther to the right of the number line
    while current_index < total_intervals:
        best_interval = None
        farthest_right_reach = current_coverage_point

        #check all intervals that start at or before the current coverage point
        while current_index < total_intervals and intervals[current_index][0] <= current_coverage_point:
            #choose interval that extends farthest to the right
            if intervals[current_index][1] > farthest_right_reach:
                farthest_right_reach = intervals[current_index][1]
                best_interval = intervals[current_index]
            current_index += 1 #move to next interval in sorted list

        #no interval starts at or before current coverage point
            #cannot extend any further
        if best_interval is None:
            break

        #add interval that gave farthest cover extension to the right
        chosen_cover_intervals.append(best_interval)

        #extend covered region 
        current_coverage_point = farthest_right_reach

    return chosen_cover_intervals #reutrn list of chosen intervals for minimum cover


if __name__ == '__main__':
    #example input
    left_endpoints = [1, 2, 3, 6, 7, 10]
    right_endpoints = [5, 4, 8, 9, 12, 11]

    ## add output for the left and right endpoitns so that i can see original input 
        #and then the output from those intervals

    result = smallest_interval_cover(left_endpoints, right_endpoints)

    print("intervals chosen for minimum cover:")
    for interval in result:
        print(interval)