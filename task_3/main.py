import sys
from operations import load_logs, parse_log_line, filter_logs_by_level, count_logs_by_level, display_log_counts, display_filtered_log
      
try:
    cmd, *args = sys.argv
    log_list = []
    for line in load_logs(args[0]):
        log_list.append(parse_log_line(line))

    if len(args) > 1:
        filtered_by_log_level = filter_logs_by_level(log_list, args[1])
        all_logs = count_logs_by_level(log_list)
        display_log_counts(all_logs)
        display_filtered_log(filtered_by_log_level, args[1])
    else:

        all_logs = count_logs_by_level(log_list)
        display_log_counts(all_logs)

except Exception as ex:
    print(ex)
