def vacuum_cleaner_agent(location, status):
    x, y = location
    if status[x][y] == 'Dirty':
        return f"The vacuum cleaner is at ({x}, {y}) and it is dirty. Cleaning."
    else:
        return f"The vacuum cleaner is at ({x}, {y}) and it is clean. Moving."

status = [['Dirty', 'Clean'], ['Dirty', 'Dirty']]
location = (0, 0)

while True:
    action = vacuum_cleaner_agent(location, status)
    print(action)

    x, y = location
    if status[x][y] == 'Dirty':
        status[x][y] = 'Clean'

    if status[0][0] == 'Clean' and status[0][1] == 'Clean' and status[1][0] == 'Clean' and status[1][1] == 'Clean':
        print("All locations are clean. The vacuum cleaner is finished.")
        break

    if y < 1:
        location = (x, y + 1)
    elif x < 1:
        location = (x + 1, 0)
