#Agent selector

import time
import random

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def main(data_for_agents, user_demand_roles, agent_selection_mode):

    # data_for_agents is a list that contains list of (name_of_agent(list index=0), is_available(list index=1), available_since(list index=2), roles_of_agent(list index=3)).
    # user_demand_roles are the roles which user wants in the agent who'll be handling this user's case. I have written this function with an assumption that 

    ans = []

    if agent_selection_mode == "all available mode":
        for i in range(len(data_for_agents)):
            #Checking for availability
            if i[1]:
                #Checking for Roles
                if i[3]==user_demand_roles:
                    #if available and the roles match, then it depends on agent whether he/she wants to go for the job.
                    #Let's assume the first available agent will go for job every time.[This is mere assumption or a way to add an element to ans list.]

                    ans.append(i[0]) #append agent name to ans list.
                    return ans
                

    elif agent_selection_mode == "least busy mode":

        max_time = 0:0:0
        j=-1
        for i in range(len(data_for_agents)):
            #Checking for availability
            if i[1]:
                #Checking for Roles
                if i[3]==user_demand_roles:
                    #if available then we'll check if the current agent is least busy.
                    # Here I am actually trying to compare time and find out least busy. Though it entirely depends on input format provided.
                    if max_time<(current_time - available_since):
                        max_time = current_time - available_since
                        j=i
        
        ans.append(data_for_agents[j][1])
        return ans

    elif agent_selection_mode == "random mode":
        ans.append(random.choice(data_for_agents)[1])
        return ans




#We Can Call main() with the required parameters and it will return a list that basically contains the name of the agent. Multiple roles passed by user can also by worked on through loops but I have considered only single role is submitted by the user.


