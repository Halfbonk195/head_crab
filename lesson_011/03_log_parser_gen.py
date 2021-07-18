file_name_r = 'events.txt'


def line_processing(line):
    date = line[1:17]
    event = line[29:-1]

    return date, event


def logparser(file_name):
    with open(file_name, 'r') as file_r:

        old_line = None
        event_count_inner = 0

        for line in file_r:
            new_date, new_event = line_processing(line)

            if old_line != new_date and old_line is not None:
                group_time_inner = old_line
                sent_event_count = event_count_inner
                event_count_inner = 0
                yield group_time_inner, sent_event_count

            if 'NOK' in new_event:
                event_count_inner += 1
            old_line = new_date

        yield new_date, event_count_inner


grouped_events = logparser(file_name_r)
for group_time, event_count in grouped_events:
    print(f'[{group_time}] {event_count}')
