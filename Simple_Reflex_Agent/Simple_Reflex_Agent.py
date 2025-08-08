import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# 2*2 Environment
enviroment = {
    "Room1" : "Clean",
    "Room2" : "Dirty",
    "Room3" : "Clean",
    "Room4" : "Dirty"
}

# mapping for grid
room_pos = {
    # top - left
    "Room1" : (0, 1),
    # top - right
    "Room2" : (1, 1),
    # bottom - left
    "Room3" : (0, 0),
    # bottom - right
    "Room4" : (1, 0)
}

rooms = list(enviroment.keys())
agent_index = 0

# reflex agent 
def reflex_agent(state):
    if state == "Dirty":
        return "Clean"
    else:
        return "Move"

#  draw the grid
def draw_environment(env , agent_pos , step):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Step : {step} - Agent in {rooms[agent_index]}")

    for room , pos in room_pos.items():
        x,y = pos
        color = 'red' if enviroment[room] == "Dirty" else 'green'
        rect = patches.Rectangle((x, y), 1, 1, facecolor = color,edgecolor= 'black')
        ax.add_patch(rect)
        ax.text(x + 0.5, y + 0.5, room, ha='center', va='center', color='white', fontsize=10)

    # Draw Agent
    agent_x , agent_y = room_pos[rooms[agent_pos]]
    agent_patch = patches.Circle((agent_x + 0.5, agent_y + 0.5 ), 0.1 , color='blue')
    ax.add_patch(agent_patch)

    plt.pause(2)
    plt.close()

# run the agent
plt.ion()
step = 8

for step in range(step):
    curr_room = rooms[agent_index]
    state = enviroment[curr_room]
    action = reflex_agent(state)

    draw_environment(enviroment, agent_index , step+1)

    if action == "Clean":
        enviroment[curr_room] = "Clean"
    else:
        agent_index = (agent_index + 1) % len(rooms)

plt.ioff()
plt.show()
print("!! Task Complete !!")